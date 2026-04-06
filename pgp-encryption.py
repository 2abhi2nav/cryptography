import gnupg
import os

homedir = 'gpg_keys'

if not os.path.exists(homedir):
    os.makedirs(homedir, mode=0o700)

gpg = gnupg.GPG(gnupghome=homedir)
gpg.encoding = 'utf-8'


def demonstrate_pgp():
    key_input = gpg.gen_key_input(
        name_real="User Name",
        name_email="user@example.com",
        passphrase="secure_password",
        key_type="RSA",
        key_length=2048
    )

    key = gpg.gen_key(key_input)
    print(f"Key Generated: {key.fingerprint}")

    filename = './msg.txt'

    # Encrypt file
    with open(filename, 'rb') as f:
        status = gpg.encrypt_file(
            f,
            recipients=["user@example.com"],
            output=filename + ".gpg",
            always_trust=True
        )
    print(f"Encryption Status: {status.status}")

    # Sign file (detached signature)
    with open(filename, 'rb') as f:
        signed_data = gpg.sign_file(
            f,
            keyid=key.fingerprint,
            passphrase="secure_password",
            detach=True
        )

    with open("msg.sig", "w") as sig_file:
        sig_file.write(str(signed_data))

    print("Digital signature created:", str(signed_data))

    # Decrypt file
    with open(filename + ".gpg", 'rb') as f:
        decrypted_data = gpg.decrypt_file(
            f,
            passphrase="secure_password"
        )

    # Verify signature
    with open("msg.sig", "rb") as sig_f:
        verified = gpg.verify_file(sig_f, filename)

    print(f"Decrypted Message: {decrypted_data.data.decode()}\n")
    print(f"Signature Verified: {verified.valid}")


if __name__ == "__main__":
    demonstrate_pgp()
