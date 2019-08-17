while 1:
    b = input("Input a number or quit:")
    if b == "quit":
        break
    try:
        print(int(b) + 2)
    except Exception:
        print("You've typed not a number or quit")
        continue

