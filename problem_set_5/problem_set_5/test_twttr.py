from twttr import shorten

def test_all_vowels():
    assert shorten('AEIOU') == ""

def test_one_vowel():
    assert shorten('hi') == 'h'

def test_no_vowels():
    assert shorten('msn') == 'msn'

def test_with_numbers():
    assert shorten('hello123') == 'hll123'