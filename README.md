# Vigenère Cipher in Python

A clean and well-documented Python implementation of the **Vigenère cipher** — one of the most classical encryption algorithms.
This repository includes two standalone scripts: one for **encryption** and one for **decryption**, both fully **PEP 8 compliant** and executable directly from the **command line**.

---

## Usage

### Encryption

```
bash
python3 vigenere_encrypt.py "ATTACKATDAWN" "LEMON"
```

Output : LXFOPVEFRNHR

---

### Decryption

```
python3 vigenere_decrypt.py "LXFOPVEFRNHR" "LEMON"
```

Output : ATTACKATDAWN

---

## How the Vigenère Cipher Works

The Vigenère cipher is a polyalphabetic substitution cipher.
Each letter of the plaintext is shifted according to the corresponding letter of a repeating key.

Example:

| Plaintext  | A | T | T | A | C | K | A | T | D | A | W | N |
| ---------- | - | - | - | - | - | - | - | - | - | - | - | - |
| Key        | L | E | M | O | N | L | E | M | O | N | L | E |
| Ciphertext | L | X | F | O | P | V | E | F | R | N | H | R |

---

## Features

- Clean and simple Python 3 implementation

- Fully PEP 8 compliant

- Command-line arguments for text and key

- Works with uppercase and lowercase letters

- Well-documented functions with docstrings

- Licensed under MIT (open source)
