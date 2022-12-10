import pandas as pd


def part_one(data):
    folders = map_folders(data)
    folders = calculate_foldersizes(folders)
    small_folder_size = folders[(folders["type"] == "dir") & (folders["size"] <= 100000)]["size"].sum()
    return small_folder_size


def part_two(data):
    hdd_size = 70000000
    required_space = 30000000
    folders = map_folders(data)
    folders = calculate_foldersizes(folders)
    free_space = hdd_size - folders[folders["directory"] == "/"]["size"].sum()
    missing_space = required_space - free_space
    minimum_delete = folders[(folders["type"] == "dir") & (folders["size"] >= missing_space)] \
        .sort_values("size", ascending=True).head(1)["size"].sum()
    return minimum_delete


def cd(directory, command):
    argument = command.split("\n")[0][3:]
    if argument == "/":
        return argument
    elif argument == "..":
        return directory[0:directory[:directory.rfind("/")].rfind("/")+1]
    else:
        return directory+argument+"/"


def map_folders(data):
    directory = "/"
    hdd = pd.DataFrame()
    for command in data.split("$ "):
        if command[0:2] == "cd":
            directory = cd(directory, command)
        elif command[0:2] == "ls":
            output = ls(command)
            folder = pd.DataFrame(columns=["directory", "name", "type", "size"])
            for item in output:
                item = item.split(" ")
                if item[0] == "dir":
                    type = "dir"
                    name = item[1]
                    size = "unknown"
                else:
                    type = "file"
                    name = item[1]
                    size = item[0]
                folder.loc[len(folder.index)] = [directory, name, type, size]
            hdd = pd.concat([hdd, folder], ignore_index=True)
    return hdd


def ls(command):
    output = command.split("\n")[1:]
    if output[-1] == "":
        output = output[:-1]
    return output


def calculate_foldersizes(folders):
    while sizecalcs_remaining(folders) > 0:
        for directory in folders["directory"].unique():
            if directory != "/":
                current = folders[folders["directory"]==directory]

                if len(current[current["size"]=="unknown"]) == 0:
                    if len(current) == 0:
                        size = 0
                    else:
                        size = current["size"].astype(int).sum()

                    parent = directory[0:directory[:directory.rfind("/")].rfind("/")+1]
                    #name = directory[directory.rfind("/"):-1]
                    name = directory[directory[:directory.rfind("/")].rfind("/")+1:-1]

                    folders.loc[(folders["directory"] == parent) & (folders["name"] == name), "size"] = str(size)

    folders["size"] = folders["size"].astype(int)
    return folders


def sizecalcs_remaining(folders):
    return len(folders[folders["size"] == "unknown"])
