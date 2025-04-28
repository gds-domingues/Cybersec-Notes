# Import the necessary modules and functions for testing
from fuel import convert, gauge
import pytest

# Test cases for the convert function
def test_convert():
    # Check valid conversions
    assert convert('1/4') == 25
    assert convert('100/100') == 100

    # Check for ValueError when providing non-integer values
    with pytest.raises(ValueError):
        convert("three/four")

    # Check for ZeroDivisionError when dividing by zero
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# Test cases for the gauge function
def test_gauge():
    # Check the categorization of percentages
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

"""
In these tests, pytest.raises is used to check if the expected exceptions (ValueError and ZeroDivisionError) are raised for specific inputs. 
The other assertions verify that the functions produce the expected results for valid input.
"""