import shutil, os, datetime


def create_file(name, text=None):
    try:
        with open(name, "w", encoding="utf-8") as f:
            if text:
                f.write(text)
    except FileNotFoundError:
        print("Please, create a directory first.")


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Dir already exists")
    except FileNotFoundError:
        print(
            "Please, check if the path is correct. Maybe you are trying to create a directory in a non-existent directory")


def get_list(path=None, folders_only=False):
    none_string = "None"
    result = os.listdir(path if path and path != none_string else None)
    if folders_only:
        path_with_slash = f"{path}/"
        empty = ""
        result = [f for f in result if is_dir(str(f"{path_with_slash if path and path != none_string else empty}{f}"))]
    print(result)


def is_dir(file):
    return os.path.isdir(file)


def delete(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except OSError:
        print("Please, check if directory is not empty or if file exists")


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Dir already exists")
    else:
        try:
            shutil.copy(name, new_name)
        except FileNotFoundError:
            print("Please, check if these files exist")


def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} --- {message}"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")


if __name__ == "__main__":
    save_info("Start test")
    print("test")
    create_file("EmptyFile")
    create_file("FileWithText", "Text")
    create_folder("EmptyFolder")
    get_list()
    get_list(True)
    save_info("Stop test")
