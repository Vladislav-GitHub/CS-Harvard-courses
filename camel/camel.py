name = [s for s in input('camelCase: ').strip()]

a = []
for i, s in enumerate(name):
    if name[i].isupper():
        a.append('_' + name[i].lower())
        continue
    a.append(name[i])
print('snake_case:', ''.join(a))