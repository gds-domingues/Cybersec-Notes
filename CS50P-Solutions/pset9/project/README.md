    # Encryption and Decryption Text 
    #### Video Demo:  <https://www.youtube.com/watch?v=EISF5IKysJU&ab_channel=GabrielD>
    #### Description:

Import Statements:

These are import statements bringing in necessary modules and libraries for the code. Key libraries include cryptography for cryptographic operations and Fernet for symmetric encryption.

Global Variables:

PRIVATE_KEY_FILE = "private_key.txt"
ENCRYPTED_FILE = "encrypted_message.txt"
These are global variables defining file names for saving the private key and encrypted text.

RSA Key Pair Generation:
generate_rsa_key_pair():
This function generates an RSA key pair (private and public keys) and returns them as bytes in PEM format.

RSA Encryption:
rsa_encrypt(text, public_key_bytes):
This function takes a plaintext text and a public key in bytes, encrypts the text using RSA-OAEP encryption, and returns the encrypted text.

RSA Decryption:
rsa_decrypt(encrypted_text, private_key_bytes):
This function takes encrypted text and a private key in bytes, decrypts the text using RSA-OAEP decryption, and returns the decrypted text as a string.

SHA-256 Encryption:
sha256_encrypt(text):
This function takes a plaintext text, computes its SHA-256 hash, and returns the hash as a hexadecimal string.

Caesar Cipher Encryption:
def caesar_encrypt(text, shift):
This function performs Caesar cipher encryption on a plaintext text with a specified shift value.

Caesar Cipher Decryption:
caesar_decrypt():
This function decrypts Caesar cipher encrypted text by applying a negative shift.

Fernet Symmetric Encryption:
encrypt_with_private_key():
This function encrypts a plaintext text using Fernet symmetric encryption with a private key. It returns the encrypted text.

Fernet Symmetric Decryption:
decrypt_with_private_key():
This function decrypts Fernet symmetric encrypted text using a private key and returns the decrypted text.

RSA Decryption Wrapper:
decrypt_with_rsa_private_key(encrypted_text, private_key):
This is a wrapper function for decrypting RSA encrypted text, assuming there's an RSA decryption function.

Save Private Key to File:
save_private_key_to_file():
This function saves a private key to a file.

Load Private Key from File:
load_private_key_from_file():
This function loads a private key from a file and prints its content.

Save Encrypted Text to File:
This function saves encrypted text to a file.

Main Function:
The main function is the entry point of the script, providing an interactive menu for the user to choose encryption or decryption methods. The chosen method is then executed.

This code essentially provides a command-line interface for various encryption and decryption methods, including Caesar cipher, SHA-256 hash, Fernet symmetric encryption, and RSA encryption. It also includes functionality to save and load keys and encrypted text to and from files.

Print Menu:

python
Copy code
print('1 - CAESAR ENCRYPTION\n'
    '2 - CAESAR DECRYPTION\n'
    '3 - SHA ENCRYPTION\n'
    '4 - SHA DECRYPTION\n'
    '5 - AES ENCRYPTION\n'
    '6 - AES DECRYPTION\n'
    '7 - RSA ENCRYPTION\n'
    '8 - RSA DECRYPTION\n')
This prints the menu of available encryption and decryption methods.

User Input:

python
Copy code
encryption_method = input('Enter an encryption method: ')
This line takes user input for choosing an encryption or decryption method.

Menu Options:
The code uses a series of if and elif statements to check the user's input and execute the corresponding encryption or decryption method based on the chosen option.

Handling Each Option:

Option 1 (Caesar Encryption):

Takes input text and rotation shift value.
Calls caesar_encrypt function.
Prints original and encrypted text.

Option 2 (Caesar Decryption):

Takes input encrypted text and rotation shift value.
Calls caesar_decrypt function.
Prints original and decrypted text.

Option 3 (SHA-256 Encryption):

Takes input text.
Calls sha256_encrypt function.
Prints original and encrypted text.

Option 4 (SHA-256 Decryption):

Prints that SHA-256 decryption is not possible as it's a one-way hash function.

Option 5 (Fernet AES Encryption):

Generates a Fernet private key.
Takes input text.
Calls encrypt_with_private_key function.
Prints private key, original, and encrypted text.

Option 6 (Fernet AES Decryption):

Takes input encrypted text and private key.
Calls decrypt_with_private_key function.
Prints decrypted text.

Option 7 (RSA Encryption):

Generates RSA key pair.
Takes input text.
Calls rsa_encrypt function.
Prints public key, private key (to be kept safe), and encrypted text.
Saves private key and encrypted text to files.

Option 8 (RSA Decryption):

Checks if the private key file exists.
Loads private key.
Takes input path to the file containing encrypted text.
Reads encrypted text from the file.
Calls decrypt_with_rsa_private_key function.
Prints decrypted text.
Exception Handling:
The try block handles potential exceptions like ValueError and other unexpected errors. If an exception occurs, it prints an error message and exits the program.

This menu-driven approach allows the user to interactively choose different encryption and decryption methods based on their preferences.








