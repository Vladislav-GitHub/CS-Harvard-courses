# prompt user for input
s = input('Greeting: ').strip().lower()

# check
if 'hello' in s:
    print('$0')
elif s[0] == 'h':
    print('$20')
else:
    print('$100')