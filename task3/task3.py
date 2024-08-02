
import os
import sys
import json


def update_values(tests_data, values_data):
    stack = [tests_data]  # т.к. по заданию степень вложенности может быть разная, то кладем все в этот массив

    while stack:
        current_item = stack.pop()  # забираем все, что в stack, очищая его

        for test_item in current_item:
            for value_item in values_data:
                if test_item['id'] == value_item['id']:
                    test_item['value'] = value_item['value']
                    break   # обрываем цикл, если значение заполнено
            if 'values' in test_item:
                stack.append(test_item['values'])  # если было 'values', то его значение забрасываем в stack

def read_and_write_to_json(values_json_file_path, tests_json_file_path, report_json_file_path):
    with open(values_json_file_path, 'r') as file1:
        data_values = json.load(file1)["values"]

    with open(tests_json_file_path, 'r') as file2:
        data_tests = json.load(file2)["tests"]

    update_values(data_tests, data_values)

    with open(report_json_file_path, 'w') as file3:
        json.dump(data_tests, file3, indent=4)


"""
Никогда с подобными постановками задачи не сталкивался. 
Я не понимаю, как точно Вы собираетесь передавать аргумент, потому делаю два варианта. Через терминал строкой с
относительными путями, или интерактивно, с полными путями (у меня тут пути для себя сохранены, гонять тесты)
"""
# python task3/task3.py task3/values.json task3/tests.json task3/report.json
if len(sys.argv) == 4:  # Если переданы аргументы командной строки
    values_json_file_path = sys.argv[1]
    tests_json_file_path = sys.argv[2]
    report_json_file_path = sys.argv[3]
else:  # Если аргументы не переданы, запрашиваем их у пользователя
    values_json_file_path = input("Введите путь к JSON файлу values.json: ")  # F:\PYTHON PROJECTS\Test_tasks\task3\values.json
    tests_json_file_path = input("Введите путь к JSON файлу tests.json: ")  # F:\PYTHON PROJECTS\Test_tasks\task3\tests.json
    report_json_file_path = input("Введите путь к JSON файлу report.json для отчета: ")  # F:\PYTHON PROJECTS\Test_tasks\task3\report.json

read_and_write_to_json(values_json_file_path, tests_json_file_path, report_json_file_path)
