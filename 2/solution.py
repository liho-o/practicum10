
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


rows = f.read().split('\n')
text = ''

for row in rows:
    if row[0:1] == 'a' or row[0:1] == 'A':
        if text == '':
            text = row
        else:
            text += '\n' + row


out.write(text)
f.close()
out.close()
