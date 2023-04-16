import sys

def main():
    try:
        if len(sys.argv) < 2:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv) > 2:
            print('Too many command-line arguments ')
            sys.exit(1)
        elif sys.argv[1].split('.')[-1] != 'py':
            print('Not a Python file')
            sys.exit(1)
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            num = 0
            for line in lines:
                if not line.lstrip().startswith('#') and line.strip() != '':
                    num += 1
            print(num)
            file.close()
    except FileNotFoundError:
        print('File does not exist')

if __name__ == '__main__':
    main()