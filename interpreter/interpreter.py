x, y, z = input('Expression: ').split(' ') # y - sign

if y == '+':
    print('{:.1f}'.format(float(x) + float(z)))
elif y == '-':
    print('{:.1f}'.format(float(x) - float(z)))
elif y == '*':
    print('{:.1f}'.format(float(x) * float(z)))
elif y == '/':
    print('{:.1f}'.format(float(x) / float(z)))
else:
    print(None)