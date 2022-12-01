import unittest
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricEncryptionTest(unittest.TestCase):

    def setUp(self):
        self.key = os.urandom(32)  # 256 bit key
        self.iv = os.urandom(16)  # equal to block size
        self.cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv))

    def test_encryption_and_decryption(self):
        encryptor = self.cipher.encryptor()
        ct = encryptor.update("This is a secret message.".encode('utf-8')) 
        encryptor.finalize()
        print(ct.hex())

        decryptor = self.cipher.decryptor()
        pt = decryptor.update(ct)
        decryptor.finalize()
        print(pt.hex())
        print(pt.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
