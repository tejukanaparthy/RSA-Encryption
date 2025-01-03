import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def decrypt_message_from_file(input_file, output_file, private_key_path):
    """Decrypts an encrypted message from a file and writes the decrypted message to an output file."""
    try:
        # Open private key and create cipher object
        with open(private_key_path, 'rb') as priv_file:
            private_key = RSA.import_key(priv_file.read())

        cipher = PKCS1_OAEP.new(private_key)

        # Read encrypted message from input file
        with open(input_file, 'rb') as file:
            encrypted_message = file.read()

        # Decode the base64 encoded message
        try:
            decoded_encrypted_msg = base64.b64decode(encrypted_message)
        except ValueError as e:
            print(f"Error decoding base64: {e}")
            return

        # Decrypt the message
        decrypted_msg = cipher.decrypt(decoded_encrypted_msg)

        # Write the decrypted message to the output file
        with open(output_file, 'w') as out_file:
            out_file.write(decrypted_msg.decode('utf-8'))

        print(f"Decrypted message saved to {output_file}")

    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    input_file = 'test_files/encrypted_message.txt'  # Reading the encrypted file
    output_file = 'test_files/decrypted_message.txt'  # Output to a decrypted file
    private_key_path = 'private.pem'

    decrypt_message_from_file(input_file, output_file, private_key_path)
