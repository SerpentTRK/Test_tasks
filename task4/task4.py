
import sys



def calculate_min_steps(nums):
    """
    "Минимальное количество ходов для равных элементов массива"
    """
    # сортируем по возрастанию для нахождения медианы (значение в середине упорядоченного набора данных)
    sorted_nums = sorted(nums)
    # получени числа, c помощью которого мы будем высчитывать количество шагов
    mediana = sorted_nums[len(sorted_nums) // 2]

    steps = 0
    for num in nums:
        steps += abs(num - mediana)
    return steps


"""
Никогда с подобными постановками задачи не сталкивался. 
Я не понимаю, как точно Вы собираетесь передавать аргумент, потому делаю два варианта. Через терминал строкой с
относительными путями, или интерактивно, с полными путями (у меня тут пути для себя сохранены, гонять тесты)
"""
# python task4/task4.py task4/numbers.txt
if len(sys.argv) == 2:  # Если переданы аргументы командной строки
    numbers_file_path = sys.argv[1]
else:  # Если аргументы не переданы, запрашиваем их у пользователя
    numbers_file_path = input("Введите путь к файлу numbers.txt: ")  # F:\PYTHON PROJECTS\Test_tasks\task4\numbers.txt

with open(numbers_file_path, 'r') as file:
    nums = [int(num) for num in file.read().split()]
    print(calculate_min_steps(nums))

