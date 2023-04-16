from cs50 import get_float


# promp user dor valid data
def get_pos_float():
    while True:
        dollars = get_float("Change owed: ")
        if(dollars >= 0.0):
            break
    return dollars


# initial data
cent = round(100 * get_pos_float())
total = 0

# conditions and calculations
while cent >= 25:
    cent -= 25
    total += 1

while cent >= 10:
    cent -= 10
    total += 1

while cent >= 5:
    cent -= 5
    total += 1

while cent >= 1:
    cent -= 1
    total += 1

# print total cash
print(total)