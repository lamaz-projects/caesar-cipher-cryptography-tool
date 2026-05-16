def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Handle uppercase vs lowercase boundaries
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the shifted character position
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            cipher_text += shifted_char
        else:
            # Leave spaces, punctuation, and numbers untouched
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, shift):
    # Decryption is just shifting backward by the same amount
    return caesar_encrypt(cipher_text, -shift)

def main():
    print("=========================================")
    print("      CAESAR CIPHER ENCRYPTION TOOL      ")
    print("=========================================")
    
    mode = input("Choose an option (encrypt / decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("[-] Error: Invalid selection. Choose either 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer, e.g., 3): "))
    except ValueError:
        print("[-] Error: Shift value must be a valid number.")
        return

    # Call the appropriate encapsulated function
    if mode == 'encrypt':
        result = caesar_encrypt(text, shift)
        print(f"\n[+] Encrypted Text: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"\n[+] Decrypted Text: {result}")
        
    print("=========================================")

if __name__ == "__main__":
    main()