import sys, csv
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) < 2:
            print('Too few command-line arguments')
            sys.exit(1)
        elif len(sys.argv) > 2:
            print('Too many command-line arguments ')
            sys.exit(1)
        elif sys.argv[1].split('.')[-1] != 'csv':
            print('Not a CSV file')
            sys.exit(1)
        table = []
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)

if __name__ == '__main__':
    main()