import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def decrypt_message_from_file(input_file, output_file, private_key_path):
    with open(private_key_path, 'rb') as priv_file:
        private_key = RSA.import_key(priv_file.read())
    
    cipher = PKCS1_OAEP.new(private_key)

    with open(input_file, 'rb') as file:
        encrypted_message = file.read()
    
    try:
        decoded_encrypted_msg = base64.b64decode(encrypted_message)
    except ValueError as e:
        print(f"Error decoding base64: {e}")
        return

    decrypted_msg = cipher.decrypt(decoded_encrypted_msg)

    with open(output_file, 'w') as out_file:
        out_file.write(decrypted_msg.decode('utf-8'))

    print(f"Decrypted message saved to {output_file}")

