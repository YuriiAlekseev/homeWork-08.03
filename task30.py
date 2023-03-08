# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""
    list_ap = []
    for num in range(1, quantity + 1):
        an = first + (num - 1) * diff
        list_ap.append(an)
    return list_ap


# print("Введите первый элемент массива= ", end =" ")
# first = int(input())
# print("Введите разность элемент массива= ", end =" ")
# diff = int(input())
# print("Введите колличество элемент массива= ", end =" ")
# quantity = int(input())

# print(arithmetic_progression(first, diff, quantity))