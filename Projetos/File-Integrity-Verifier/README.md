# File Integrity Checker

This project is a simple Python-based File Integrity Checker. It computes and stores the hash values of files, allowing you to verify their integrity later by checking for any changes in the hash values. The project uses cryptographic hash functions to ensure that the files have not been altered or corrupted.

## Features

- **Hash Computation**: Uses cryptographic hash functions (e.g., SHA-256) to compute the hash of files.
- **Storage of Hash Values**: Stores file paths and their corresponding hash values in a file.
- **Integrity Verification**: Compares the current hash of files with the stored hash to detect changes.
- **Recursive Directory Scanning**: Scans directories recursively to generate and verify hashes for all files.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/file-integrity-checker.git
   cd file-integrity-checker
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install any dependencies (if needed):

   ```bash
   pip install -r requirements.txt
   ```

   *Note: This project does not have any external dependencies by default.*

## Usage

### 1. Generate Hashes

To generate and store hashes for all files in a directory:

   ```python
   directory = '/path/to/your/directory'
   hash_file = 'file_hashes.txt'

   generate_hashes(directory, hash_file)
   ```

This will compute the hash of every file in the specified directory and store the results in `file_hashes.txt`.

### 2. Verify Integrity

To verify the integrity of the files:

   ```python
   verify_integrity(hash_file)
   ```

This will compare the current hash of each file with the stored hash and notify you if any files have changed or are missing.

### 3. Customizing the Hash Algorithm

You can specify a different hash algorithm (e.g., `md5`, `sha1`) when generating or verifying hashes:

   ```python
   generate_hashes(directory, hash_file, algorithm='md5')
   verify_integrity(hash_file, algorithm='md5')
   ```

## Example

Here’s how to use the File Integrity Checker in a Python script:

   ```python
   from file_integrity_checker import generate_hashes, verify_integrity

   # Directory to scan for files and generate hashes
   directory = '/path/to/your/directory'

   # File to store the generated hashes
   hash_file = 'file_hashes.txt'

   # Generate and store hashes for all files in the specified directory
   generate_hashes(directory, hash_file)

   # Verify the integrity of the files by comparing their current hashes to the stored hashes
   verify_integrity(hash_file)
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with any improvements or bug fixes.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at (gabriel.domingues.silva@usp.br).
