import unittest
import random
import os
import secrets


# Generate secure random numbers for managing secrets
# https://docs.python.org/3/library/secrets.html#random-numbers

class RandomNumberTest(unittest.TestCase):

    # Note that the same seed results in the same random number !!
    # The pseudo-random generators of the random module should not be used
    # for security purposes.
    # For security or cryptographic uses, see the secrets module.
    def test_randint(self):
        random.seed(1)  # if no value is given, the current system time is used
        b = random.randint(0, 1000)
        print(b)

    #  It is our recommendation to always use your operating system’s provided random
    #  number generator, which is available as os.urandom().
    def test_urandom(self):
        iv = os.urandom(16)
        print(iv.hex())

    def test_random_token(self):
        iv = secrets.token_bytes(16)
        print(iv)
        print(iv.hex())

    def test_random_token_hex(self):
        iv = secrets.token_hex(16)
        print(iv)

    def test_random_token_urlsafe(self):
        iv = secrets.token_urlsafe(16)
        print(iv)


if __name__ == '__main__':
    unittest.main()
