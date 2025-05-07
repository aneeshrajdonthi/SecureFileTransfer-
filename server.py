import socket
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from utils import generate_checksum, decrypt_file

# Server details
SERVER_HOST = 'localhost'
SERVER_PORT = 5000

def server_receive_file():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive file name and checksum
    file_info = client_socket.recv(1024).decode()
    filename, checksum = file_info.split("\n")
    print(f"Receiving file: {filename}, expected checksum: {checksum}")

    # Receive the encrypted file data
    encrypted_data = client_socket.recv(1024*1024)  # Can adjust buffer size
    print(f"Encrypted file data received.")

    # Decrypt the file
    decrypted_data = decrypt_file(encrypted_data)

    # Verify the checksum of the decrypted data
    received_checksum = generate_checksum(decrypted_data)
    if received_checksum == checksum.strip():
        print("File integrity verified.")
        with open(f"received_{filename}", 'wb') as file:
            file.write(decrypted_data)
        print(f"File saved as received_{filename}")
    else:
        print("Checksum mismatch! File may be corrupted.")
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server_receive_file()
