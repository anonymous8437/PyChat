import socket
import threading

s=socket.socket()
ip='localhost'
port=9999
s.connect((ip,port))
print('''Connected!
please wait for server message...''')
def send():
    while True:
        msg=input("\nYour message>>>")
        s.send(msg.encode())
def recv():
    while True:
        print("\nserver message>>> "+s.recv(1024).decode())

send = threading.Thread(target=send).start()
recv = threading.Thread(target=recv).start()