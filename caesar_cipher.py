# Caesar Cipher implementation using procedural approach

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

def main():
    # Prompt user to choose encryption or decryption
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice == 'E':
        # For encryption
        plaintext = input("Enter the plaintext: ").strip()
        key = int(input("Enter the key (0-25): "))
        encrypted_text = encrypt(plaintext, key)
        print(f"Encrypted text: {encrypted_text}")
        
    elif choice == 'D':
        # For decryption
        ciphertext = input("Enter the ciphertext: ").strip()
        key = int(input("Enter the key (0-25): "))
        decrypted_text = decrypt(ciphertext, key)
        print(f"Decrypted text: {decrypted_text}")
        
    else:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")

# Run the program
if __name__ == "__main__":
    main()

