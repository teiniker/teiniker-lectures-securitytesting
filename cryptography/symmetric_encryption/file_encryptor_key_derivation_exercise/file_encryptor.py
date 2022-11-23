import unittest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FileEncryptor:
    # TODO
    pass


class FileEncryptorTest(unittest.TestCase):
    def setUp(self):
        password = b'TopSecret!'
        salt = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        iv = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')        
        self.encrypter = FileEncryptor(password, salt, iv)

    def test_save_bytes(self):
        data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
        hash = self.encrypter.save('secure.data', data)
        # verify encrypted data from the file 
        with open('secure.data', 'rb') as f:
            ciphertext = f.read()    
            self.assertEqual("b666fa439a76471e1e9ca25662cbba8c", ciphertext.hex())

    def test_load_bytes(self):
        data = self.encrypter.load('secure.data')
        print(data)
        self.assertEqual("000102030405060708090a0b0c0d0e0f", data.hex())


if __name__ == '__main__':
    unittest.main()
