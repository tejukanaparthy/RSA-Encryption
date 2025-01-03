# RSA-Encryption

This is a simple RSA encryption and decryption tool written in Python. It allows you to generate RSA key pairs, encrypt and decrypt files using the RSA algorithm.

## Features
- **Key Pair Generation**: Generate RSA public and private key pairs.
- **File Encryption**: Encrypt files using the public key.
- **File Decryption**: Decrypt files using the private key.

## Prerequisites
- Python 3.x
- `pycryptodome` library

## Installation

### Clone the Repository
    git clone git@github.com:tejukanaparthy/RSA-Encryption.git

### Install Dependencies

Navigate to the project directory and install the necessary dependencies:

    cd RSA-Encryption
    pip install -r requirements.txt

# Usage

### Generate RSA Key Pair:
    python rsa_encryption_tool.py generate-keys

### Encrypt a File:
    python rsa_encryption_tool.py encrypt test_files/input.txt test_files/encrypted.txt public.pem

### Decrypt a File:
    python rsa_encryption_tool.py decrypt test_files/encrypted.txt test_files/decrypted.txt private.pem

# Project Structure

    RSA-Encryption/
    ├── README.md
    ├── requirements.txt
    ├── rsa_encryption_tool.py
    └── test_files/
        └── input.txt
    └── encrypted.txt
    └── decrypted.txt

- **rsa_encryption_tool.py**: The main script for encryption and decryption operations.
- **requirements.txt**: A file that lists the required Python dependencies.
- **test_files/**: A directory containing test files (e.g., input.txt) for testing encryption and decryption.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

