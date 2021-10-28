import unittest
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class KeyDerivationFunctionTest(unittest.TestCase):

    # PBKDF2 (Password Based Key Derivation Function 2) is typically used for
    # deriving a cryptographic key from a password.

    def test_PBKDF2(self):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(b"password")
        print(key.hex())

    # Scrypt is a KDF designed for password storage by Colin Percival
    def test_scrypt(self):
        salt = os.urandom(16)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1
        )
        key = kdf.derive(b"password")
        print(key.hex())


if __name__ == '__main__':
    unittest.main()
