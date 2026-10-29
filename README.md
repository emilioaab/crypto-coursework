# Cryptography coursework

From-scratch implementations written for the cybersecurity track at SCE —
no crypto libraries, the algorithms are built by hand to understand the internals.

## Contents
- **`des/`** — DES block cipher: initial/final permutations, key schedule, 16 Feistel rounds, encrypt/decrypt.
- **`rsa/`** — RSA: extended Euclidean algorithm, modular inverse, key setup and decryption.

## Run
```bash
python3 des/DES.py
python3 rsa/rsa.py
```
