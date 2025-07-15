
# Name: Rachel Wilbanks
# Language: Python
# Program Name: client.py
# Finish Date: 6/15/2025
#
# Purpose: The purpose of this program is meant to send an
#          encrypted message, over TCP connection, to a server.
#          This is done by using AES-GCM for encryption with a
#          key that is already shared between client and server.
#          A piece of plaintext is encrypted (by the client)
#          (using an IV.
#          Lastly, both the ciphertext and IV are sent to the
#          server.
#
#          In a nutshell, the goal of this is to send IV and
#          ciphertext (made from plaintext) to a/the server.
#

import socket       #Socket handles the TCP connection (I believe)
import os           #Used to generate random bytes (IV)

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = b'\x01' * 32


Plaintext = b"Test Plaintext"


print(f"Client:)     Plaintext: {Plaintext.decode()}")

aesgcm = AESGCM(key)

IV = os.urandom(12)

Ciphertext = aesgcm.encrypt(IV, Plaintext, None)

print(f"Client:)     IV (hex): {IV.hex()}")
print(f"Client:)     Ciphertext (hex): {Ciphertext.hex()}")

# Create TCP socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 5432))

    s.sendall(IV + Ciphertext)

    print("Client:)     The data was successfully sent!")
    #^Confirm that data was sent





