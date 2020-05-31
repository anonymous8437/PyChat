import socket
import threading

s=socket.socket()

ip='localhost'
port=9999

s.bind((ip,port))
s.listen()
print('Wait for connection...')
c, addr=s.accept()
print('client added!')
def send():
    while True:
        msg = input("\nYour message>>>")
        c.send(msg.encode())
def recv():
    while True:
        print("\nclient message>>>"+c.recv(1024).decode())

send = threading.Thread(target=send).start()
recv = threading.Thread(target=recv).start()