f = open('input', 'r')
rows = f.read().split('\n')
f.close()
out = open("input", 'w')
text = ''

for row in rows:
    print(row)
    if row == '100':
        if text == '':
            text = '\n'
        else:
            text += '\n'
    else:
        if text == '':
            text = row
        else:
            text += '\n' + row

out.write(text)
out.close()