# File: tests/test_report_length.py


from lib.report_length import *  

# Normal case
def test_reports_length_of_single_word():
    result = report_length("hello")
    assert result == "This string was 5 characters long."

# Edge case: empty string, the smallest possible input
def test_reports_zero_for_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

# Spaces and punctuation count as characters
def test_counts_spaces_and_punctuation():
    result = report_length("Hi there!")
    assert result == "This string was 9 characters long."

# Edge case: single character (exposes "1 characters" grammar quirk)
def test_reports_length_of_single_character():
    result = report_length("a")
    assert result == "This string was 1 characters long."