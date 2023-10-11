import unittest
import hashlib

class MessageDigestTest(unittest.TestCase):

    def test_sha256(self):
        b = "message".encode('utf-8')
        m = hashlib.sha256()
        m.update(b)
        value = m.hexdigest()
        print(value)

    def test_sha512(self):
        b = "message".encode('utf-8')
        m = hashlib.sha512()
        m.update(b)
        value = m.hexdigest()
        print(value)


if __name__ == '__main__':
    unittest.main()
