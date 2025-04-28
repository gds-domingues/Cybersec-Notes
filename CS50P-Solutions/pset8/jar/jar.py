class Jar:
    # Constructor method to initialize the cookie jar with a specified capacity (default is 12)
    def __init__(self, capacity=12):
        # Check if the given capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        
        # Set the capacity and initialize the number of cookies in the jar to 0
        self._capacity = capacity
        self._cookies = 0

    # String representation of the Jar, using emoji to represent the cookies
    def __str__(self):
        return "🍪" * self._cookies

    # Method to deposit a specified number of cookies into the jar
    def deposit(self, n):
        # Check if the given number of cookies to deposit is a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer")
        
        # Check if depositing the specified number of cookies exceeds the jar's capacity
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds the cookie jar's capacity")
        
        # Update the number of cookies in the jar
        self._cookies += n

    # Method to withdraw a specified number of cookies from the jar
    def withdraw(self, n):
        # Check if the given number of cookies to withdraw is a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer")
        
        # Check if withdrawing the specified number of cookies exceeds the current number of cookies
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar")
        
        # Update the number of cookies in the jar after withdrawal
        self._cookies -= n

    # Property to get the capacity of the cookie jar
    @property
    def capacity(self):
        return self._capacity

    # Property to get the current number of cookies in the jar
    @property
    def size(self):
        return self._cookies

"""
The code defines a Jar class representing a cookie jar. 
The class has a constructor method that initializes the jar with a specified capacity (default is 12), 
and it includes input validation to ensure that the capacity is a non-negative integer. 
The class has methods for depositing and withdrawing a specified number of cookies, each with corresponding input validations. 
It also provides a string representation using emoji to visualize the number of cookies in the jar. 
Two properties, capacity and size, are defined to access the jar's capacity and the current number of cookies, respectively. 
The code emphasizes proper encapsulation and validation to maintain the integrity of the jar's state.
"""