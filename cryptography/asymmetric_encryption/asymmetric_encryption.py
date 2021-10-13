import unittest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import serialization

# Asymmetric Encryption
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/index.html
# Encryption is performed using the public key, meaning anyone can encrypt data.
# The data is then decrypted using the private key.

class AsymmetricEncryptionTest(unittest.TestCase):

    def setUp(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.public_key = self.private_key.public_key()


    def test_encryption_and_decryption(self):
        message = b"Some data we want to encrypt"
        print('Message   : ' + message.decode('utf-8'))
        print('Message   : ' + message.hex())

        # encrypt a message
        ciphertext = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        # Optimal Asymmetric Encryption Padding (OAEP) is a padding scheme
        # often used together with RSA encryption.
        # OAEP was introduced by Bellare and Rogaway and subsequently standardized in RFC 2437
        print('Ciphertext: ' + ciphertext.hex())

        # decrypt a message
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print('Plaintext : ' + plaintext.hex())
        print('Plaintext : ' + plaintext.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
