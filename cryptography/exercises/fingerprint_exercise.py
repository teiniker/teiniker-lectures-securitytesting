import unittest
import hashlib

# Exercise: Fingerprint
#
# Implement a class called "Fingerprint" with the following methods:
# 1. from_bytes(self, data)
#   Calculate a SHA-256 hash value from a given binary array "data"
#
# 2. from_string(self, text)
#   Calculate a SHA-256 hash value from a given string "text"
#
# 3. from_file(self, filename)
#   Calculate a SHA-256 hash value from a given file with the name
#   "filename" read from the filesystem.
#   Compare your fingerprint with the output of the command line tool:
#       $ sha256sum wordlist.txt

class Fingerprint:
    # TODO
    pass

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


if __name__ == '__main__':
    unittest.main()
