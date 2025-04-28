import hashlib
import argparse

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

if __name__ == "__main__":
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

    # Read dictionary words
    dictionary = set()
    if args.dictionary:
        for line in args.dictionary:
            dictionary.add(line.strip())

    # Crack the password
    password = crack_password(args.hash_value, args.charset, args.max_length, dictionary)
    if password:
        print("Password cracked:", password)
    else:
        print("Password not cracked.")
