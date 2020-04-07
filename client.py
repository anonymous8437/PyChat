import socket

s=socket.socket()
ip='localhost'
port=9999
s.connect((ip,port))
print('''Connected!
please wait for server message...''')
while True:
    print('server message >>>',s.recv(1024).decode())
    msg=input("Your message >>>")
    s.send(msg.encode())
