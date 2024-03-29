# Generating Private and Public Keys Using OpenSSL

To generate an RSA **private key** type the following command:
```
$ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out openssl-private-key.pem
$ cat private-key.pem
-----BEGIN PRIVATE KEY-----
MIIJQQIBADANBgkqhkiG9w0BAQEFAASCCSswggknAgEAAoICAQC18RulJsPhX8TM
H25/0yzcSB5zOXT6NiVxMloysok9c2va5HlauydRYCxnGLISAcaeKPg3JFmQ78Bb
ffkmWB8Aexw0fHdP38A0AE3tfrLUC9AAIRZ3SsgyaUQ04aTmDHVfCYBHa81ezjVa
...
0WzCDbcVjDorfaWLomo932bimsi2gMMLH/c93k9VXShKkQhKLPKbiocGlWqVcb5u
xGp7shRR6ykLLPKx75gj3KPjt0hqBP+4WXJRZdAt8k44YAt2FN11C/8M2bazYNdp
zK0Ot5tcBeH7KuM1BEzd78cIJBUW
-----END PRIVATE KEY-----
```
Parameters: 
* **genpkey**: Generate a private key.
* **-algorithm alg**: Public key algorithm to use such as **RSA**, DSA or DH.
* **-pkeyopt opt:value**: Set the public key algorithm option `opt` to `value`.
* **-out filename**: Output the key to the specified file. If this argument is not specified then standard output is used.
 
Having previously generated your private key, you may generate the corresponding **public key** using the following command:
```
$ openssl pkey -in openssl-private-key.pem -out openssl-public-key.pem -pubout
$ cat public-key.pem 
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAtfEbpSbD4V/EzB9uf9Ms
3Egeczl0+jYlcTJaMrKJPXNr2uR5WrsnUWAsZxiyEgHGnij4NyRZkO/AW335Jlgf
AHscNHx3T9/ANABN7X6y1AvQACEWd0rIMmlENOGk5gx1XwmAR2vNXs41WjrdSPh1
aN2ipN/OFZt0MDGVxliXhUDZ6pvfrYbXwRYxDd1bNK8dHYaw73ybWK9gI6SCCsbB
...
LEgYQN1N5RURmiBI8WWOdv6JUH3Ddd3zOj+wTCv6qIUX4gLQ4pgHHc8MRmAmsoUQ
kWK+pn2FV8/KjGaYXhR+TeDg/TXj6db43GPXCPFjYtu/a6kWvT7xEK1tE+4r/P8X
h//Br01zuuLfBgtd633gT1UCAwEAAQ==
-----END PUBLIC KEY-----
```
Parameters:
* **pkey**: Public or private key processing tool.
* **-in filename**: This specifies the **input filename** to read a key from or standard input 
   if this option is not specified. 
   If the key is encrypted a pass phrase will be prompted for.
* **-out filename**: This specifies the **output filename** to write a key to or standard output 
   if this option is not specified. 
   If any encryption options are set then a pass phrase will be prompted for. 
   The output filename should **not be the same** as the input filename.
* **-pubout**: By default a private key is output: with this option a **public key** will be 
   output instead. This option is automatically set if the input is a public key.


## References
* [openssl](https://www.openssl.org/docs/man1.1.1/man1/openssl.html)

*Egon Teiniker, 2020-2021, GPL v3.0*