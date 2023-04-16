import csv

titles = dict()  # or titles = {}

with open("Fav TV Shows.csv", "r") as file:  # read by default, so we can don't write "r"
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title'].strip().upper()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

def f(title):
    return titles[title]

for title in sorted(titles, key=f(), revers=True):  # by default it's sorted by key, but now it's sorted by value due to the function f
    print(title, titles[title])
