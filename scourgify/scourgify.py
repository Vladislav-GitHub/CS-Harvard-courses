import sys, csv

def main():
    # Check command-line arguments
    check_command_line_args()
    output = []
    # Try to open the file
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: # input
                name_list = row['name'].split(',')
                output.append({'first': name_list[1].lstrip(), 'last': name_list[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    # Write new csv file
    with open(sys.argv[2], 'w') as csvfile_2:
        writer = csv.DictWriter(csvfile_2, fieldnames=['first', 'last', 'house'])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})


def check_command_line_args():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments ')
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit('Not a CSV file')


if __name__ == '__main__':
    main()