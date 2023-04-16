from cs50 import get_string
from cs50 import get_int
from cs50 import get_float

answer = get_string("What's your name? ") # w/o cs50 library get_string = input
print("Hello, " + answer)
print(f"Hello again, {answer}")
x = int(input("What's x? "))
print(x)

for i in range(3): # or for in range(0, 101, 2), where 2 is the increment and 101 is the interval from 0 to 100
    print("hello world")

for i in [0, 1, 2]:
    print("hi")
    i += i

words = set()
def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.app(line.strip())
        file.close()
        return True # capital T

#def check():
#    if words.lower() in words:
#        return True
#    else:
#        return False

def size():
    return len(words)

def unload():
    return True

def get_positive_int():
    while True: # it's the same condition as do {} while (n < 1)
        n = get_int("Positive integer: ")
        if n > 0:
            break
    return n

people = { # dictionary
    "Carter" : "$200", # key : value
    "Brian" : "$350"
}

name = get_string("Name: ")
if name in people:
    number = people[name] # number = dictionary[value]
    print(f"Number: {number}")