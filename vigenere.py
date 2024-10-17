def vigenere_encrypt(text, key):
    repeated_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    encrypted_text = ""
    
    for text_char, key_char in zip(text, repeated_key):
        if text_char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            base = ord('A') if text_char.isupper() else ord('a')
            encrypted_char = chr((ord(text_char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += text_char  # Non-alphabetic characters remain unchanged
    
    return encrypted_text

def vigenere_decrypt(text, key):
    repeated_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    decrypted_text = ""
    
    for text_char, key_char in zip(text, repeated_key):
        if text_char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            base = ord('A') if text_char.isupper() else ord('a')
            decrypted_char = chr((ord(text_char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += text_char  # Non-alphabetic characters remain unchanged
    
    return decrypted_text

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please choose 'E' to encrypt or 'D' to decrypt.")
        return
    
    text = input("Enter the text: ").strip()
    key = input("Enter the key: ").strip()
    
    if not key.isalpha():
        print("Key must only contain alphabetic characters.")
        return
    
    if choice == 'e':
        encrypted_text = vigenere_encrypt(text, key)
        print(f"Encrypted Text: {encrypted_text}")
    else:
        decrypted_text = vigenere_decrypt(text, key)
        print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()


