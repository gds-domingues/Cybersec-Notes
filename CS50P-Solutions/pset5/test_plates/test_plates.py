# Import the necessary module and function for testing
from plates import is_valid

# Test cases for the is_valid function
def test_is_valid():
    # Check valid license plate ("CS50")
    assert is_valid("CS50")
    
    # Check invalid license plates
    assert not is_valid("H")        # Invalid length
    assert not is_valid("AI2.14")   # Invalid characters
    assert not is_valid("thistoolong")  # Invalid length
    assert not is_valid("AAA22A")   # Invalid characters
    assert not is_valid("CS05")     # Invalid length
    assert not is_valid("57EED")    # Invalid characters
    assert not is_valid("32")       # Invalid length

"""
it tests the is_valid function from the plates module with various input cases. 
The assertions cover different scenarios to ensure that the function behaves as expected. 
"""