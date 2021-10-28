# Key Derivation Functions

## PBKDF2 (Password-Based Key Derivation Function 2)

Since a password is not directly applicable as a key to any conventional
cryptosystem, however, some processing of the password is required to perform
cryptographic operations with it. Moreover, as passwords are often chosen
from a relatively small space, special care is required in that processing
to defend against search attacks.

Another approach to password-based cryptography is to construct key derivation
techniques that are relatively expensive, thereby increasing the cost of
exhaustive search. One way to do this is to include an iteration count in the
key derivation technique, indicating how many times to iterate some underlying
function by which keys are derived.


## SCrypt

SCrypt is a **password-based key derivation function** created by Colin Percival.

With existing key derivation algorithms, even when the iteration count is
increased so that the time taken to verify a password remains constant, the
cost of finding a password by using a brute-force attack implemented in
hardware drops each year.

The scrypt function aims to reduce the advantage that attackers can gain by using
custom-designed parallel circuits for breaking password-based key derivation
functions.

The scrypt function takes several parameters:
* The **passphrase P** is typically a human-chosen password.
* The **salt** is normally uniquely and randomly generated [RFC4086].
* The parameter **r** specifies the block size.
* The CPU/Memory cost parameter **N** must be larger than 1,
       a power of 2, and less than 2^(128 * r / 8).
* The parallelization parameter **p**  is a positive
      integer less than or equal to ((2^32-1) * 32) / (128 * r).

Users of scrypt can tune the parameters N, r, and p according to the amount
of memory and computing power available, the latency-bandwidth product of the
memory subsystem, and the amount of parallelism desired.

At the current time, r=8 and p=1 appears to yield good results, but as memory
latency and CPU parallelism increase, it is likely that the optimum values for
both r and p will increase.      


## References
* [cryptography: Key derivation functions](https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions.html)

* [RFC 7914: The scrypt Password-Based Key Derivation Function](https://tools.ietf.org/html/rfc7914)
* [RFC2898: PKCS #5: Password-Based Cryptography Specification Version 2.0](https://tools.ietf.org/html/rfc2898)

* [WinZip: About Encryption](http://kb.winzip.com/help/help_encryption.htm)


*Egon Teiniker, 2020-2021, GPL v3.0*