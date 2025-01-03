from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open('private.pem', 'wb') as priv_file:
        priv_file.write(private_key)

    with open('public.pem', 'wb') as pub_file:
        pub_file.write(public_key)

    print("Keys generated and saved as 'private.pem' and 'public.pem'.")

def encrypt_message(message, public_key_path):
    with open(public_key_path, 'rb') as pub_file:
        public_key = RSA.import_key(pub_file.read())
    
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_msg = cipher.encrypt(message.encode('utf-8'))
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    
    return encoded_encrypted_msg

def decrypt_message(encrypted_message, private_key_path):
    with open(private_key_path, 'rb') as priv_file:
        private_key = RSA.import_key(priv_file.read())
    
    cipher = PKCS1_OAEP.new(private_key)
    decoded_encrypted_msg = base64.b64decode(encrypted_message)
    decrypted_msg = cipher.decrypt(decoded_encrypted_msg)

    return decrypted_msg.decode('utf-8')

if __name__ == "__main__":
    try:
        with open('private.pem', 'rb') as _:
            pass
    except FileNotFoundError:
        generate_keys()

    message = "Hello, this is a secure message!"
    encrypted_message = encrypt_message(message, 'public.pem')
    print(f"Encrypted message: {encrypted_message.decode('utf-8')}")

    decrypted_message = decrypt_message(encrypted_message, 'private.pem')
    print(f"Decrypted message: {decrypted_message}")
