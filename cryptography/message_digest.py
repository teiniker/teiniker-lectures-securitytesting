import unittest
import hashlib

# Secure hashes and message digests
# https://docs.python.org/3/library/hashlib.html

class MessageDigestTest(unittest.TestCase):

    def test_SHA256(self):
        b = "message".encode('utf-8')
        m = hashlib.sha256()
        m.update(b)
        value = m.hexdigest()
        print(value)

    def test_SHA512(self):
        b = "message".encode('utf-8')
        m = hashlib.sha512()
        m.update(b)
        value = m.hexdigest()
        print(value)


if __name__ == '__main__':
    unittest.main()