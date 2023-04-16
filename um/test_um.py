import pytest
from um import count

def main():
    test_upper_and_lower_cases()
    test_word_with_um()
    test_space()


def test_upper_and_lower_cases():
    assert count('UM, I know this, um.') == 2
    assert count('Um, thanks for the present!') == 1


def test_word_with_um():
    assert count('yummi') == 0


def test_space():
    assert count('I have some  um  vegetables.') == 1
    assert count('um?') == 1

if __name__ == '__main__':
    main()