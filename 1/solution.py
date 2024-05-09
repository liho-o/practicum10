"""
Напишите программу solution.py, которая считывает данные из файла input.txt и
записывает результат в файл output.txt для решения следующей задачи:

Входные данные преобразовать к верхнему регистру.
"""

# для Mac
# with open("input", "r") as f_in:
#     with open("output", "w") as f_out:
#         for line in f_in:
#             f_out.write(line.upper())


# with open("input.txt", "r") as f_in:
#     with open("output.txt", "w") as f_out:
#         for line in f_in:
#             f_out.write(line.upper())

f = open('input', 'r')
out = open("output", 'w')

out.write(f.read().upper())
f.close()
out.close()
