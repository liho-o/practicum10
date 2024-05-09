f = open('input', 'r')
out = open("output", 'w')


rows = f.read().split('\n')
text = ''

for row in rows:
    if len(row) > 20:
        if text == '':
            text = row
        else:
            text += '\n' + row


out.write(text)
f.close()
out.close()
