import socket
import sys

# Prepare the web server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO

while True:
    # Establish connection
    print("Ready to serve...")

    # Attempt to retrieve requested file
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
