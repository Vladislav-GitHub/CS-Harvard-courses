while True:
    try:
        X, Y = [int(n) for n in input('Fraction: ').strip().split('/')]
        Fuel_gauge = X / Y * 100
    except (ValueError, ZeroDivisionError):
        continue
    else:
        if X > Y:
            continue
        elif Fuel_gauge < 1:
            print('E')
            break
        elif Fuel_gauge > 99:
            print('F')
            break
        else:
            print(f'{round(Fuel_gauge)}%')
            break