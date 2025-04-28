import hashlib
import os

def compute_file_hash(file_path, algorithm='sha256'):
    """
    Compute the hash of a file using the specified algorithm.
    
    Parameters:
    - file_path: Path to the file to be hashed.
    - algorithm: Hash algorithm to use (default is SHA-256).
    
    Returns:
    - The hexadecimal hash of the file.
    """
    hash_algo = hashlib.new(algorithm)
    
    # Open the file in binary read mode
    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid memory issues with large files
        while chunk := file.read(8192):
            hash_algo.update(chunk)
    
    # Return the computed hash as a hexadecimal string
    return hash_algo.hexdigest()

def store_hashes(hash_dict, hash_file):
    """
    Store the file paths and their corresponding hashes in a file.
    
    Parameters:
    - hash_dict: Dictionary containing file paths as keys and their hashes as values.
    - hash_file: Path to the file where the hashes will be stored.
    """
    # Open the hash file in write mode
    with open(hash_file, 'w') as f:
        # Write each file path and its hash to the file
        for file_path, file_hash in hash_dict.items():
            f.write(f'{file_path}:{file_hash}\n')

def generate_hashes(directory, hash_file, algorithm='sha256'):
    """
    Generate and store hashes for all files in a directory and its subdirectories.
    
    Parameters:
    - directory: The root directory to scan for files.
    - hash_file: Path to the file where the hashes will be stored.
    - algorithm: Hash algorithm to use (default is SHA-256).
    """
    hash_dict = {}
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Compute the hash of the file
            file_hash = compute_file_hash(file_path, algorithm)
            # Store the file path and its hash in the dictionary
            hash_dict[file_path] = file_hash
    
    # Store all hashes in the specified file
    store_hashes(hash_dict, hash_file)

def verify_integrity(hash_file, algorithm='sha256'):
    """
    Verify the integrity of files by comparing their current hashes to stored hashes.
    
    Parameters:
    - hash_file: Path to the file containing the stored hashes.
    - algorithm: Hash algorithm to use for verification (default is SHA-256).
    """
    # Read the stored hashes from the file
    with open(hash_file, 'r') as f:
        stored_hashes = dict(line.strip().split(':') for line in f)
    
    # Compare each stored hash with the current hash of the corresponding file
    for file_path, old_hash in stored_hashes.items():
        if os.path.exists(file_path):
            # Compute the current hash of the file
            current_hash = compute_file_hash(file_path, algorithm)
            if current_hash != old_hash:
                print(f'File changed: {file_path}')
            else:
                print(f'File intact: {file_path}')
        else:
            print(f'File missing: {file_path}')

# Example usage:

# Directory to scan for files and generate hashes
directory = '/path/to/your/directory'

# File to store the generated hashes
hash_file = 'file_hashes.txt'

# Generate and store hashes for all files in the specified directory
generate_hashes(directory, hash_file)

# Verify the integrity of the files by comparing their current hashes to the stored hashes
verify_integrity(hash_file)
