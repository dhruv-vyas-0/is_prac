# Hardcoded monoalphabetic cipher key
# Change aaccordingly
cipher_key = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'a', 'i': 's', 'j': 'd',
    'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j', 'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u',
    'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q'
}

# Function to reverse the cipher key for decryption
def reverse_cipher_key(cipher_key):
    return {value: key for key, value in cipher_key.items()}

# Function to encrypt plaintext
def encrypt(plaintext):
    encrypted_text = ""
    for char in plaintext.lower():
        if char in cipher_key:
            encrypted_text += cipher_key[char]
        else:
            encrypted_text += char  # If character is not in the cipher key (e.g., space or punctuation)
    return encrypted_text

# Function to decrypt ciphertext
def decrypt(ciphertext):
    reversed_key = reverse_cipher_key(cipher_key)
    decrypted_text = ""
    for char in ciphertext.lower():
        if char in reversed_key:
            decrypted_text += reversed_key[char]
        else:
            decrypted_text += char  # If character is not in the cipher key
    return decrypted_text

# Main function to handle user choice
def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        plaintext = input("Enter the text to encrypt: ")
        print(f"Encrypted text: {encrypt(plaintext)}")
    elif choice == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        print(f"Decrypted text: {decrypt(ciphertext)}")
    else:
        print("Invalid choice, please enter 'e' to encrypt or 'd' to decrypt.")

# Run the main function
if __name__ == "__main__":
    main()

