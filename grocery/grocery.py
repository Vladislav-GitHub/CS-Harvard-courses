d = {}

while True:
    try:
        key = input().strip().upper()
    except (EOFError, KeyError):
        break
    else:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
[print(f'{val} {key}') for key, val in sorted(d.items())]