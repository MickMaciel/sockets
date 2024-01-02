import socket

# Create a TCP socket for the client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the hostname and port of the server
host = "localhost"  # replace with the actual server's hostname or IP address
port =  9999            # choose the port

# Connect the client socket to the server
clientsocket.connect((host, port))

# Prepare a message for the server
message = b"Hello from client"

# Encode the message in binary format for transmission
encoded_message = message

# Send the message to the server
clientsocket.sendall(encoded_message)

# Receive the server's response
response = clientsocket.recv(1024)

# Decode the response from binary to ASCII format
decoded_response = response.decode('ascii')

# Print the server's response
print(decoded_response)

# Close the connection with the server
clientsocket.close()
