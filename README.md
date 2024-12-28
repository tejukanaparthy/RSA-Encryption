# RSA-Encryption

# This is a simple RSA encryption and decryption tool written in Python. It allows you to generate RSA key pairs, encrypt and decrypt files using the RSA algorithm.

## Features
# - **Key Pair Generation**: Generate RSA public and private key pairs.
# - **File Encryption**: Encrypt files using the public key.
# - **File Decryption**: Decrypt files using the private key.

## Prerequisites
# - Python 3.x
# - `pycryptodome` library

## Installation

### Clone the Repository
# Clone this repository to your local machine:

# ```bash
# git clone https://github.com/your-username/rsa-encryption.git
# ```

### Install Dependencies
# Navigate to the project directory and install the necessary dependencies:

# ```bash
# cd rsa-encryption
# pip install -r requirements.txt
# ```

## Usage

### Generate RSA Key Pair
# To generate the RSA public and private key pair, run the following command:

# ```bash
# python rsa_encryption_tool.py generate-keys
# ```

# This will create two files: `private.pem` (private key) and `public.pem` (public key).

### Encrypt a File
# To encrypt a file using the public key, run:

# ```bash
# python rsa_encryption_tool.py encrypt test_files/input.txt test_files/encrypted.txt public.pem
# ```

# This command will encrypt the contents of `input.txt` and save the encrypted data in `encrypted.txt`.

### Decrypt a File
# To decrypt a file using the private key, run:

# ```bash
# python rsa_encryption_tool.py decrypt test_files/encrypted.txt test_files/decrypted.txt private.pem
# ```

# This command will decrypt the contents of `encrypted.txt` and save the decrypted data in `decrypted.txt`.

### Verify Decryption
# After decryption, you can verify that the decryption was successful by checking the contents of the decrypted file:

# ```bash
# cat test_files/decrypted.txt
# ```

# The contents of `decrypted.txt` should match the original `input.txt`.

## Project Structure

# ```bash
# .
# ├── README.md
# ├── requirements.txt
# ├── rsa_encryption_tool.py
# └── test_files
#     └── input.txt
# ```

# - `rsa_encryption_tool.py`: The main script for encryption and decryption operations.
# - `requirements.txt`: A file that lists the required Python dependencies.
# - `test_files/`: A directory containing test files (e.g., `input.txt`) for testing encryption and decryption.

## License
# This project is licensed under the MIT License - see the LICENSE file for details.
