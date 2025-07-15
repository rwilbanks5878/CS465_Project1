-----------------------------------------------------------------------

### Run requirements ###

- Python 3
- Python's cryptography library
-  ^(download the library with "pip install cryptography")

-----------------------------------------------------------------------

### Instructions ###

- Open 2 Terminal tabs
- cd (change directory) to the "CS465_Project1" folder 
-  ^(how you do this depends on where you have placed the folder)

- On one tab, start server by using "python3 server.py"

- On the 2nd tab, start client by using "python client.py"

-----------------------------------------------------------------------

### Key Exchange and Encryption ###

Key Exchange: 
A 32-byte (or 256-bit) AES key is coded on both the server and client.

Encryption Used:
-The method of encryption used is AES-GCM (256-bit).

-The client encrypts a predetermined plaintext, generates a 12-byte IV,
     and sends both the IV and encrypted plaintext (ciphertext) to the
     server.

-The server receives the encrypted text (ciphertext) and IV, then 
     decrypts it using a key and IV identical to the ones the client
     used ("aesgcm.decrypt(IV, ciphertext, None)" for server). 

-----------------------------------------------------------------------

