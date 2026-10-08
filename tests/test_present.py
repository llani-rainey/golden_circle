# tests/test_present.py

from lib.present import *
import pytest 

# 1) starting state:

def test_unwrap_new_present_raises_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."

# 2) one action:

def test_wrap_then_unwrap_returns_contents():
    present = Present()
    present.wrap("socks")
    result = present.unwrap()
    assert result == "socks"   #what we got vs what we expect

# 3) many action:
def test_unwrap_twice_returns_same_contents():
    present = Present()
    present.wrap("socks")
    present.unwrap()
    assert present.unwrap() == "socks"
    
# 4) paths:

# wrap() has a fork: already wrapped → raise error, otherwise → store contents.
# Wrapping twice is the only way to reach the error branch.
# It takes two actions, but what it's testing is the branch, so it goes under paths.
def test_wrap_twice_raises_error(): 
    present = Present()
    present.wrap("socks")
    with pytest.raises(Exception) as e:
        present.wrap("shoes")
    assert str(e.value) == "A contents has already been wrapped."
    
def test_wrap_twice_keeps_original_contents():
    
    present = Present()
    present.wrap("socks")
    with pytest.raises(Exception): # don't need as e here, because this test doesn't check the message. we just need to catch the error so the test can carry on and check the socks are still there.
        present.wrap("shoes")
    assert present.unwrap() == "socks"

# 5) boundries:

def test_wrap_empty_string_counts_as_wrapped():
    present = Present()
    present.wrap("")
    assert present.unwrap() == ""
    
def test_wrap_none_leaves_present_unwrapped():
    present = Present()
    present.wrap(None)
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."
    
    
# 6) edges cases:




# 7) isolation: 
def test_two_presents_are_indepedent():
    present_A = Present()
    present_A.wrap("socks")
    
    present_B = Present()
    present_B.wrap("shoes")
    
    assert present_a.unwrap() == "socks"
    assert present_b.unwrap() == "shoes"
# 
# 
# 
# 