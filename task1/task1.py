
import sys

def make_circular_path(n, m):
    massiv = [num for num in range(1, n + 1)]

    cyclic_array = circular_generator(massiv)
    interval = []
    nest_list = []

    while True:
        num = next(cyclic_array)
        nest_list.append(num)
        if len(nest_list) == m:
            interval.append(nest_list.copy())
            if massiv[0] == nest_list[-1]:
                break
            else:
                nest_list = nest_list[-1:]

    path = [str(data[0]) for data in interval]
    return path


def circular_generator(massiv):
    """
    Бесконечный генератор
    """
    while True:
        for i in range(1, len(massiv) + 1):
            yield i


"""
Никогда с подобными постановками задачи не сталкивался. 
Я не понимаю, как точно Вы собираетесь передавать аргумент, потому делаю два варианта. Через терминал строкой с
относительными путями, или интерактивно, с полными путями (у меня тут пути для себя сохранены, гонять тесты)
"""
# Получаем числа N и M из аргументов командной строки: python task1\task1.py 5 4
if len(sys.argv) == 3:  # Если переданы аргументы командной строки
    path = make_circular_path(int(sys.argv[1]), int(sys.argv[2]))
else:  # Если аргументы не переданы, запрашиваем их у пользователя
    data = input("Введите через пробел количество элементов и интервал длинны кругового массива: ").split()
    n, m = int(data[0]), int(data[1])
    path = make_circular_path(n, m)

print("".join(path))


