# Caesar Cipher Encryption Tool

A modular, clean Python script implementing the historical Caesar Cipher algorithm to scramble and descramble text strings using custom rotational alphabet shifts.

## Technical Details
This implementation strictly leverages modular design by separating the cryptographic processes into isolated logical components:
* caesar_encrypt(plain_text, shift): Maps character unicode code-points (ord()) to wrap boundaries across a mod-26 alphabet layer.
* caesar_decrypt(cipher_text, shift): Smoothly reverses the positional offset values by processing inverse mathematical logic loops.

Non-alphabetic artifacts (numerical values, empty space layouts, and unique punctuation elements) are entirely preserved without modification.

## Usage
1. Verify Python availability on your native CLI environment.
2. Clone this repository or copy the caesar_cipher.py script.
3. Launch the script via terminal processing:
   ```bash
   python caesar_cipher.py
