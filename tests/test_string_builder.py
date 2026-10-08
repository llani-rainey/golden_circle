from lib.string_builder import *
# import pytest (only if need raise error)

# new StringBuilder -> outputs ""
# add str to existing StringBuilder -> outputs str
#  add multiple str -> outputs correctly
# 
# 
# 

# File: tests/test_string_builder.py
#
# HOW THESE TESTS WERE CHOSEN
# ---------------------------
# 1. Starting state  - what does a brand new object look like?
# 2. One action      - does each method work once, on its own?
# 3. Many actions    - does state build up correctly over several calls?
# 4. Edge cases      - empty input, unusual characters, wrong types
# 5. Isolation       - do two objects interfere with each other?
#
# Each test follows Arrange -> Act -> Assert:
#   Arrange: set up the object
#   Act:     call the method(s) you're testing
#   Assert:  check the result is what you expect
#
# Each test checks ONE behaviour, and its name says what that behaviour is,
# so when it fails you know exactly what broke.

import pytest
from lib.string_builder import StringBuilder


# ---------- 1. Starting state ----------

def test_new_builder_outputs_empty_string():
    # Before anything is added, there should be nothing to output.
    builder = StringBuilder()
    assert builder.output() == ""


def test_new_builder_has_size_zero():
    # And its size should be 0. Testing this separately from output()
    # means a bug in one method doesn't hide a bug in the other.
    builder = StringBuilder()
    assert builder.size() == 0


# ---------- 2. One action ----------

def test_add_one_string_then_output_returns_it():
    # Simplest "happy path": add something, get it back.
    builder = StringBuilder()
    builder.add("hello")
    assert builder.output() == "hello"


def test_add_one_string_then_size_is_its_length():
    # "hello" has 5 characters, so size should be 5.
    builder = StringBuilder()
    builder.add("hello")
    assert builder.size() == 5


# ---------- 3. Many actions ----------

def test_add_multiple_strings_joins_them_in_order():
    # The whole point of a builder: strings accumulate, in the order added.
    # Using different words checks the order, not just that both are there.
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" ")
    builder.add("world")
    assert builder.output() == "hello world"


def test_add_multiple_strings_size_is_total_length():
    # 5 + 1 + 5 = 11. Checks size keeps up as more is added.
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" ")
    builder.add("world")
    assert builder.size() == 11


def test_output_does_not_clear_the_builder():
    # Calling output() should only READ the string, not reset it.
    # A sneaky bug would be output() emptying self.str afterwards.
    builder = StringBuilder()
    builder.add("abc")
    builder.output()
    assert builder.output() == "abc"


# ---------- 4. Edge cases ----------

def test_add_empty_string_changes_nothing():
    # Adding "" is valid but should have no effect.
    builder = StringBuilder()
    builder.add("abc")
    builder.add("")
    assert builder.output() == "abc"
    assert builder.size() == 3


def test_spaces_and_symbols_count_towards_size():
    # Every character counts, including spaces and punctuation.
    builder = StringBuilder()
    builder.add("hi there!")
    assert builder.size() == 9


def test_adding_non_string_raises_type_error():
    # Documents current behaviour: str + int isn't allowed in Python,
    # so add(5) raises TypeError. pytest.raises checks an error happens.
    builder = StringBuilder()
    with pytest.raises(TypeError):
        builder.add(5)


# ---------- 5. Isolation ----------

def test_two_builders_are_independent():
    # Each object should have its own string. This catches a classic bug:
    # storing data on the class instead of on self.
    builder_a = StringBuilder()
    builder_b = StringBuilder()
    builder_a.add("apple")
    builder_b.add("banana")
    assert builder_a.output() == "apple"
    assert builder_b.output() == "banana"