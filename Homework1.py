class Task1(object):
    def runTask(self):
        print("Task1")
        while 1:
            inputString = input("Input a number or quit:")
            if inputString == "quit":
                break
            try:
                print(int(inputString) + 2)
            except Exception:
                print("You've typed not a number or quit")
            continue


class Task2(object):
    def runTask(self):
        print("Task2")
        while 1:
            inputString = input("Input a number from 0 to 9 or quit:")
            if inputString == "quit":
                break
            try:
                result = int(inputString)
                if 0 <= result < 10:
                    print(result ** 2)
                else:
                    print("You've entered a wrong number, try again")
            except Exception:
                print("You've typed not a number or quit")
            continue


class Task3(object):
    def quitTask(self, strArg):
        if strArg == "quit":
            quit(0)

    def runTask(self):
        print("Task3")
        while 1:
            name = input("Input your name or quit:")
            self.quitTask(name)
            second_name = input("Input your second name or quit:")
            self.quitTask(second_name)
            age = input("Input your age or quit:")
            self.quitTask(age)
            weight = input("Input your weight or quit:")
            self.quitTask(weight)
            try:
                ageInt = int(age)
                weightInt = int(weight)
                if ageInt <= 30 and 50 <= weightInt <= 120:
                    print("Patient " + name + " " + second_name + " is in good shape")
                elif 30 < ageInt <= 40 and (50 > weightInt or weightInt > 120):
                    print("Patient " + name + " " + second_name + " should take care of himself/herself")
                elif ageInt > 40 and (50 > weightInt or weightInt > 120):
                    print("Patient " + name + " " + second_name + " should go to a doctor")
            except Exception:
                print("You've typed not a number or quit")
            continue


task1 = Task1()
task1.runTask()
task2 = Task2()
task2.runTask()
task3 = Task3()
task3.runTask()
