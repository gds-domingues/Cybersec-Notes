from um import count  # Import the count function from the um module

def test_count():
    # Test cases to validate the count function
    assert count("no Um! hi um? um. who") == 3
    assert count(", uM, ! mU") == 1
    assert count("wHat, um, yea") == 1
    assert count(" what! Um???") == 1
    assert count("UM who Is tHat") == 1
    assert count("UMM what!") == 0  # No match with "UMM"
    assert count("Hey UM?") == 1
    assert count("WHat U.m?") == 0  # No match with "U.m"
    assert count("WHo Is tHat U m!") == 0  # No match with "U m"

"""
These test cases cover scenarios where the count function is expected to correctly identify and count instances of the word "um" with various punctuation, 
capitalization, and spacing. They provide a comprehensive evaluation of the function's behavior in different contexts.
"""