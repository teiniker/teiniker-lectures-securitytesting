import unittest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FileEncryptor:
    def __init__(self, password:bytes, salt:bytes, iv:bytes)->None:
        key = self.key_derivation(password, salt)
        self.cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

    def key_derivation(self, password:bytes, salt:bytes)->bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(password)
        return key

    def load(self, filename:str)->bytes:
        with open(filename, 'rb') as f:
            ciphertext = f.read()
        return self.decrypt(ciphertext)

    def save(self, filename:str, data:bytes)->None:
        ciphertext = self.encrypt(data)
        with open(filename, 'wb') as f:
            f.write(ciphertext)

    def encrypt(self, plaintext:bytes)->bytes:
        encryptor = self.cipher.encryptor()
        ciphertext = encryptor.update(plaintext)
        encryptor.finalize()
        return ciphertext

    def decrypt(self, ciphertext:bytes)->bytes:
        decryptor = self.cipher.decryptor()
        plaintext = decryptor.update(ciphertext)
        decryptor.finalize()
        return plaintext


class FileEncryptorTest(unittest.TestCase):
    def setUp(self):
        password = b'TopSecret!'
        salt = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        iv = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        self.encrypter = FileEncryptor(password, salt, iv)

    def test_save_bytes(self):
        data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
        self.encrypter.save('secure.data', data)
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
