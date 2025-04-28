# Import the necessary module and function for testing
from twttr import shorten

# Test cases for the shorten function
def test_shorten():
    # Check the removal of vowels from a word
    assert shorten("testing") == "tstng"
    
    # Check the removal of vowels from a sentence
    assert shorten("this is my tweet!") == "ths s my twt!"
    
    # Check the removal of vowels from uppercase letters
    assert shorten("UPPERCASE") == "PPRCS"
    
    # Check a word with numbers and special characters
    assert shorten("s0meth1ng") == "s0mth1ng"

"""
 This code tests the shorten function from the twttr module with various input cases. 
 The assertions cover different scenarios to ensure that the function behaves as expected.
"""