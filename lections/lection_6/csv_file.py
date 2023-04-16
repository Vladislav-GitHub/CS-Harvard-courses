import csv # import library that helps us work with comma-separated values (CSV) files
from cs50 import get_string

file = open("phonebook.csv", "a") # open the file for appending

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file) # call "csv.writer" to create a "writer" object from the file
writer.writerow([name, number]) # use a method "writer.writerow" to write a list as a row

file.close()

with open("phonebook.csv", "a") as file: # use the with keyword, which will close the file for us after we’re finished
    writer = csv.writer(file)
    writer.writerow((name, number))