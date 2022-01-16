import socket
import sys

# Relevant values
SERVER_PORT = 33867
DEFAULT_FILE = "example.html"

# Prepare the web server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', SERVER_PORT))
server_socket.listen(3)
sock_name = server_socket.getsockname()
print("Socket is listening and can be found at http://{}:{}.".format(sock_name[0], sock_name[1]))

while True:
    connection_socket, addr = server_socket.accept()
    print("Received connection from {} on port {}.".format(addr[0], addr[1]))

    # Attempt to retrieve requested file
    file_name = connection_socket.recv(1024).split()[1] 
    file_name = file_name.decode('UTF-8')[1:]
    if not len(file_name):
        file_name = DEFAULT_FILE
    print("Attempting to retrieve {}...".format(file_name))

    try:
        # Attempt to retrieve the file and send it to the user
        file = open(file_name)
        content = file.read()

        # Send the HTTP header
        connection_socket.send("HTTP/1.1 200 OK\n\n".encode())
        
        # Send the file contents line by line
        connection_socket.send(content.encode())

        # End HTTP response
        connection_socket.send("\r\n".encode())

        pass

    except IOError:
        # Send response message for file not found
        # TODO
        pass

    # Terminate server after sending data
    server_socket.close()
    sys.exit()
