from random import randint


def main():
    level = get_level()
    # Get the score
    score = simulate_game(level)
    print('Score: ', score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    # Depending on the level, get a different random integer
    if level == 1:
        # Generate random values for the equation
        X = randint(0, 9)
        Y = randint(0, 9)
    elif level == 2:
        X = randint(10, 99)
        Y = randint(10, 99)
    else:
        X = randint(100, 999)
        Y = randint(100, 999)
    return X, Y


def simulate_round(x, y):
    count = 1 # count tries
    while count <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count += 1
                print("EEE")
        except:
            count += 1
            print('EEE')
    print(f"{x} + {y} = {x + y}")
    return False


def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()