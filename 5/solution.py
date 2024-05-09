
def main(first, second, third):
    try:
        result = first / second + third
        out = open("output", 'w')
        out.write(str(result))
        out.close()
    except ZeroDivisionError:
        print('division by 0')


f = open('input', 'r')
rows = f.read().split('\n')
text = ''

try:
    first, second, third = map(int, (rows[0], rows[1], rows[2]))
    main(first, second, third)
    f.close()
except ValueError:
    print('data error')
