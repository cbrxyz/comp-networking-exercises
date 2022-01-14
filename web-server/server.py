import socket
import sys

# Relevant values
SERVER_PORT = 33867

# Prepare the web server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', SERVER_PORT))
server_socket.listen(3)
print("Socket is listening and can be found at {}.".format(server_socket.getsockname()))

while True:
    connection_socket, addr = server_socket.accept()
    print("Received connection from {} on port {}.".format(addr[0], addr[1]))

    # Attempt to retrieve requested file
    file_name = connection_socket.recv(1024).split()[1]
    file_name = file_name.decode('UTF-8')[1:]
    print("Attempting to retrieve {}...".format(file_name))

    try:
        # TODO
        pass

    except IOError:
        # Send response message for file not found
        # TODO
        pass

    # Terminate server after sending data
    server_socket.close()
    sys.exit()
