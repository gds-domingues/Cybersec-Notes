# Password Cracker

This code provides a basic implementation of a password cracker tool in Python. 
It includes functions for brute force attack, dictionary attack, and a main function to orchestrate the cracking process. 
The tool takes the hash value of the password as input, along with optional parameters such as character set, 
maximum password length, and dictionary file for dictionary attack. 
It then attempts to crack the password using various techniques and prints the cracked password if successful.

Explanation:

Let's break down the code into smaller parts and explain each part:

```python
import hashlib
import argparse
```

These lines import the necessary modules: **`hashlib`** for hashing functions and **`argparse`** for parsing command-line arguments.

```python
def brute_force_attack(hash_value, charset, max_length):
    """
    Perform a brute force attack to crack the password.
    """
    # Initialize password variable
    password = ""

    # Iterate through all possible password lengths
    for length in range(1, max_length + 1):
        # Generate all possible combinations of characters with given length
        for combination in itertools.product(charset, repeat=length):
            password_attempt = "".join(combination)
            # Calculate hash of password attempt
            hashed_attempt = hashlib.sha256(password_attempt.encode()).hexdigest()
            # Check if hash matches the target hash
            if hashed_attempt == hash_value:
                return password_attempt
    return None
```

This function **`brute_force_attack`** performs a brute force attack to crack the password. It iterates through all possible password lengths up to a specified maximum length, generates all possible combinations of characters from the given character set, calculates the hash of each combination, and checks if the hash matches the target hash. If a matching hash is found, it returns the corresponding password.

```python
def dictionary_attack(hash_value, dictionary):
    """
    Perform a dictionary attack to crack the password.
    """
    # Iterate through each word in the dictionary
    for word in dictionary:
        # Calculate hash of dictionary word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        # Check if hash matches the target hash
        if hashed_word == hash_value:
            return word
    return None
```

This function **`dictionary_attack`** performs a dictionary attack to crack the password. It iterates through each word in the dictionary, calculates the hash of the word, and checks if the hash matches the target hash. If a matching hash is found, it returns the corresponding word.

```python
def crack_password(hash_value, charset, max_length, dictionary):
    """
    Crack the password using various techniques.
    """
    # Try brute force attack
    password = brute_force_attack(hash_value, charset, max_length)
    if password:
        return password
    # Try dictionary attack
    password = dictionary_attack(hash_value, dictionary)
    if password:
        return password
    return None
```

This function **`crack_password`** orchestrates the password cracking process. It tries a brute force attack first and then falls back to a dictionary attack if the brute force attack fails. It returns the cracked password if successful, otherwise, it returns **`None`**.

```python
if __name__ == "__main__":
```

This line checks if the script is being run as the main program.

```python
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Password Cracker Tool")
    parser.add_argument("hash_value", help="Hash value of the password to be cracked")
    parser.add_argument("-c", "--charset", default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                        help="Character set to use for brute force attack (default: alphanumeric)")
    parser.add_argument("-m", "--max-length", type=int, default=8,
                        help="Maximum length of password for brute force attack (default: 8)")
    parser.add_argument("-d", "--dictionary", type=argparse.FileType("r"),
                        help="Path to dictionary file for dictionary attack")
    args = parser.parse_args()
```

These lines set up a command-line argument parser using **`argparse`**. It defines several arguments: **`hash_value`** for the hash value of the password to be cracked (required), **`charset`** for the character set to use in the brute force attack (defaulting to alphanumeric characters), **`max-length`** for the maximum length of passwords to try in the brute force attack (defaulting to 8), and **`dictionary`** for the path to a dictionary file to use in the dictionary attack.

```python
    # Read dictionary words
    dictionary = set()
    if args.dictionary:
        for line in args.dictionary:
            dictionary.add(line.strip())
```

These lines read the words from the specified dictionary file (if provided) and store them in a set.

```python
# Crack the password
    password = crack_password(args.hash_value, args.charset, args.max_length, dictionary)
    if password:
        print("Password cracked:", password)
    else:
        print("Password not cracked.")
```

This part calls the **`crack_password`** function with the provided arguments (**`hash_value`**, **`charset`**, **`max_length`**, **`dictionary`**). It then prints the cracked password if one is found, or a message indicating that the password could not be cracked.

This part of the code is responsible for parsing command-line arguments, reading dictionary words (if provided), and initiating the password cracking process based on the specified arguments. It leverages the **`argparse`** module for a clean and organized way of handling command-line inputs.
