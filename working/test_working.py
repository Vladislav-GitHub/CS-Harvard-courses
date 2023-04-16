import pytest
from working import convert


def main():
    test_wrong_check()
    test_wrong_hour()
    test_wrong_minute()
    test_wrong_time()


def test_wrong_check():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert('13 AM to 17 PM')


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')


def test_wrong_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'


if __name__ == "__main__":
    main()