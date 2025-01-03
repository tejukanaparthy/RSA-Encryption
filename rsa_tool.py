import argparse
from generate_keys import generate_keys
from rsa_encrypt import encrypt_message_from_file
from rsa_decrypt import decrypt_message_from_file

def main():
    parser = argparse.ArgumentParser(description="RSA Encryption/Decryption Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    parser_gen = subparsers.add_parser('generate-keys', help="Generate RSA key pair")
    parser_gen.add_argument('--private', default='private.pem', help="Path to save private key")
    parser_gen.add_argument('--public', default='public.pem', help="Path to save public key")

    parser_enc = subparsers.add_parser('encrypt', help="Encrypt a message")
    parser_enc.add_argument('input', help="Path to input plaintext file or message")
    parser_enc.add_argument('output', help="Path to output encrypted file")
    parser_enc.add_argument('public_key', help="Path to public key file")

    parser_dec = subparsers.add_parser('decrypt', help="Decrypt a message")
    parser_dec.add_argument('input', help="Path to input encrypted file or message")
    parser_dec.add_argument('output', help="Path to output plaintext file")
    parser_dec.add_argument('private_key', help="Path to private key file")

    args = parser.parse_args()

    if args.command == 'generate-keys':
        generate_keys(args.private, args.public)
    elif args.command == 'encrypt':
        encrypt_message_from_file(args.input, args.output, args.public_key)
    elif args.command == 'decrypt':
        decrypt_message_from_file(args.input, args.output, args.private_key)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

