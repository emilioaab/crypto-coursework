""""Emil Abdumalikov and Topaz Trabelsi"""

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e, phi_n):
    """Find modular inverse of e modulo phi_n"""
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % phi_n + phi_n) % phi_n


def rsa_decrypt():
    # Given values
    p = 47
    q = 53
    e = 5

    # Encrypted message
    ciphertext = [999, 2197, 1242, 1242, 1320, 662, 2181, 1320, 785, 1242, 1634]

    print(f"Given values:")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"e = {e}")
    print(f"Ciphertext: {ciphertext}")
    print()

    # Step 1: Calculate n
    n = p * q
    print(f"Step 1: Calculate n")
    print(f"n = p × q = {p} × {q} = {n}")
    print()

    # Step 2: Calculate φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"Step 2: Calculate φ(n)")
    print(f"φ(n) = (p-1) × (q-1) = ({p}-1) × ({q}-1) = {p - 1} × {q - 1} = {phi_n}")
    print()

    # Step 3: Find private key d
    d = mod_inverse(e, phi_n)
    print(f"Step 3: Find private key d")
    print(f"d ≡ e⁻¹ (mod φ(n))")
    print(f"d ≡ {e}⁻¹ (mod {phi_n})")
    print(f"d = {d}")
    print()

    # Verify that e * d ≡ 1 (mod φ(n))
    verification = (e * d) % phi_n
    print(f"Verification: e × d mod φ(n) = {e} × {d} mod {phi_n} = {verification}")
    print()

    # Step 4: Decrypt the message
    print(f"Step 4: Decrypt the message")
    print(f"For each ciphertext value c, calculate: m ≡ c^d (mod n)")
    print()

    decrypted_numbers = []
    decrypted_chars = []

    for i, c in enumerate(ciphertext):
        # Decrypt: m = c^d mod n
        m = pow(c, d, n)
        decrypted_numbers.append(m)

        # Convert to character
        char = chr(m)
        decrypted_chars.append(char)

        print(f"Position {i + 1}: {c}^{d} mod {n} = {m} → '{char}'")

    print()
    print(f"Decrypted numbers: {decrypted_numbers}")
    print(f"Decrypted message: '{''.join(decrypted_chars)}'")

    return decrypted_chars


# Run the decryption
if __name__ == "__main__":
    result = rsa_decrypt()