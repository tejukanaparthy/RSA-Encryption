from Crypto.PublicKey import RSA

def generate_keys(private_key_path='private.pem', public_key_path='public.pem'):
    """Generates RSA key pair and saves them to files."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(private_key_path, 'wb') as priv_file:
        priv_file.write(private_key)

    with open(public_key_path, 'wb') as pub_file:
        pub_file.write(public_key)

    print(f"Keys generated and saved as '{private_key_path}' and '{public_key_path}'.")

if __name__ == "__main__":
    generate_keys()  
