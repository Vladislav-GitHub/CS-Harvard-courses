from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_2 = Jar(4)
    assert jar_2.capacity == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7



def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    jar.deposit(3)
    jar.withdraw(10)
    assert jar.size == 1