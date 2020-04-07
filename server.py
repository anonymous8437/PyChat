import socket

s=socket.socket()

ip='localhost'
port=9999

s.bind((ip,port))
s.listen()
print('Wait for connection...')
c, addr=s.accept()
print('client added!')
while True:
    msg=input("Your message >>>")
    c.send(msg.encode())
    print("client message >>>",c.recv(1024).decode())
