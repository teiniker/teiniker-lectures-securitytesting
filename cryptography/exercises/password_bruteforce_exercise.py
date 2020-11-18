import unittest
import hashlib
import os


# Exercise: Password Brute Force Attack
#
# 1. PasswordEncryption
# Implement a class "PasswordEncryption" with the following methods:
#   def encrypt(self, password):
#   verify(self, password, password_hash):
# To encrypt the password, use a SHA-256 algorithm.
# Verify your implementation using the test_encrypt() and test_verify(self) tests.
#
# 2. Brute Force Attack
# Implement a test_bruteforce() test which reads common passwords from
# the "wordlist.txt" file. Each line will be encrypted and compared to the
# given hash value:
#    password_hash = "04e77bf8f95cb3e1a36a59d1e93857c411930db646b46c218a0352e432023cf2"
# If the hash values match, you have found the plaintext password - print it to the
# console window.
#

class PasswordEncryption:

    def encrypt(self, password):
        # TODO
        pass

    def verify(self, password, password_hash):
        # TODO
        pass


class PasswordEncryptionTest(unittest.TestCase):
    def setUp(self):
        self.encyption = PasswordEncryption()

    def test_encrypt(self):
        password = "trink4bier!"
        hash = self.encyption.encrypt(password)
        print(hash)
        self.assertEqual("f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2", hash)

    def test_verify(self):
        password = "trink4bier!"
        hash = "f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2"
        is_valid = self.encyption.verify(password, hash)
        self.assertTrue(is_valid)

    def test_bruteforce(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()

# References:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
