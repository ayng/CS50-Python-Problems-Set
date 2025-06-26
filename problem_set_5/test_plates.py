from plates import is_valid

def test_abc123():
    assert is_valid('abc123') == True

def test_abcdash34():
    assert is_valid('abc-34') == False

def test_987654():
    assert is_valid('987654') == False

def test_abdash12():
    assert is_valid('ab-12') == False

def test_one_c():
    assert is_valid('c') == False

def test_correct():
    assert is_valid('abC123') == True

def test_question():
    assert is_valid('ABC12?') == False

