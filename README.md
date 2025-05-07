# SecureFileTransfer-# SecureFileTransfer

A basic client-server system for securely transferring files using AES-256 encryption and ensuring file integrity using SHA-256 checksums.

## Use-Case: Secure File Sharing

This project demonstrates how to securely transfer a file (e.g., PDF or ZIP file) over a network. The file is encrypted using AES-256, and its integrity is verified using SHA-256.

## Prerequisites

- Python 3.x
- PyCryptodome library (Install using `pip install pycryptodome`)

## Files

- `client.py`: Client script for reading, encrypting, and sending a file over a network.
- `server.py`: Server script for receiving the encrypted file, decrypting it, and verifying its hash.
- `utils.py`: (Optional) Contains AES encryption and checksum verification functions.

## How It Works

1. The client reads a file, encrypts it using AES-256 encryption.
2. The client sends the encrypted file and its checksum to the server.
3. The server receives the file, decrypts it, and verifies the integrity using SHA-256 checksum.
4. If the checksum matches, the file is successfully transferred.

## Running the Project

1. Start the server:
   ```bash
   python server.py
