import sys
from GuessGame import print_welcome
from simfir_core import create_folder, create_file, copy_file, delete, get_list, save_info

save_info("Start")

default_dir_file_name = "default_dir.txt"
none_string = "None"
slash_string = "/"
empty_string = ""


def see_help():
    print("Type -h to see all commands")


def load_def_dir():
    with open(default_dir_file_name, "r") as f:
        return f.readline()


try:
    default_dir = load_def_dir()
except FileNotFoundError:
    default_dir = None


def get_path():
    return default_dir + slash_string if default_dir and default_dir != none_string else empty_string


try:
    command = sys.argv[1]
except IndexError:
    see_help()
else:
    if command == "-l":
        try:
            second_arg = sys.argv[2]
        except IndexError:
            get_list(default_dir)
        else:
            if second_arg == "-p":
                try:
                    path = sys.argv[3]
                except IndexError:
                    see_help()
                else:
                    get_list(path)
    elif command == "-lfo":
        try:
            second_arg = sys.argv[2]
        except IndexError:
            get_list(default_dir, folders_only=True)
        else:
            if second_arg == "-p":
                try:
                    path = sys.argv[3]
                except IndexError:
                    see_help()
                else:
                    get_list(path, True)
            else:
                see_help()
    elif command == "-mkf":
        try:
            name = sys.argv[2]
        except IndexError:
            see_help()
        else:
            try:
                text = sys.argv[3]
            except IndexError:
                create_file(f"{get_path()}{name}")
            else:
                create_file(f"{get_path()}{name}", text)
    elif command == "-mkd":
        try:
            name = sys.argv[2]
        except IndexError:
            see_help()
        else:
            create_folder(f"{get_path()}{name}")
    elif command == "-c":
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            see_help()
        else:
            copy_file(f"{get_path()}{name}", f"{get_path()}{new_name}")
    elif command == "-d":
        try:
            name = sys.argv[2]
        except IndexError:
            see_help()
        else:
            delete(
                f"{get_path()}{name}")
    elif command == "-cd":
        try:
            name = sys.argv[2]
        except IndexError:
            see_help()
        else:
            create_file(default_dir_file_name, name)
    elif command == "-game":
        print_welcome()
    elif command == "-h" or command == "-help":
        print(f"current_default_dir ={default_dir}")
        print("-l - show list of files (add -p path to change path)")
        print("-lfo - show list of directories only (add -p path to change path)")
        print("-mkf name text(optional) - create file empty or with text")
        print("-mkd name - create directory")
        print("-c name new_name - copy file or directory")
        print("-d name - delete file or directory")
        print(f"-cd name - change default directory (type {none_string} to use current directory)")
        print("-game - Computer will guess your numbers")
        print("-h - print help")
    else:
        see_help()

save_info("Finish")
