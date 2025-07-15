
# Name: Rachel Wilbanks
# Language: Python
# Program Name: server.py
# Finish Date: 6/15/2025
#
# Purpose: The purpose of this program is meant to decrypt an
#          encrypted message delivered through a TCP connection.
#          This is done by using AES-GCM for decryption with a
#          key that is already shared between client and server.
#          The program waits for a response from client
#          (waits for a connection between the two), then receives
#          IV and ciphertext from "client.py". After receiving it,
#          it decrypts it.
#
#          In a nutshell, the goal is to receive and decrypt/decode
#          text/a message sent by a client.
#
#


import socket       #Socket handles the TCP connection (I believe)
import os           #Used to generate random bytes (IV)

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
#^For AES Encryption

# Same pre-shared key as client
key = b'\x01' * 32


IV_SIZE = 12

# Setup the TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 5432))

    s.listen(1)
    print("Server:)     Waiting for a connection...")

    connection, address = s.accept()

    with connection:
        print(f"Server:)     Is connected by {address}")
        data = connection.recv(1024)

        IV = data[:IV_SIZE]
        ciphertext = data[IV_SIZE:]


        print(f"Server:)     IV (hex): {IV.hex()}")
        print(f"Server:)     Ciphertext (hex): {ciphertext.hex()}")


        aesgcm = AESGCM(key)
        try:
            decryptedText = aesgcm.decrypt(IV, ciphertext, None)
            print(f"Server:)     Decrypted Message is: {decryptedText.decode()}")
        except Exception as e:
            print(f"Server:)     Decryption failed: {e}")





