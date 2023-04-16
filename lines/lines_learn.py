import csv, sys
from PIL import Image

def main():
    #name = input("What's your name? ")

    #with open("names.txt") as file:
    #    for line in file:
    #        names.append(line.rstrip())

    #names = []
    #for name in sorted(names):
    #    print(f'Hello, {name}')
        #file.write(f'\n{name}\n')

    #with open('students.csv') as file:
    #    for line in file:
    #        name, house = line.rstrip().split(",")
    #        print(f'{name} is in {house}')

    #students = []
    #with open('students.csv') as file:
    #    for line in file:
    #        name, house = line.rstrip().split(',')
    #        students.append(f'{name} is in {house}')
    #for student in sorted(students):
    #    print(student)
    #with open('students.csv') as file:
    #    for line in file:
    #        name, house = line.rstrip().split(',')
    #        student = {}
    #        student['name'] = name
    #        student['house'] = house
    #        students.append(student)
    #for student in students:
    #    print(f"{student['name']} is in {student['house']}")

    #home = input("Where's your home? ")
    #with open("students2.csv", "a") as file:
    #    writer = csv.writer(file)
    #    writer.writerow([name, home])
    images = []

    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )

if __name__ == '__main__':
    main()