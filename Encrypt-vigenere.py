"""
Vigenère Cipher - Encryption Script
This script encrypts a given plaintext using a Vigenère cipher key.
"""

import sys


def vigenere_encrypt(plaintext, key):
    """
    Encrypt a plaintext using the Vigenère cipher.

    Parameters
    ----------
    plaintext : str
        The message to encrypt.
    key : str
        The keyword used for encryption.

    Returns
    -------
    str
        The encrypted ciphertext.
    """
    result = []
    key = key.upper()
    plaintext = plaintext.upper()
    key_index = 0

    for c in plaintext:
        if c.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted = (ord(c) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(encrypted))
            key_index += 1
        else:
            result.append(c)
    return ''.join(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vigenere_encrypt.py <plaintext> <key>")
        sys.exit(1)

    text = sys.argv[1]
    key = sys.argv[2]
    print(vigenere_encrypt(text, key))
