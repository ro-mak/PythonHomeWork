import sys, os
from random import choice


def choose_random_element(some_list: list):
    if  some_list.__len__() == 0:
        return None
    return choice(some_list)


if sys.argv.__len__() > 1:
    command = sys.argv[1]
    if command == "list":
        list_to_choose_from = []
        for i in range(2, sys.argv.__len__()):
            list_to_choose_from.append(sys.argv[i])
        print(list_to_choose_from)
        print(choose_random_element(list_to_choose_from))
