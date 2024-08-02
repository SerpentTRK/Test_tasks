

import os
import sys
import json






values_data = [{'id': 2, 'value': 'passed'}, {'id': 41, 'value': 'passed'}, {'id': 73, 'value': 'passed'},
          {'id': 110, 'value': 'failed'}, {'id': 122, 'value': 'failed'}, {'id': 234, 'value': 'passed'},
          {'id': 238, 'value': 'passed'}, {'id': 345, 'value': 'passed'}, {'id': 653, 'value': 'passed'},
          {'id': 690, 'value': 'failed'}, {'id': 5321, 'value': 'passed'}, {'id': 5322, 'value': 'failed'}]

tests_data = [{'id': 2, 'title': 'Smoke test', 'value': ''},
        {'id': 41, 'title': 'Debug test', 'value': ''},
        {'id': 73, 'title': 'Performance test', 'value': '',
          'values': [{'id': 345, 'title': 'Maxperf', 'value': '',
              'values': [{'id': 230, 'title': 'Percent',
                  'values': [{'id': 234, 'title': '200', 'value': ''},
                             {'id': 653, 'title': '300', 'value': ''}]}]},
                      {'id': 110, 'title': 'Stability test', 'value': '',
                          'values': [{'id': 261, 'title': 'Percent',
                          'values': [{'id': 238, 'title': '160', 'value': ''},
                                     {'id': 690, 'title': '240', 'value': ''}]}]}]},
        {'id': 122, 'title': 'Security test', 'value': '',
          'values': [{'id': 5321, 'title': 'Confidentiality', 'value': ''},
                     {'id': 5322, 'title': 'Integrity', 'value': ''}]}]

# stack = [tests_data]
# print(len(stack))
#
# current_item = stack.pop()
# print(current_item)


# for test_item in tests_data:
#     print(test_item)


# def update_values(tests_data, values_data):
#     stack = [tests_data]
#
#     while stack:
#         current_item = stack.pop()
#
#         for test_item in current_item:
#             for value_item in values_data:
#                 if test_item['id'] == value_item['id']:
#                     test_item['value'] = value_item['value']
#                     break
#             if 'values' in test_item:
#                 stack.append(test_item['values'])
#
# # Вызов функции для обновления значений
# update_values(tests_data, values_data)
#
# # Вывод обновленных данных
# print(json.dumps(tests_data, indent=4))



def calculate_min_steps(nums):
    arithmetic_mean = sum(nums) // len(nums)  # среднее арифметическое ЦЕЛОЕ число

    steps = 0
    for num in nums:
        steps += abs(num - arithmetic_mean)
    return steps

nums = [1, 10, 2, 9]
print(calculate_min_steps(nums))


