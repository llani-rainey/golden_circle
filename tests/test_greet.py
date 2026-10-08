#tests/test_greet.py

from lib.greet import *

def test_greet():
    result = greet("Llani")
    assert result == "Hello, Llani!"
    
def test_greet_works_with_a_different_name():
    result = greet("Bob")
    assert result == "Hello, Bob!"