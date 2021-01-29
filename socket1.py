import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Make a phone/Make a file
# Sockets kind of function like files!!!!!!
# But you can send and receive files via this file
# Creating a socket(creating a file that is inside your computer)
mysock.connect(('data.pr4e.org', 80)) # Dial via your phone to a server, this is the call
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


print(f"cmd encoded is: {cmd}\n\n\n")

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=' ')

mysock.close()
