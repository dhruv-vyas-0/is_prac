# RSA Algorithm Implementation

def rsa_encrypt(message, e, n):
    """Encrypt the message using the public exponent e and modulus n."""
    ciphertext = pow(message, e, n)
    return ciphertext

def rsa_decrypt(ciphertext, d, n):
    """Decrypt the ciphertext using the private exponent d and modulus n."""
    decrypted_message = pow(ciphertext, d, n)
    return decrypted_message

def main():
    p = 3   # A prime number
    q = 11  # Another prime number
    
    # Calculate n
    n = p * q
    
    # Calculate phi
    phi = (p-1) * (q-1)
    
    # Choose a ublic exponent
    e = 3
    
    # Calculate d such that...
    # d * e = 1 mod phi
    d = 7

    # Prompt the user for a message
    # condition : message < n
    message = int(input("Enter a message as an integer (0-32): "))

    # Ensure the message is within the valid range
    if message < 0 or message >= n:
        print(f"Message must be between 0 and {n-1}.")
        return

    # Encrypt the message
    ciphertext = rsa_encrypt(message, e, n)
    print(f"Encrypted message (ciphertext): {ciphertext}")

    # Decrypt the ciphertext
    decrypted_message = rsa_decrypt(ciphertext, d, n)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

