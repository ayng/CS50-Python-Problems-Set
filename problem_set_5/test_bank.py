from bank import value

def test_hello():
    assert value('hello') == 0

def test_hi():
    assert value('hi') == 20

def test_nothing():
    assert value('') == 100

def test_diff_greeting():
    assert value('yeller!') == 100