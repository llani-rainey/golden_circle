# File: tests/test_check_codeword.py
#
# WHAT WE'RE TESTING
# check_codeword has three possible outcomes (branches):
#   1. "horse" exactly            -> "Correct! Come in."
#   2. starts with "h" AND ends with "e" -> "Close, but nope."
#   3. anything else              -> "WRONG!"
#
# WHY THESE TESTS
# - Every branch needs at least one test, otherwise part of the
#   function is never checked and could break without us noticing.
# - Edge cases: test the boundaries of each condition, not just the
#   obvious example. For the "close" branch, BOTH conditions must be
#   true, so we test:
#     * both true ("house")             -> close
#     * shortest possible match ("he")  -> close
#     * only the start matches ("horses") -> wrong
#     * only the end matches ("morse")  -> wrong
#   This proves the function uses AND, not OR.
# - Case sensitivity: "HORSE" isn't "horse", so it's wrong. Testing
#   this documents the behaviour so nobody is surprised later.
# - Empty string: codeword[0] doesn't exist for "", so the function
#   crashes with IndexError. pytest.raises lets us test that an error
#   happens. This is a bug the tests revealed.

import pytest
from lib.check_codeword import *

# Branch 1: correct codeword
def test_correct_codeword_lets_you_in():
    assert check_codeword("horse") == "Correct! Come in."

# Branch 2: close (starts with h AND ends with e)
def test_starts_with_h_and_ends_with_e_is_close():
    assert check_codeword("house") == "Close, but nope."

def test_two_letter_he_is_close():
    assert check_codeword("he") == "Close, but nope."

# Branch 3: wrong, including cases where only ONE condition matches
def test_starts_with_h_but_wrong_ending_is_wrong():
    assert check_codeword("horses") == "WRONG!"

def test_ends_with_e_but_wrong_start_is_wrong():
    assert check_codeword("morse") == "WRONG!"

def test_completely_different_word_is_wrong():
    assert check_codeword("dog") == "WRONG!"

def test_is_case_sensitive():
    assert check_codeword("HORSE") == "WRONG!"

# Edge case: empty string crashes the function
def test_empty_string_raises_index_error():
    with pytest.raises(IndexError):
        check_codeword("")