import socket

# Import the socket module to create network connections

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket

# Specify the network interface (host) and port for the server to listen on
host = socket.gethostbyname("localhost")  # Get the local host name
port = 444

# Bind the socket to the specified host and port
serversocket.bind((host, port))

# Set the maximum number of pending connections in the queue
serversocket.listen(3)

# Continuously accept incoming client connections
while True:
    # Accept a connection from a client and receive the client's address
    clientsocket, address = serversocket.accept()

    # Print a message indicating that a connection has been established
    print("Received connection from: %s" % str(address))

    # Prepare a welcome message for the client
    message = "You are connected to the server. This is an example of how sockets can be used! \r\n"

    # Encode the message in ASCII format for transmission
    encoded_message = message.encode('ascii')

    # Send the welcome message to the client
    clientsocket.sendall(encoded_message)

    # Close the communication socket with the client
    clientsocket.close()
