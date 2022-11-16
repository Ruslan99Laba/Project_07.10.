# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def list_reverced_start():
    my_list = ["Hello", "Active", "Hi", "Good", "Alarm"]
    return list_reverced(my_list)


def list_reverced(my_list):
    new_list = my_list.copy()
    for i in range(0, len(my_list), 2):
        new_list[i] = str(my_list[i])[-1::-1]
    return new_list


print(list_reverced_start())


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

def a_begginer_start():
    my_list = ["Hello", "Active", "Hi", "Good", "Alarm"]
    return a_begginer(my_list)


def a_begginer(my_list):
    new_list = []
    for i in my_list:
        if str(i).lower().startswith("a"):
            new_list.append(i)
        else:
            pass
    return new_list


print(a_begginer_start())


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def a_searching_start():
    my_list = ["Hello", "Active", "Hi", "Good", "Alarm"]
    return a_searching(my_list)


def a_searching(my_list):
    new_list = []
    for i in my_list:
        if "a" in str(i).lower():
            new_list.append(i)
    return new_list


print(a_searching_start())


# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def list_wathcer_start():
    my_list = ["Hello", 2, "Active", 36, 51, "Hi", "Good", 285, "Alarm"]
    return list_watcher(my_list)


def list_watcher(my_list):
    new_list = []
    for i in my_list:
        if type(i) is str:
            new_list.append(i)
    return new_list


print(list_wathcer_start())


# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

def one_count_symbol_start():
    my_str = "Hello, Active, Hi, Good, Alarm"
    return one_count_symbol(my_str)


def one_count_symbol(my_str):
    new_list = []
    for i in my_str:
        if my_str.count(i) == 1:
            new_list.append(i)
    return new_list


print(one_count_symbol_start())


# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

def string_count_symbol_start():
    my_str1 = "This is my first program"
    my_str2 = "It should work well"
    return string_count_symbol(my_str1, my_str2)


def string_count_symbol(my_str1, my_str2):
    new_list = []
    for i in my_str1 and my_str2:
        if my_str1.count(i) and my_str2.count(i):
            new_list.append(i)
    return new_list


print(string_count_symbol_start())
