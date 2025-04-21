from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_text(text: str) -> str:
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_text(cipher: str) -> str:
    return cipher_suite.decrypt(cipher.encode()).decode()
