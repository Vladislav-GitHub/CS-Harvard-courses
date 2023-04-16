from numb3rs import validate


def main():
    test_validate()
    test_range()


def test_validate():
    assert validate(r'1.3.255.4') == True
    assert validate(r'2.212.3') == False
    assert validate(r'1.2.3') == False
    assert validate(r'1') == False


def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'500.255.255.255') == False
    assert validate(r'255.255.500.255') == False
    assert validate(r'255.255.255.500') == False
    assert validate(r'255.500.255.255') == False


if __name__ == "__main__":
    main()