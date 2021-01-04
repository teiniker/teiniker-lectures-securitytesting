import unittest
import hashlib

class Fingerprint:
    def from_file(self, filename):
        with open(filename, 'rb') as f:
            buffer = f.read()
        return self.from_bytes(buffer)

    def from_string(self, text):
        return self.from_bytes(text.encode('utf-8'))

    def from_bytes(selfself, data):
        digest = hashlib.sha256()
        digest.update(data)
        password_hash = digest.hexdigest()
        return password_hash


class FingerprintTest(unittest.TestCase):
    def setUp(self):
        self.fingerprint = Fingerprint()

    def test_from_bytes(self):
        data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
        print(data)
        hash = self.fingerprint.from_bytes(data)
        print(hash)
        self.assertEqual("be45cb2605bf36bebde684841a28f0fd43c69850a3dce5fedba69928ee3a8991", hash)

    def test_from_string(self):
        text = 'Pleased to meet you, hope you guess my name'
        hash = self.fingerprint.from_string(text)
        print(hash)
        self.assertEqual("3b8be20de1d75d3087f5591b0687d9b3fd036a68b42dc27c5c9618a9bb72732e", hash)

    def test_from_file(self):
        filename = "../wordlist.txt"
        hash = self.fingerprint.from_file(filename)
        print(hash)
        self.assertEqual("fd17b0ff31d7fb7b4e202b0cd99e1f11aa1f4972aab81010544a4e562f42bac7", hash)
        # compare with $ sha256sum wordlist.txt

if __name__ == '__main__':
    unittest.main()
