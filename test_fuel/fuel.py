def main():
    fraction = input('Fraction: ')
    converted_fraction = convert(fraction)
    output = gauge(converted_fraction)
    print(f'{output}%')

def convert(fraction):
    while True:
        try:
            X, Y = fraction.split('/')
            new_X = int(X)
            new_Y = int(Y)
            f = new_X / new_Y
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
            if percentage <= 1:
                return 'E'
            elif percentage >= 99:
                return 'F'
            else:
                return str(percentage) + '%'

if __name__ == "__main__":
    main()