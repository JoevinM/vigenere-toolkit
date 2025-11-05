"""
Vigenère Cipher - Decryption Script
This script decrypts a ciphertext using a Vigenère cipher key.
"""

import sys


def vigenere_decrypt(ciphertext, key):
    """
    Decrypt a ciphertext encrypted with the Vigenère cipher.

    Parameters
    ----------
    ciphertext : str
        The encrypted message to decrypt.
    key : str
        The keyword used for decryption.

    Returns
    -------
    str
        The decrypted plaintext.
    """
    result = []
    key = key.upper()
    ciphertext = ciphertext.upper()
    key_index = 0

    for c in ciphertext:
        if c.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted = (ord(c) - ord('A') - shift) % 26 + ord('A')
            result.append(chr(decrypted))
            key_index += 1
        else:
            result.append(c)
    return ''.join(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vigenere_decrypt.py <ciphertext> <key>")
        sys.exit(1)

    text = sys.argv[1]
    key = sys.argv[2]
    print(vigenere_decrypt(text, key))
