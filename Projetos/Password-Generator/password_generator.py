import random
import string

def generate_password(length=12):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the character set
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage:
password = generate_password(16)  # Generate a 16-character password
print(f"Generated Password: {password}")
