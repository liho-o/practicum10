f = open('input', 'r')
out = open("output", 'w')

rows = f.read().split('\n')
text = ''

try:
    len_row = int(rows[0])
    if len_row == len(rows) - 1:
        text = "YES"
        out.write(str(text))
        out.close()
    else:
        text = "NO"
        out.write(str(text))
        out.close()
except:
    print('Error')