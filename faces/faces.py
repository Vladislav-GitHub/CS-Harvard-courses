def main(s = str(input())):
    return convert(s)

def convert(string):
    string = string.replace(':(', '🙁').replace(':)', '🙂')
    return string

print(main())