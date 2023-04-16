from cs50 import get_int


def get_pos_height():
    while True:
        height = get_int("Height: ")
        if (height >= 1 and height <= 8):
            break
    return height


h = get_pos_height()

for row in range(h):
    for space in range(h - row - 1, 0, -1):  # range(start, stop[, step])
        print(" ", end="")  # we pass in end="" to specify that nothing should be printed at the end of our string
    for hash in range(row + 1):
        print("#", end="")
    print("\n", end="")