import unittest


class ByteArrayTest(unittest.TestCase):

    def test_list_to_bytearray(self):
        prime_numbers = [2, 3, 5, 7]
        byte_array = bytearray(prime_numbers)
        print(byte_array)

    def test_bytes_to_bytearray(self):
        b = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        byte_array = bytearray(b)
        print(byte_array)

    def test_string_to_bytearray(self):
        s = 'message'
        byte_array = bytearray(s, 'utf-8')
        byte_array[0] = 0x64
        print(byte_array)

        
if __name__ == '__main__':
    unittest.main()
