def main():
    # prompt user for input
    greeting = input('Greeting: ')
    print(f'${value(greeting)}')

def value(s):
    s = s.strip().lower()
    # check
    if 'hello' in s:
        return 0
    elif s[0] == 'h':
        return 20
    else:
        return 100