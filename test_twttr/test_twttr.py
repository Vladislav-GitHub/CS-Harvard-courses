from twttr import shorten

# atop test_twttr.py so that you can call shorten in your tests.
# Take care to return, not print, a str in shorten. Only main should call print.

def main():
    test_upper_and_lower_cases()

# Test cases
def test_upper_and_lower_cases():
    assert shorten('twitter') == 'twttr' # input().strip()
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

# Test numbers
def test_numbers():
    assert shorten('1234') == '1234'

# Test punctuation
def test_punct():
    assert shorten('?!,.') == '?!,.'

if __name__ == "__main__":
    main()