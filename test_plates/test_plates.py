from plates import is_valid

def main():
    test_max_and_min()
    test_two_symbols()
    test_end()
    test_number_zero()
    test_punctuation()

def test_max_and_min():
    # max = 6 symbols, min = 2 symbols
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

def test_two_symbols():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('11') == False

def test_end():
    assert is_valid('AAA111') == True
    assert is_valid('AAA11A') == False

def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

if __name__ == '__main__':
    main()