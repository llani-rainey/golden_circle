# File: tests/test_gratitudes.py
#
# Same approach as StringBuilder:
#   1. Starting state  2. One action  3. Many actions
#   4. Edge cases      5. Isolation
#
# add() is a COMMAND (returns None), so we check its effect
# through format(), which is the QUERY.

import pytest
from lib.gratitudes import Gratitudes


# ---------- 1. Starting state ----------

def test_format_with_no_gratitudes_returns_just_the_prefix():
    # Nothing added, so join() of an empty list gives "".
    # Note the trailing space after the colon: it's in the code, so it's in the result.
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "


# ---------- 2. One action ----------

def test_format_with_one_gratitude():
    # One item: no comma should appear.
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    assert gratitudes.format() == "Be grateful for: coffee"


# ---------- 3. Many actions ----------

def test_format_with_multiple_gratitudes_joins_with_comma_and_space():
    # Checks the separator is ", " and that the order added is kept.
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    gratitudes.add("sunshine")
    gratitudes.add("friends")
    assert gratitudes.format() == "Be grateful for: coffee, sunshine, friends"


def test_format_does_not_clear_gratitudes():
    # format() is a query: calling it twice should give the same result.
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    gratitudes.format()
    assert gratitudes.format() == "Be grateful for: coffee"


def test_can_add_more_after_formatting():
    # Formatting part-way through shouldn't stop new items being added.
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    gratitudes.format()
    gratitudes.add("sunshine")
    assert gratitudes.format() == "Be grateful for: coffee, sunshine"


# ---------- 4. Edge cases ----------

def test_duplicate_gratitudes_are_kept():
    # It's a list, not a set, so duplicates should appear twice.
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    gratitudes.add("coffee")
    assert gratitudes.format() == "Be grateful for: coffee, coffee"


def test_adding_non_string_raises_type_error_when_formatting():
    # Interesting one: add(5) does NOT fail, because a list can hold anything.
    # The error only appears later, in format(), when ", ".join() hits the int.
    # That's why the pytest.raises block wraps format(), not add().
    gratitudes = Gratitudes()
    gratitudes.add(5)
    with pytest.raises(TypeError):
        gratitudes.format()


# ---------- 5. Isolation ----------

def test_two_gratitudes_objects_are_independent():
    # self.gratitudes = [] is set in __init__, so each object gets its own list.
    # If it were a class attribute, both would share one list.
    first = Gratitudes()
    second = Gratitudes()
    first.add("coffee")
    second.add("tea")
    assert first.format() == "Be grateful for: coffee"
    assert second.format() == "Be grateful for: tea"