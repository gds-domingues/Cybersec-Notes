# Import necessary modules for encryption and decryption
import sys
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import base64
import hashlib

# Constants for file names
PRIVATE_KEY_FILE = "private_key.txt"
ENCRYPTED_FILE = "encrypted_message.txt"

def generate_rsa_key_pair():
    """
    Generate an RSA key pair.

    Returns:
        Tuple of private key bytes and public key bytes
    """
    # Generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Get the public key
    public_key = private_key.public_key()

    # Serialize the keys
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes

def rsa_encrypt(text, public_key_bytes):
    """
    Encrypt text using RSA public key.

    Args:
        text (str): Text to encrypt.
        public_key_bytes (bytes): RSA public key bytes.

    Returns:
        bytes: Encrypted text.
    """
    # Load the public key
    public_key = serialization.load_pem_public_key(public_key_bytes)

    # Encrypt the text
    encrypted_text = public_key.encrypt(
        text.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_text

def rsa_decrypt(encrypted_text, private_key_bytes):
    """
    Decrypt RSA encrypted text.

    Args:
        encrypted_text (bytes): Encrypted text.
        private_key_bytes (bytes): RSA private key bytes.

    Returns:
        str: Decrypted text.
    """
    # Load the private key
    private_key = serialization.load_pem_private_key(
        private_key_bytes,
        password=None
    )

    # Decrypt the text
    decrypted_text = private_key.decrypt(
        encrypted_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted_text.decode('utf-8')

def sha256_encrypt(text):
    """
    Encrypt text using SHA-256 hash.

    Args:
        text (str): Text to encrypt.

    Returns:
        str: Encrypted text (SHA-256 hash).
    """
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    encrypted_text = sha256.hexdigest()
    return encrypted_text

def caesar_encrypt(text, shift):
    """
    Encrypt text using Caesar cipher.

    Args:
        text (str): Text to encrypt.
        shift (int): Shift value for the cipher.

    Returns:
        str: Encrypted text (Caesar cipher).
    """
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Shift only alphabetical characters
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    """
    Decrypt Caesar cipher encrypted text.

    Args:
        encrypted_text (str): Encrypted text (Caesar cipher).
        shift (int): Shift value for decryption.

    Returns:
        str: Decrypted text.
    """
    # To decrypt, use a negative shift
    return caesar_encrypt(encrypted_text, -shift)

def encrypt_with_private_key(text, private_key):
    """
    Encrypt text using Fernet symmetric encryption.

    Args:
        text (str): Text to encrypt.
        private_key (bytes/str): Fernet private key.

    Returns:
        bytes: Encrypted text.
    """
    # Ensure the private key is properly formatted
    if isinstance(private_key, str):
        private_key = private_key.encode('utf-8')

    # Ensure the private key is 32 bytes long
    if len(private_key) != 32:
        raise ValueError("Fernet key must be 32 bytes.")

    cipher = Fernet(base64.urlsafe_b64encode(private_key))
    encrypted_text = cipher.encrypt(text.encode('utf-8'))
    return encrypted_text

def decrypt_with_private_key(encrypted_text, private_key):
    """
    Decrypt Fernet symmetric encrypted text.

    Args:
        encrypted_text (bytes): Encrypted text.
        private_key (bytes/str): Fernet private key.

    Returns:
        str: Decrypted text.
    """
    # Ensure the private key is properly formatted
    if isinstance(private_key, str):
        private_key = private_key.encode('utf-8')

    # Ensure the private key is 32 bytes long
    if len(private_key) != 32:
        raise ValueError("Fernet key must be 32 bytes.")

    cipher = Fernet(base64.urlsafe_b64encode(private_key))
    decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8')
    return decrypted_text

def decrypt_with_rsa_private_key(encrypted_text, private_key):
    """
    Decrypt RSA encrypted text.

    Args:
        encrypted_text (bytes): Encrypted text.
        private_key (bytes): RSA private key.

    Returns:
        str: Decrypted text.
    """
    # Assuming you have an RSA decryption function in RSA_functions
    decrypted_text = rsa_decrypt(encrypted_text, private_key)
    return decrypted_text

def save_private_key_to_file(private_key):
    """
    Save private key to a file.

    Args:
        private_key (bytes): Private key to be saved.
    """
    with open(PRIVATE_KEY_FILE, "wb") as file:
        file.write(private_key)

def load_private_key_from_file():
    """
    Load private key from a file.

    Returns:
        bytes: Loaded private key.
    """
    try:
        with open(PRIVATE_KEY_FILE, "rb") as file:
            content = file.read()
            print(f"Content of {PRIVATE_KEY_FILE}: {content}")
            return content
    except Exception as e:
        print(f"Error loading private key: {e}")
        raise

def save_encrypted_text_to_file(encrypted_text):
    """
    Save encrypted text to a file.

    Args:
        encrypted_text (bytes): Encrypted text to be saved.
    """
    with open(ENCRYPTED_FILE, "wb") as file:
        file.write(encrypted_text)

def main():
    try:
        # Prompt user for encryption method choice
        print('1 - CAESAR ENCRYPTION\n'
            '2 - CAESAR DECRYPTION\n'
            '3 - SHA ENCRYPTION\n'
            '4 - SHA DECRYPTION\n'
            '5 - AES ENCRYPTION\n'
            '6 - AES DECRYPTION\n'
            '7 - RSA ENCRYPTION\n'
            '8 - RSA DECRYPTION\n')

        encryption_method = input('Enter an encryption method: ')

        # Perform the chosen encryption or decryption method
        if '1' in encryption_method:
            text = input('Enter the Text to Encrypt: ')
            rotation = int(input('Enter the shift value: '))
            encrypted_text = caesar_encrypt(text, rotation)
            print(f"Original Text: {text}")
            print(f"Encrypted Text (CAESAR): {encrypted_text}")

        elif '2' in encryption_method:
            encrypted_text = input('Enter text to decrypt: ')
            rotation = int(input('Enter the shift Value: '))
            decrypted_text = caesar_decrypt(encrypted_text, rotation)
            print(f"Original Text: {encrypted_text}")
            print(f"Decrypted Text (CAESAR): {decrypted_text}")

        elif '3' in encryption_method:
            text_to_encrypt = input('Enter the text to Encrypt')
            encrypted_text_sha256 = sha256_encrypt(text_to_encrypt)
            print(f"Original Text: {text_to_encrypt}")
            print(f"Encrypted Text (SHA-256): {encrypted_text_sha256}")

        elif '4' in encryption_method:
            print("SHA Decryption is not possible as it's a one-way hash function.")

        elif '5' in encryption_method:
            private_key = Fernet.generate_key()
            text_to_encrypt = input('Enter the text to encrypt: ')
            encrypted_text = encrypt_with_private_key(text_to_encrypt, private_key)
            print(f"Private Key (Keep safe): {private_key}")
            print(f"Original Text: {text_to_encrypt}")
            print(f"Encrypted Text: {encrypted_text}")

        elif '6' in encryption_method:
            encrypted_text = input('Enter the text to decrypt: ')
            private_key = input('Enter the private key: ')
            decrypted_text = decrypt_with_private_key(encrypted_text, private_key)
            print(f"Decrypted Text: {decrypted_text}")

        elif '7' in encryption_method:
            private_key, public_key = generate_rsa_key_pair()
            text_to_encrypt = input('Enter the text for encryption: ')
            encrypted_text = rsa_encrypt(text_to_encrypt, public_key)

            print(f"\nPublic Key:\n{public_key}\n")
            print("\nPrivate Key (Safekeeping Required):\n{}".format(private_key.decode('utf-8')))
            print(f"Encrypted Text: {encrypted_text}")

            # Save private key to file
            save_private_key_to_file(private_key)

            # Save encrypted text to file
            save_encrypted_text_to_file(encrypted_text)

        elif '8' in encryption_method:
            # Decryption logic for function 8
            if not os.path.exists(PRIVATE_KEY_FILE):
                print("Private key file not found. Please run option 7 to generate the key.")
                return

            private_key_input = load_private_key_from_file()

            # Instead of input, read from a file
            encrypted_text_file_path = input("Enter the path to the file containing encrypted text: ")
            try:
                with open(encrypted_text_file_path, "rb") as file:
                    encrypted_text_input = file.read()

                decrypted_text = decrypt_with_rsa_private_key(
                    encrypted_text_input,
                    private_key_input
                )

                print(f"Decrypted Text: {decrypted_text}")

            except FileNotFoundError:
                print(f"File not found: {encrypted_text_file_path}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit('Please enter a valid input')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit('Exiting due to an error')

if __name__ == "__main__":
    main()  # Execute the main function if the script is run as the main program

"""
The code imports necessary modules for encryption and decryption, including cryptography and Fernet.
Constants for file names (PRIVATE_KEY_FILE and ENCRYPTED_FILE) are defined.
Functions for various encryption and decryption methods are provided, including RSA, Caesar cipher, SHA-256 hash, and Fernet symmetric encryption.
Functions to save and load private keys and encrypted text to and from files are defined.
The main() function provides a user interface for choosing an encryption or decryption method and executing the corresponding operations.
The script checks for errors during user input and unexpected exceptions, printing informative messages and exiting with an error status if needed.
The script is designed to be executed as the main program, ensuring that the main() function is called when the script is run.
"""