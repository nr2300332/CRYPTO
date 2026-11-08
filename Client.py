import socket
from DES import KEY, encrypt, text_to_hex

message = "Transfer 1500 EGP from 1001 to 4455"
plain_hex = text_to_hex(message)


print("Key:               ", KEY)
print("Plaintext (hex):   ", plain_hex)

cipher_bytes = bytes.fromhex(encrypt(plain_hex, KEY, show=True))
print("Ciphertext (bytes):", cipher_bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(("127.0.0.1", 5000))
except ConnectionRefusedError as exc:
    client.close()
    raise SystemExit("Could not connect to the server. Start Server.py first.") from exc

with client:
    client.sendall(cipher_bytes)
    print("Server says:", client.recv(1024).decode())