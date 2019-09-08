# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#
#     Примечание: Списки фруктов создайте вручную в начале файла.
#
fruits_1 = ["apple", "banana", "orange"]
fruits_2 = ["peach", "banana", "lemon", "grape"]
equal_fruits = [fruit for fruit in fruits_1 if fruits_2.__contains__(fruit)]
print(equal_fruits)
# 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
#
#     Элемент кратен 3,
#     Элемент положительный,
#
#     Элемент не кратен 4.
#
#     Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
#
numbers = [-2, 1, 4, 5, 10, 523, 534, 34, 55, 77, 12, 17, 333, 9, 28, 27, -4]
result = [number for number in numbers if number % 3 == 0 and number > 0 and number % 4 != 0]
print(result)

# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
#
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
#     Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
#

from math import sqrt


def square_list(some_list: list):
    square_result = [sqrt(number) if number > 0 else number for number in some_list]
    return square_result


print(square_list(numbers))


# 4. Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.


def number_fun(number: int):
    if number < 1 or number > 100 or number == 13:
        raise ValueError
    return number ** 2


while 1:
    number = input("Type a number from 1 to 100\n")
    try:
        res_num = number_fun(int(number))
    except ValueError:
        print("You've entered either a wrong or unlucky number\n")
    except Exception as e:
        print("Something went completely wrong\n", e)
    else:
        print(f"Square is {res_num}\n")
        break
