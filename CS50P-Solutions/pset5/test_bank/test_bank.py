# In test_bank.py

from bank import value

def test_value():
    # Test cases for the value function
    
    # Test when greeting starts with "Hello"
    assert value("Hello") == 0
    
    # Test when greeting starts with "H"
    assert value("How are you doing?") == 20
    
    # Test when greeting doesn't start with either "Hello" or "H"
    assert value("What's happening?") == 100

"""
In test module (test_bank.py), are using the assert statements to check if the value function produces the expected results for different input strings. 
Make sure you have a testing framework, like pytest, installed to run the tests.
"""