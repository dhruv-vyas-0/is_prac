# Function to convert a string to a list of numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper()]

# Function to convert a list of numbers back to a string
def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

# Matrix multiplication for 2x2 matrix with a 2x1 vector (mod 26)
def matrix_multiply(matrix, vector):
    result = [0, 0]
    result[0] = (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26
    result[1] = (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26
    return result

# Encryption function
def encrypt(plain_text):
    # Hardcoded 2x2 key matrix
    # Change accordingly
    key_matrix = [[3, 3], [2, 5]]
    
    plain_numbers = text_to_numbers(plain_text)

    # If the length of the plain text is odd, add a filler character (e.g., 'X')
    if len(plain_numbers) % 2 != 0:
        plain_numbers.append(ord('X') - ord('A'))
    
    cipher_numbers = []
    # Encrypt in blocks of 2 letters
    for i in range(0, len(plain_numbers), 2):
        block = plain_numbers[i:i+2]
        cipher_block = matrix_multiply(key_matrix, block)
        cipher_numbers.extend(cipher_block)
    
    cipher_text = numbers_to_text(cipher_numbers)
    return cipher_text

# Decryption function
def decrypt(cipher_text):
    # Hardcoded inverse of the key matrix
    # Change accordingly
    inverse_key_matrix = [[15, 17], [20, 9]]  # Precomputed inverse modulo 26
    
    cipher_numbers = text_to_numbers(cipher_text)

    plain_numbers = []
    # Decrypt in blocks of 2 letters
    for i in range(0, len(cipher_numbers), 2):
        block = cipher_numbers[i:i+2]
        plain_block = matrix_multiply(inverse_key_matrix, block)
        plain_numbers.extend(plain_block)
    
    plain_text = numbers_to_text(plain_numbers)
    return plain_text

# Main function
def hill_cipher():
    # Ask the user if they want to encrypt or decrypt
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == 'e':
        # Ask for plain text
        plain_text = input("Enter the plain text: ").replace(" ", "").upper()
        # Encrypt the plain text
        cipher_text = encrypt(plain_text)
        print(f"Encrypted Text: {cipher_text}")
    
    elif choice == 'd':
        # Ask for cipher text
        cipher_text = input("Enter the cipher text: ").replace(" ", "").upper()
        # Decrypt the cipher text
        decrypted_text = decrypt(cipher_text)
        print(f"Decrypted Text: {decrypted_text}")
    
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")

# Run the cipher
hill_cipher()

