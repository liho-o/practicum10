
f = open('input', 'r')
out = open("output", 'w')


rows = f.read().split('\n')
text = ''

for row in rows:
    text += row[0:1]



out.write(text)
f.close()
out.close()
