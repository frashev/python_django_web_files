from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5) # the number of calls in the queue that server can handle
        while(1):

            (clientsocket, address) = serversocket.accept() # blocking.... wait for the phone call

            # Runs when a phone call is received
            # The server knows that the client must speak first!!!!
            rd = clientsocket.recv(5000).decode() # Its UNICODE in python
            pieces = rd.split("\n")
            if (len(pieces) > 0): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            # The client needs to cancel the connection
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()