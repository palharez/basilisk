from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

BLOCK_SIZE = AES.block_size


class Cipher:
    def __init__(self, key):
        self.key = self.adjust_key(key)

    def pad(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")

        padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def unpad(self, data):
        padding_len = data[-1]
        return data[:-padding_len]

    def adjust_key(self, key_str, key_sizes=(16, 24, 32)):
        key_bytes = hashlib.sha256(key_str.encode("utf-8")).digest()

        for size in key_sizes:
            if len(key_bytes) == size:
                return key_bytes
            elif len(key_bytes) < size:
                return key_bytes.ljust(size, b"\0")

        return key_bytes[: max(key_sizes)]

    def create_aes_cipher(self, iv):
        return AES.new(self.key, AES.MODE_CBC, iv)

    def encrypt(self, plaintext: str) -> str:
        iv = get_random_bytes(BLOCK_SIZE)

        cipher = self.create_aes_cipher(iv)

        padded_plaintext = self.pad(plaintext)
        ciphertext = cipher.encrypt(padded_plaintext)

        return (iv + ciphertext).hex()

    def decrypt(self, ciphertext: str) -> str:
        if isinstance(ciphertext, str):
            ciphertext = bytes.fromhex(ciphertext)

        iv = ciphertext[:BLOCK_SIZE]
        encrypted_data = ciphertext[BLOCK_SIZE:]

        cipher = self.create_aes_cipher(iv)

        padded_plaintext = cipher.decrypt(encrypted_data)
        plaintext = self.unpad(padded_plaintext)

        return plaintext.decode("utf-8")
