import hashlib

text = input("Enter the text: ")
text_bytes = text.encode()

sha1_obj = hashlib.sha1(text_bytes)
sha1_hex = sha1_obj.hexdigest()

sha512_obj = hashlib.sha512(text_bytes)
sha512_hex = sha512_obj.hexdigest()

print(f"\n Hash Results ")
print(f"SHA-1: {sha1_hex}")
print(f"SHA-512: {sha512_hex}")

print(f"\n Comparison ")
print(f"Digest Length (Hex chars): SHA-1 ({len(sha1_hex)}) vs SHA-512({len(sha512_hex)})")
print(f"Digest Length (Bits): SHA-1 ({len(sha1_hex) * 4} bits) vs SHA-512({len(sha512_hex) * 4} bits)")

print("\nSecurity Level & Collision Resistance:")
print("- SHA-1: Considered cryptographically broken. Vulnerable to collision attacks.")
print("- SHA-512: Highly secure. Robust resistance against collisions; current industry standard.")
