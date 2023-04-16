from bank import value

def main():
    test_zero()

def test_zero():
    assert value('Hello') == 0
    assert value('hello man') == 0
    assert value('hello Man') == 0

def test_20():
    assert value('Hi') == 20
    assert value('hey') == 20

def test_100():
    assert value("What's wrong?") == 100
    assert value('good morning') == 100

if __name__ == '__main__':
    main()