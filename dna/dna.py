import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    STRs = []  # short tandem repeats
    names = []

    # TODO: Read database file into a variable
    with open(sys.argv[1], mode='r') as data:
        reader_data = csv.DictReader(data)
        STRs = reader_data.fieldnames[1:]
        for row in reader_data:
            names.append(row)

    sequence_str_count = dict.fromkeys(STRs, 0)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], mode="r") as sequence_file:
        # Grab first line of txt file
        sequence = sequence_file.readline()
        # Loop over every STR from the database
        for STR in STRs:
            # Update the Sequence STR dictionary with max amount of repeats
            sequence_str_count[STR] = find_repeats(sequence, STR)

    # TODO: Find longest match of each STR in DNA sequence
    for name in names:
        match_count = 0
        for STR in STRs:
            if int(name[STR]) != sequence_str_count[STR]:
                continue
            match_count += 1

        if match_count == len(STRs):
            print(name['name'])
            exit(0)

    print("No match")
    exit(1)

    # TODO: Check database for matching profiles


def find_repeats(sequence, STR):
    # Number of bases in Short Tandem Repeat
    L = len(STR)
    max_repeats = 0
    for i in range(len(sequence)):
        repeats = 0

        if sequence[i: i + L] == STR:
            repeats += 1
            while sequence[i: i + L] == sequence[i + L: i + (2 * L)]:
                repeats += 1
                i += L

        if repeats > max_repeats:
            max_repeats = repeats

    return max_repeats


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
