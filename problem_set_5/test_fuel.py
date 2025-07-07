from fuel import convert, gauge
import pytest

""" Test convert """

# Test a whole number
def test_convert_1():
    assert convert('1/1') == 100

# Test x is not a number
def test_x():
    with pytest.raises(ValueError):
        convert('x/1')

# Test y is not a number
def test_y():
    with pytest.raises(ValueError):
        convert('1/y')

# Test 2 '//' provided
def test_slash_slash():
    with pytest.raises(ValueError, match = 'Error: Not a fraction'):
        convert ('1//2')

# Test neither are numbers
def test_xy():
    with pytest.raises(ValueError):
        convert('x/y')

# Test zero division error
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')


""" Test Gauge """
def test_gauge_e():
    assert gauge(1) == 'E'

def test_gauge_f():
    assert gauge(100) == 'F'

def test_gauge_randome():
    assert gauge(25) == '25%'
