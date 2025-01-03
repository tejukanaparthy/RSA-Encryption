from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def decrypt_message(encrypted_message, private_key_path):
    """Decrypts an encrypted message using the private key."""
    with open(private_key_path, 'rb') as priv_file:
        private_key = RSA.import_key(priv_file.read())

    cipher = PKCS1_OAEP.new(private_key)
    decoded_encrypted_msg = base64.b64decode(encrypted_message)
    decrypted_msg = cipher.decrypt(decoded_encrypted_msg)

    return decrypted_msg.decode('utf-8')

def decrypt_message_from_file(input_file, output_file, private_key_path):
    """Decrypts an encrypted message from a file and writes the decrypted message to an output file."""
    try:
        with open(input_file, 'rb') as file:
            encrypted_message = file.read()

        decrypted_message = decrypt_message(encrypted_message, private_key_path)

        with open(output_file, 'w') as file:
            file.write(decrypted_message)

        print(f"Message decrypted and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message or file path: ")
    decrypt_message(encrypted_message, 'private.pem') 
