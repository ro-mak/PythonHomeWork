import os, sys


def create_dirs():
    for i in range(0, 10):
        print("creating dirs")
        os.mkdir(os.path.join(os.getcwd(), f"dir_{i}"))


def delete_dirs():
    for i in range(0, 10):
        print("deleting dirs")
        os.rmdir(os.path.join(os.getcwd(), f"dir_{i}"))


if sys.argv.__len__() > 1:
    command = sys.argv[1]
    if command == "create":
        create_dirs()
    elif command == "delete":
        delete_dirs()
