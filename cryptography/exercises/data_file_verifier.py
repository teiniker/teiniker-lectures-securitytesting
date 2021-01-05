import unittest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import serialization

class DataFileVerifier:
    def __init__(self, filename):
        # Load public key
        with open(filename, "rb") as key_file:
            self.public_key = serialization.load_pem_public_key(
                key_file.read()
            )
            print('Load public key: ' + str(self.public_key))

    def verify_data_file(self, filename):
        with open(filename + '.data', 'rb') as f:
            data = f.read()
            print('Data: ' + data.hex())

        with open(filename + '.signature', 'rb') as f:
            signature = f.read()
            print('Signature: ' + signature.hex())

        self.public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length = padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        # If the signature does not match, verify() will raise an InvalidSignature exception.
        return data


class SignatureTest(unittest.TestCase):

    def setUp(self):
        self.verifier = DataFileVerifier('../public_key.pem')

    def test_load_and_verify(self):
        data = self.verifier.verify_data_file('../measurement')
        print('Verified data: ' + data.hex())

    def test_load_and_verify_invalid(self):
        with self.assertRaises(InvalidSignature):
            self.verifier.verify_data_file('../measurement2')


    def test_save_data_and_signature(self):
        # Create data file
        with open('../measurement.data', 'wb') as f:
            data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
            f.write(data)

        # Create data file signature
        with open("../private_key.pem", "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
            print('Load private key: ' + str(self.private_key))

        signature = self.private_key.sign(
            data,
            padding.PSS(
                padding.MGF1(
                    hashes.SHA256()),
                    salt_length = padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        print('Signature: ' + signature.hex())
        with open('../measurement.signature', 'wb') as f:
            f.write(signature)

if __name__ == '__main__':
    unittest.main()
