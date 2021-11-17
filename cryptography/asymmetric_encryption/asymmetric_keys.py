import unittest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Asymmetric Keys
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/index.html
# Asymmetric encryption uses two keys - a private key and a public key.
# Public keys are given out for anyone to use, you make them public information.

class AsymmetricKeysTest(unittest.TestCase):

    # Generating private and public key
    def setUp(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.public_key = self.private_key.public_key()

    def test_save_and_load_private_key(self):
        # Save private key
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open('private_key.pem', 'wb') as f:
            f.write(pem)

        # Load private key
        with open("private_key.pem", "rb") as key_file:
            pk = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
            print('Private key: ' + str(pk))
            print('Public  key: ' + str(pk.public_key()))

    def test_save_and_load_public_key(self):
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open('public_key.pem', 'wb') as f:
            f.write(pem)

        # Load public key
        with open("public_key.pem", "rb") as key_file:
            pubk = serialization.load_pem_public_key(
                key_file.read()
            )
            print('Public key: ' + str(pubk))

    # Generate "openssl-private-key.pem" via opensSSL
    def test_load_private_key(self):
        with open("openssl-private-key.pem", "rb") as key_file:
            pk = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
            print('Private key: ' + str(pk))
            print('Public  key: ' + str(pk.public_key()))

    # Generate "openssl-public-key.pem" via opensSSL
    def test_load_public_key(self):
        with open("openssl-public-key.pem", "rb") as key_file:
            pubk = serialization.load_pem_public_key(
                key_file.read()
            )
            print('Public key: ' + str(pubk))

if __name__ == '__main__':
    unittest.main()
