from calculator import square

# Define main. The sole function of main is to test test_square

# Introduction to assert
"""
def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print('2 squared is not 4')
    try:
        assert square(3) == 9
    except AssertionError:
        print('3 squared is not 9')
    try:
        assert square(-2) == 4
    except AssertionError:
        print('-2 squared is not 4')
    try:
        assert square(-3) == 9
    except AssertionError:
        print('-3 squared is not 9')
    try:
        assert square(0) == 0
    except AssertionError:
        print('0 squared is not 0')


if __name__ == '__main__':
    main()
"""

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0