from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import os

KEY = os.urandom(32)  # 256-bit key for AES-256

def generate_checksum(data):
    """Generate SHA-256 checksum of the file data."""
    return sha256(data).hexdigest()

def encrypt_file(file_data):
    """Encrypt the file data using AES-256."""
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(file_data, AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

def decrypt_file(encrypted_data):
    """Decrypt the file data using AES-256."""
    iv = encrypted_data[:16]
    ct_bytes = encrypted_data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return decrypted_data
