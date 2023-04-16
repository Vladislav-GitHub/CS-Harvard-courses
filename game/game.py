import random

while True:
    try:

        # Prompt user for the level
        n = int(input('Level: '))

        # Check for non-positive values
        if n <= 0:
            continue

        # Prompt user for guess
        guess = int(input('Guess: '))

        # Check for non-positive values
        if guess <= 0:
            continue
    except ValueError:
        continue
    else:

        # Randomly generated integer
        integer = random.randint(1, n)

        if guess < integer:
            print('Too small!')
            continue
        elif guess > integer:
            print('Too large!')
            continue
        elif guess == integer:
            print('Just right!')
            break