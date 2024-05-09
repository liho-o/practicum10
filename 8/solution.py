from random import randint

days = []
for _ in range(365):
    days.append(str(randint(5000, 20000)))

with open('input', 'w', encoding='UTF-8') as file_w:
    for day in days:
        file_w.write(day + '\n')

#############


with open('input', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_data = []
prev_month = 0

for curr_month in days:
    temp = content[prev_month:curr_month + prev_month]
    months_data.append(temp)
    prev_month += curr_month

print(months_data)

result = []
for data in months_data:
    total_sum = 0
    for line in data:
        line = int(line)
        total_sum += line
    res = round((total_sum / len(data)))
    result.append(str(res) + '\n')


with open('output', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(result)

print(result)
