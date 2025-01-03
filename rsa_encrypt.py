from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt_message(message, public_key_path):
    """Encrypts a message using the public key."""
    with open(public_key_path, 'rb') as pub_file:
        public_key = RSA.import_key(pub_file.read())
    
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_msg = cipher.encrypt(message.encode('utf-8'))
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)

    return encoded_encrypted_msg

def encrypt_message_from_file(input_file, output_file, public_key_path):
    """Encrypts a message from a file and writes the encrypted message to an output file."""
    try:
        with open(input_file, 'r') as file:
            message = file.read()

        encrypted_message = encrypt_message(message, public_key_path)

        with open(output_file, 'wb') as file:
            file.write(encrypted_message)

        print(f"Message encrypted and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error during encryption: {e}")

if __name__ == "__main__":
    input_file = 'test_files/input.txt'  # Reading from the input file
    output_file = 'test_files/encrypted_message.txt'  # Output to an encrypted file
    public_key_path = 'public.pem'

    encrypt_message_from_file(input_file, output_file, public_key_path)
