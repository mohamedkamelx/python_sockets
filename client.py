import socket
import threading
HEADER = 64 #leangth of the first meassage
PORT = 5050
#this is the ip of the device locally
SERVER_IP = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISSCONNECT = 'kosomk'


ADDR = (SERVER_IP,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def recieve():
    pass

massage = ''
client.connect(ADDR)
while not massage:
    massage = client.recv(64)
    if not massage:
        break
    massage=massage.decode('utf-8')
    print(massage)
    
def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    payload_len = str(msg_len).encode(FORMAT)
    payload_len += b' ' * (HEADER - len(payload_len))
    client.send(payload_len)
    client.send(message)

x='j'

t1 = threading.Thread(target=recieve,daemon=True)

while x:
    x=input()
    send(x)