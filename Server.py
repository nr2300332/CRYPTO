# server.py - Legacy Bank mainframe: receive, decrypt and print the transaction
import socket
from DES import KEY, decrypt, hex_to_text

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allow quick restart
server.bind(("127.0.0.1", 5000))
server.listen(1)
print("Server is waiting on port 5000 ...")

conn, addr = server.accept()
print("Client connected:", addr)

cipher_bytes = conn.recv(4096)
print("Received ciphertext (bytes):", cipher_bytes)

cipher_hex = cipher_bytes.hex().upper()
plain_hex = decrypt(cipher_hex, KEY)
print("Decrypted (hex):    ", plain_hex)
print("Transaction:        ", hex_to_text(plain_hex))

conn.send("Transaction received".encode())
conn.close()
server.close()