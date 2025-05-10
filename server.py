import socket
import threading

HEADER = 64 #length of the first meassage
PORT = 5050
#this is the ip of the device locally
SERVER_IP = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISSCONNECT = 'kosomk'
print(SERVER_IP)

server = socket.socket(family=socket.AF_INET ,type=socket.SOCK_STREAM)
ADDR = (SERVER_IP,PORT)
server.bind(ADDR)
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    m = 'you connected' + str(addr)
    conn.send(m.encode('utf-8'))
    while True:
        raw_header = conn.recv(HEADER)
        if not raw_header:
            break
        try:
            msg_len = int(raw_header.decode(FORMAT).strip())
        except ValueError:
            print(f"[ERROR] Bad header from {addr}: {raw_header!r}")
            break

        data = bytearray()
        while len(data) < msg_len:
            packet = conn.recv(msg_len - len(data))
            if not packet:
                break  # client dropped
            data.extend(packet)

        msg = data.decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg == DISSCONNECT:
            break

    conn.close()
    print(f"[DISCONNECTED] {addr}")

print("started")
server.listen()
print(f"[LISTENING] on {SERVER_IP}:{PORT}")
try:
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
except KeyboardInterrupt:
    print("\n[SHUTTING DOWN] Closing server socket.")
    server.close()

