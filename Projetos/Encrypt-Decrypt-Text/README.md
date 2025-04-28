    # Encryption and Decryption Text 
    #### Video Demo:  <https://www.youtube.com/watch?v=EISF5IKysJU&ab_channel=GabrielD>
    #### Description:

This program serves as a comprehensive encryption and decryption tool with eight distinct options. It enables users to encrypt and decrypt text using various methods. Options 1 and 2 implement Caesar cipher encryption and decryption, respectively, requiring user input for text and rotation shift values. Option 3 performs SHA-256 encryption on user-provided text, while Option 4 explains the impossibility of SHA-256 decryption due to its one-way nature. Options 5 and 6 utilize Fernet symmetric encryption, generating a private key and allowing users to encrypt and decrypt text. Options 7 and 8 involve RSA encryption and decryption, generating key pairs, processing user input, and saving encrypted text and private keys to files. Overall, the program provides a user-friendly interface for securing and revealing information through diverse cryptographic techniques.

**Import Statements:**

These statements play a crucial role in incorporating essential modules and libraries into the code. Notable libraries encompass cryptography for cryptographic operations and Fernet for symmetric encryption.

**Global Variables:**

```python
PRIVATE_KEY_FILE = "private_key.txt"
ENCRYPTED_FILE = "encrypted_message.txt"
```

These global variables delineate the file names for storing the private key and encrypted text.

**RSA Key Pair Generation**:

```python
generate_rsa_key_pair()
```

This function generates an RSA key pair (private and public keys) and returns them as bytes in PEM format.

**RSA Encryption:**

```python
rsa_encrypt(text, public_key_bytes)
```

This function takes plaintext text and a public key in bytes, encrypts the text using RSA-OAEP encryption, and returns the encrypted text.

**RSA Decryption:**

```python
rsa_decrypt(encrypted_text, private_key_bytes)
```

This function takes encrypted text and a private key in bytes, decrypts the text using RSA-OAEP decryption, and returns the decrypted text as a string.

**SHA-256 Encryption:**

```python
sha256_encrypt(text)
```

This function takes plaintext text, computes its SHA-256 hash, and returns the hash as a hexadecimal string.

**Caesar Cipher Encryption:**

```python
def caesar_encrypt(text, shift)
```

This function performs Caesar cipher encryption on plaintext text with a specified shift value.

**Caesar Cipher Decryption:**

```python
caesar_decrypt()
```

This function decrypts Caesar cipher encrypted text by applying a negative shift.

**Fernet Symmetric Encryption:**

```python
encrypt_with_private_key()
```

This function encrypts plaintext text using Fernet symmetric encryption with a private key and returns the encrypted text.

**Fernet Symmetric Decryption:**

```python
decrypt_with_private_key()
```

This function decrypts Fernet symmetric encrypted text using a private key and returns the decrypted text.

**RSA Decryption Wrapper:**

```python
decrypt_with_rsa_private_key(encrypted_text, private_key)
```

A wrapper function for decrypting RSA encrypted text, assuming there's an RSA decryption function.

**Save Private Key to File:**

```python
save_private_key_to_file()
```

This function saves a private key to a file.

**Load Private Key from File:**

```python
load_private_key_from_file()
```

This function loads a private key from a file and prints its content.

**Save Encrypted Text to File:**

```python
save_encrypted_text_to_file()
```

This function saves encrypted text to a file.

**Main Function:**

The main function serves as the script's entry point, presenting an interactive menu for the user to choose encryption or decryption methods. The selected method is then executed.

**Print Menu:**

```python
print_menu()
```

This function prints the menu of available encryption and decryption methods.

**User Input:**

```python
encryption_method = input('Enter an encryption method: ')
```

This line captures user input for choosing an encryption or decryption method.

**Menu Options:**

The code employs a series of if and elif statements to check the user's input and execute the corresponding encryption or decryption method based on the chosen option.

**Handling Each Option:**

- **Option 1 (Caesar Encryption):** Takes input text and rotation shift value. Calls caesar_encrypt function. Prints original and encrypted text.
- **Option 2 (Caesar Decryption):** Takes input encrypted text and rotation shift value. Calls caesar_decrypt function. Prints original and decrypted text.
- **Option 3 (SHA-256 Encryption):** Takes input text. Calls sha256_encrypt function. Prints original and encrypted text.
- **Option 4 (SHA-256 Decryption):** Prints that SHA-256 decryption is not possible as it's a one-way hash function.
- **Option 5 (Fernet AES Encryption):** Generates a Fernet private key. Takes input text. Calls encrypt_with_private_key function. Prints private key, original, and encrypted text.
- **Option 6 (Fernet AES Decryption):** Takes input encrypted text and private key. Calls decrypt_with_private_key function. Prints decrypted text.
- **Option 7 (RSA Encryption):** Generates RSA key pair. Takes input text. Calls rsa_encrypt function. Prints public key, private key (to be kept safe), and encrypted text. Saves private key and encrypted text to files.
- **Option 8 (RSA Decryption):** Checks if the private key file exists. Loads private key. Takes input path to the file containing encrypted text. Reads encrypted text from the file. Calls decrypt_with_rsa_private_key function. Prints decrypted text.

**Exception Handling:**

The try block manages potential exceptions like ValueError and other unexpected errors. If an exception occurs, it prints an error message and exits the program.

This menu-driven approach empowers the user to interactively choose different encryption and decryption methods based on their preferences.






