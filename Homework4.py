# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
def avarage_grade(grades, subjects):
    grades = grades.split()
    int_lst = [int(x) for x in grades]
    summ_grades = sum(int_lst)
    while subjects == 0:
        subjects = int(input('Количество предметов не может быть равно 0,введите количество заново'))
    return round(summ_grades / subjects, 2) #Впринципе можно сократить subjects заменив его на len(grades)
grades = input('Введите оценки по вашим предметам')
subjects = int(input('Введите количество предметов'))
print(avarage_grade(grades, subjects))
# #
# # 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# # пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# # Функция должна принимать параметры как именованные аргументы. Реализовать
# # вывод данных о пользователе одной строкой.
def user(name, surname, birthday, city, email, phone):
    return 'Ваше имя: %s, Ваша фамилия: %s, Ваш год рождения: %d, Ваш город проживания: %s, Ваш email: %s, Ваш телефон: %d.'%(name, surname, birthday, city, email, phone)
name = str(input('Введите ваше имя'))
surname = str(input('Введите вашу фамилию'))
birthday = int(input('Введите ваш год рождения'))
city = str(input('Введите ваш город проживания'))
email = str(input('Введите ваш email'))
phone = int(input('Введите ваш номер телефона'))
print(user(name, surname, birthday, city, email, phone))
#
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Вариант 1.
def my_fync(arg_1, arg_2, arg_3):
    list_1 = [arg_1, arg_2, arg_3]
    if arg_1 == max(list_1) and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_1 == max(list_1) and arg_2 < arg_3:
        return arg_1 + arg_3
    elif arg_2 == max(list_1) and arg_1 > arg_3:
        return arg_2 + arg_1
    elif arg_2 == max(list_1) and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_3 == max(list_1) and arg_1 > arg_2:
        return arg_3 + arg_1
    elif arg_3 == max(list_1) and arg_2 > arg_1:
        return arg_3 + arg_2
arg_1 = int(input('Введите значение первого аргумента'))
arg_2 = int(input('Введите значение второго аргумента'))
arg_3 = int(input('Введите значение третьего аргумента'))
print(my_fync(arg_1, arg_2, arg_3))
# Вариант 2.
def my_fync(arg_1, arg_2, arg_3):
    list_1 = [arg_1, arg_2, arg_3]
    if arg_1 == min(list_1):
        return arg_2 + arg_3
    elif arg_2 == min(list_1):
        return arg_1 + arg_3
    elif arg_3 == min(list_1):
        return arg_2 + arg_1
arg_1 = int(input('Введите значение первого аргумента'))
arg_2 = int(input('Введите значение второго аргумента'))
arg_3 = int(input('Введите значение третьего аргумента'))
print(my_fync(arg_1, arg_2, arg_3))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая
# использование цикла.
# Вариант 1.
def my_func(x, y):
     return x ** y
x = int(input('Введите положительное число'))
y = int(input('Введите целое отрицательное число'))
print(my_func(x,y))
# Вариант 2.
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res
print(my_func(float(input()), int(input())))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.
def func_2 (numbers):
    numbers = numbers.split()
    int_lst = [int(x) for x in numbers]
    summ_numbers = sum(int_lst)
    print(summ_numbers)
    while 'q' or 'Q' in numbers: #не понимаю как задать условие что считать пока не будет символа
        # 'Q' или символ 'q'
        numbers = input('Введите числа через пробел')
        numbers = numbers.split()
        int_lst = [int(x) for x in numbers]
        summ_numbers += sum(int_lst)
        print(summ_numbers)
        if 'q' or 'Q' in numbers: #Здесь соответственно также не понмаю как задать условие, но понимаю
            #что в случае если условие выполнится то нужно заменить символ Q или q на ноль 
            numbers = numbers.split()
            int_lst = [int(x) for x in numbers]
            summ_numbers += sum(int_lst)
            print(summ_numbers)
    return 'Введен специальный символ!Программа завершена'
numbers = input('Введите числа через пробел')
print(func_2(numbers))

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(x, *word):
    return x.title() and word.title()
x = str(input('Введите любое слово с маленькой буквы'))
word = str(input('Введите любое слово с маленькой буквы'))
print(int_func(x, word))
