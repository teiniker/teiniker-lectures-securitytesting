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


## Operations

* str.encode(): **Returns a bytes representation** of the Unicode string, encoded in the requested encoding.

* bytes.fromhex(): This method **creates a bytes object** from a string of hexadecimal digits.

* bytes.decode(): This function is used to **convert bytes to string object**.

## References

* [Python Bytes, Bytearray](https://www.w3resource.com/python/python-bytes.php)


*Egon Teiniker, 2020-2022, GPL v3.0*
 