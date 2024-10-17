def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")

    # Step 1: Generate a large prime number and a primitive root
    prime = 23
    primitive_root = 9

    print(f"Prime number (p): {prime}")
    print(f"Primitive root (g): {primitive_root}")

    # Step 2: Each party chooses a secret key
    secret_key_a = int(input("Party A, enter your secret key (a): "))
    secret_key_b = int(input("Party B, enter your secret key (b): "))

    # Step 3: Calculate the public keys
    public_key_a = pow(primitive_root, secret_key_a, prime)
    public_key_b = pow(primitive_root, secret_key_b, prime)

    print(f"Party A's public key: {public_key_a}")
    print(f"Party B's public key: {public_key_b}")

    # Step 4: Each party calculates the shared secret
    shared_secret_a = pow(public_key_b, secret_key_a, prime)
    shared_secret_b = pow(public_key_a, secret_key_b, prime)

    print(f"Party A's calculated shared secret: {shared_secret_a}")
    print(f"Party B's calculated shared secret: {shared_secret_b}")

    # Step 5: Verify that both shared secrets are equal
    if shared_secret_a == shared_secret_b:
        print("Shared secrets match! Key exchange successful.")
    else:
        print("Shared secrets do not match! Key exchange failed.")

if __name__ == "__main__":
    diffie_hellman()

