import inflect

p = inflect.engine()

''' Implementation of a program that prompts the user for names, one per line, until the user inputs control-d.
The user will input at least one name. Then bid adieu to those names, separating two names with one and,
three names with two commas and one and, and names with commas and one and '''

names = []

while True:
    try:
        name = input('Name: ')
        names.append(name)
    except (EOFError, KeyError):
        print()
        break

output = p.join(names)
print("Adieu, adieu, to " + output)