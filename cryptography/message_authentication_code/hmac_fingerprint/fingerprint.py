import unittest
import hashlib
import hmac

class Fingerprint:
    def __init__(self, key):
        self.key_bytes = bytes.fromhex(key)
        #print('key_bytes = ' + str(self.key_bytes))

    def from_file(self, filename):
        with open(filename, 'rb') as f:
            buffer = f.read()
        return self.from_bytes(buffer)

    def from_string(self, text):
        return self.from_bytes(text.encode('utf-8'))

    def from_bytes(self, data):
        digest = hmac.new(self.key_bytes, data, hashlib.sha256)
        value = digest.hexdigest()
        return value


class FingerprintTest(unittest.TestCase):
    def setUp(self):
        # The key consists of 32 random bytes 
        key = "fce0ddc9bf4ad0f68d92af77b42b486bd10c27bc1b45a4c4929cda4f63bf0386"
        self.fingerprint = Fingerprint(key)

    def test_from_bytes(self):
        data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
        print(data)
        mac = self.fingerprint.from_bytes(data)
        print(f'mac of byte array = {mac}')
        self.assertEqual("9864b5619d85f2c0d8025bdfcf375d9f1c95aca25fea7fa235053f2f60925086", mac)

    def test_from_string(self):
        text = 'Pleased to meet you, hope you guess my name'
        mac = self.fingerprint.from_string(text)
        print(f'mac of string    = {mac}')
        self.assertEqual("a88533ad56b2acaa1d569cae1a9a6785b0a5cd2dc266ee601dc33667ff9daa6f", mac)

    def test_from_file(self):
        filename = "wordlist.txt"
        mac = self.fingerprint.from_file(filename)
        print(f'mac of file      = {mac}')
        self.assertEqual("8c6f05f6800af9cd374f45c6d5b0a5bb8b4764629a4e130c510de8793b32f12d", mac)
 
if __name__ == '__main__':
    unittest.main()
