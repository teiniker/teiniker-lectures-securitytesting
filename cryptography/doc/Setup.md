# Setup Cryptographic Libraries in Python

## Python Package Installer
believe it or not, Kali doesn't include the Python package installer, 
so we have to install it first:
```
$ sudo apt install python3-pip
```

## pyca/cryptography
[cryptography](https://cryptography.io/en/latest/)
 includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions.
```
$ pip install cryptography
```

Note that on Kali Linux an **old version** is already installed.
In that case, we have to update the library:
```
$ pip install cryptography --upgrade
Successfully installed cffi-1.14.3 cryptography-3.1.1 pycparser-2.20
```

