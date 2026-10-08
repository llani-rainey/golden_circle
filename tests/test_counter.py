# tests/test_counter.py

from lib.counter import * #import the functions / class
# import pytest #only need if want to use pytest.raises()


# tests:
# new counter -> report says 0
# add one number - > report says that number 
# add several numbers -> report says the total
# add a negative or zero -> report reflects it
#
#

def test_new_counter_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
    
def test_add_one_number_reports_that_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
    
def test_add_several_numbers_reports_total():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."
    
def test_add_negative_number_reduces_count():
    counter = Counter()
    counter.add(5)
    counter.add(-2)
    assert counter.report() == "Counted to 3 so far."