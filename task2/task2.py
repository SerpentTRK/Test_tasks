import sys
import os
import math

from decimal import Decimal, getcontext
getcontext().prec = 40


# # def read_circle_data(file_path):
# #     with open(file_path, 'r') as file:
# #         data = file.readline().strip().split()
# #         center_x, center_y = int(data[0]), int(data[1])
# #         radius = int(file.readline().strip())
# #     return center_x, center_y, radius
#
#
def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
        if len(data) == 3:
            center_x, center_y = Decimal(data[0]), Decimal(data[1].replace('\\n', ''))
            radius = Decimal(data[2])
        else:
            center_x, center_y = Decimal(data[0]), Decimal(data[1].split('\\')[0])
            radius = Decimal(data[1].split('n')[-1])
    return center_x, center_y, radius


def read_points(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\\n')

        points = []
        for line in data:
            line_list = line.strip().split()
            try:
                x, y = Decimal(line_list[0]), Decimal(line_list[1])
                points.append((x, y))
            except IndexError:
                pass
    return points

def calculate_distance_between_center_and_point(x1, y1, x2, y2):
    """
    формулу расстояния между двумя точками в декартовой системе координат
    """
    # print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), radius)
    # return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return Decimal((x2 - x1) ** 2 + (y2 - y1) ** 2).sqrt()

def point_position(center_x, center_y, radius, x, y):
    distance = calculate_distance_between_center_and_point(center_x, center_y, x, y)
    tolerance = Decimal('1E-40')  # Установите желаемую точность
    if abs(radius-distance) < tolerance:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

"""
Никогда с подобными постановками задачи не сталкивался.
Я не понимаю, как точно Вы собираетесь передавать аргумент, потому делаю два варианта. Через терминал строкой с
относительными путями, или интерактивно, с полными путями (у меня тут пути для себя сохранены, гонять тесты)
"""
# python task2/task2.py task2/circle.txt task2/dot.txt
if len(sys.argv) == 3:  # Если переданы аргументы командной строки
    circle_file_path = sys.argv[1]
    points_file_path = sys.argv[2]
else:  # Если аргументы не переданы, запрашиваем их у пользователя
    circle_file_path = input("Введите путь к файлу circle.txt: ")  # F:\PYTHON PROJECTS\Test_tasks\task2\circle.txt
    points_file_path = input("Введите путь к файлу dot.txt: ")  # F:\PYTHON PROJECTS\Test_tasks\task2\dot.txt


center_x, center_y, radius = read_circle_data(circle_file_path)
points = read_points(points_file_path)

for point in points:
    position = point_position(center_x, center_y, radius, point[0], point[1])
    print(position)



