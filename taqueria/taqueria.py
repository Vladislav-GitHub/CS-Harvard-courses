d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

val = 0
while True:
    try:
        item = input('Item: ').strip().title()
    except (EOFError, KeyError):
        print('\n')
        break
    else:
        if item in d:
            val += d.get(item)
            print('Total: ${:.2f}'.format(val))