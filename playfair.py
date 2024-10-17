import string

# Define the key matrix as a global variable
# Change accordingly
key_matrix = [
    ['k', 'e', 'y', 'w', 'o'],
    ['r', 'd', 'a', 'b', 'c'],
    ['f', 'g', 'h', 'i', 'l'],
    ['m', 'n', 'p', 'q', 's'],
    ['t', 'u', 'v', 'x', 'z']
]

def prepare_text(text, replace_char='x'):
    text = text.lower().replace('j', 'i')  # Replace 'j' with 'i'
    prepared_text = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else replace_char
        if a == b:
            prepared_text += a + replace_char
            i += 1
        else:
            prepared_text += a + b
            i += 2
    if len(prepared_text) % 2 != 0:
        prepared_text += replace_char
    return prepared_text

def find_position(char):
    # Use the global key_matrix
    global key_matrix
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

def encrypt(plaintext):
    global key_matrix  # Access global key_matrix
    plaintext = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)

        if row_a == row_b:
            ciphertext += key_matrix[row_a][(col_a + 1) % 5]
            ciphertext += key_matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += key_matrix[(row_a + 1) % 5][col_a]
            ciphertext += key_matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += key_matrix[row_a][col_b]
            ciphertext += key_matrix[row_b][col_a]

    return ciphertext

def decrypt(ciphertext):
    global key_matrix  # Access global key_matrix
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)

        if row_a == row_b:
            plaintext += key_matrix[row_a][(col_a - 1) % 5]
            plaintext += key_matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += key_matrix[(row_a - 1) % 5][col_a]
            plaintext += key_matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += key_matrix[row_a][col_b]
            plaintext += key_matrix[row_b][col_a]

    return plaintext

def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == 'e':
        plaintext = input("Enter the plaintext: ").replace(" ", "").lower()
        encrypted_text = encrypt(plaintext)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        ciphertext = input("Enter the ciphertext: ").replace(" ", "").lower()
        decrypted_text = decrypt(ciphertext)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

