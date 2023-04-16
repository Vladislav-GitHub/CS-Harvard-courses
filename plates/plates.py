def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for c in s:
        if c in ["!",".","?",' ']:
            return False
    if s[len(s)//2].isnumeric() and s[-1].isalpha():
        return False
    elif len(s) >= 2 and len(s) <= 6 and s[:2].isalpha() and s[:int(len(s)//2)].isalpha() and s[len(s)//2] != '0':
        return True
    else:
        return False

main()