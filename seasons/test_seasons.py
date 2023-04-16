from seasons import check_date


def main():
    test_check_date()


def test_check_date():
    assert check_date('1999-12-31') == ("1999", "12", "31")
    assert check_date('1996-5-16') == None
    assert check_date('January 1, 1999') == None


if __name__ == '__main__':
    main()