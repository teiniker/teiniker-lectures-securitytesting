# Python Bytes and Bytearrays

## Python Data Types

Python supports a range of types to store sequences. There are six sequence types: strings, byte sequences (bytes objects), byte arrays (bytearray objects), lists, tuples, and range objects.

**Strings** contain Unicode characters. Their literals are written in single or double quotes : 'python', "data". 

**Bytes** and **bytearray** objects contain single bytes – the former is immutable while the latter is a mutable sequence. Bytes objects can be constructed the constructor, `bytes()`, and from literals; use a `b` prefix with normal string syntax: `b'python'`. 
To construct byte arrays, use the `bytearray()` function.

Distinguish the following types in Python: 

* **str**:
    A string is a sequence of Unicode characters (encoded in UTF -16 or UTF-32 and entirely depends on Python’s compilation).

* **bytes**:
    Byte strings in Python 3 are officially called bytes, an immutable sequence of integers in the range 0 <= x < 256.

* **bytearray**:     
    Another bytes-like object added in 2.6 is the bytearray - similar to **bytes**, but mutable.   

### Operations

* `str.encode()`: **Returns a bytes representation** of the Unicode string, encoded in the requested encoding.

* `bytes.fromhex()`: This method **creates a bytes object** from a string of hexadecimal digits.

* `bytes.decode()`: This function is used to **convert bytes to string object**.


## Base64 Encoding 

The `base64` module provides functions for **encoding binary data to printable ASCII characters** and decoding such encodings back to binary data. 
It provides encoding and decoding functions for the encodings specified in **RFC 4648**, which defines the Base16, Base32, and Base64 algorithms, and for the de-facto standard Ascii85 and Base85 encodings.

### Operations

* `base64.standard_b64encode(s)`: Encode bytes-like object `s` using the **standard Base64 alphabet** and return the encoded bytes.

* `base64.standard_b64decode(s)`: Decode bytes-like object or ASCII string `s` using the **standard Base64 alphabet** and return the decoded bytes.

* `base64.urlsafe_b64encode(s)`: Encode bytes-like object `s` using the **URL- and filesystem-safe alphabet**, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the encoded bytes. The result can still contain `=`.

* `base64.urlsafe_b64decode(s)`: Decode bytes-like object or ASCII string s using the **URL- and filesystem-safe alphabet**, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the decoded bytes.


## Base16 Encoding 

Base16 encoding (a.k.a. Hex encoding) uses powers of 16. 
The possible digits are `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A`, `B`, `C`, `D`, `E`, and `F`.

### Operations 

* `base64.b16encode(s)`: Encode the bytes-like object `s` using Base16 and return the encoded bytes.

* `base64.b16decode(s, casefold=False)`: Decode the Base16 encoded bytes-like object or ASCII string s and return the decoded bytes. Optional casefold is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is `False`.


## References

* [Python Bytes, Bytearray](https://www.w3resource.com/python/python-bytes.php)
* [base64 — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)

*Egon Teiniker, 2020-2022, GPL v3.0*
 