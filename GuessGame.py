# Guess a number game

import random


def start_the_game():
    print("Game started")
    print("Please think of some number from 0 to 100 and I'll try to guess it")
    print(
        "Print one of the signs to help me guess a number: > (bigger than user's) < (smaller than user's) = (equals) ")
    help_messages = ["Help me please!\n",
                     "I beg you, give me the number\n",
                     "I'm nothing, I can't win\n",
                     "Who made me so emotional? Please help!\n"]
    default_min_number = 0
    default_max_number = 100
    current_min_number = default_min_number
    current_max_number = default_max_number
    comp_guess = random.randint(current_min_number, current_max_number)
    while True:
        try:
            previous_guess = comp_guess
            print(f"I guess it is {comp_guess}")
            user_input = input("Am I right?\n")
            if user_input == "=":
                print("At last...")
                break
            elif user_input == ">":
                current_max_number = comp_guess
            elif user_input == "<":
                current_min_number = comp_guess
            comp_guess = int((current_max_number + current_min_number) / 2)
            if comp_guess == previous_guess:
                print("You are cheating, I won't play with you...")
                break
            print(help_messages[random.randint(0, 3)])
        except Exception:
            print("You are cheating, I won't play with you...")
            break


def print_welcome():
    print("Hello my dear friend! Welcome to the Game!")
    print("Wanna play?")
    print("This time it's my turn to guess a number")
    ready_to_play = input("Are you ready to play?\n")
    ready_to_play = ready_to_play.lower()
    if ready_to_play.__contains__("yes") or ready_to_play.__contains__("да"):
        start_the_game()
