def task1():
    my_list_1 = [2, 5, 8, 2, 12, 12, 4]
    my_list_2 = [2, 7, 12, 3]
    set1 = set(my_list_1)
    set2 = set(my_list_2)
    print(set1 - set2)


task1()


def printDate(arg):
    numbers = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое",
               "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое",
               "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое", "двадцать первое", "двадцать второе",
               "двадцать третье", "двадцать четвертое", "двадцать пятое", "двадцать шестое", "двадцать седьмое",
               "двадцать восьмое", "двадцать девятое", "тридцатое", "тридцать первое"]
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
              "декабря"]
    day = arg.split(".")[0]
    month = arg.split(".")[1]
    year = arg.split(".")[2]
    print(numbers[int(day) - 1], months[int(month) - 1], year, "года")


def task2():
    date1 = "02.11.2013"
    date2 = "19.08.2019"
    printDate(date1)
    printDate(date2)


task2()


def printUniqueNumbers(arg):
    result_list = []
    count = 0
    for number1 in arg:
        for number2 in arg:
            if number1 == number2:
                count += 1
        if count == 1:
            result_list.append(number1)
        count = 0
    print(result_list)


def task3():
    my_list_1 = [2, 2, 5, 12, 8, 2, 12]
    my_list_2 = [2, 2, 5, 12, 8, 2, 12, 8, 5, 10, 11, 20, 19]
    printUniqueNumbers(my_list_1)
    printUniqueNumbers(my_list_2)


task3()
