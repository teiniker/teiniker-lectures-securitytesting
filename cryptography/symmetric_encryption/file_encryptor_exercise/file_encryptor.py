import unittest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Exercise: File Encryptor
#
# Implement a class called "FileEncrypter" with the following operations:
# 1. __init__(self, key, iv)
#   A constructor that takes a secret key and an initialization vector (iv) to setup
#   an AES cipher in CTR mode.
#
# 2. save(self, filename, data)
#   Encrypt the given data with the AES cipher.
#   Store the ciphertext in a binary file with the given "filename".
#
# 3. load(self, filename)
#   Load the content of a binary file with the given "filename".
#   Decrypt the loaded bytes with the AES cipher and return the plaintext data.

class FileEncryptor:
    # TODO
    pass

class FileEncryptorTest(unittest.TestCase):
    def setUp(self):
        # key = os.urandom(32)  # 256 bit key
        key = bytes.fromhex('a4f7802bd2b099fdd603abb5cc20a5402719f6d408975017950a021bb2f1ee52')
        print('key: ' + key.hex())
        # iv = os.urandom(16)  # equal to block size
        iv = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        print(' iv : ' + iv.hex())
        self.encrypter = FileEncryptor(key, iv)

    def test_save_bytes(self):
        data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
        hash = self.encrypter.save('secure.data', data)

    def test_load_bytes(self):
        data = self.encrypter.load('secure.data')
        print(data)
        self.assertEqual("000102030405060708090a0b0c0d0e0f", data.hex())

if __name__ == '__main__':
    unittest.main()
