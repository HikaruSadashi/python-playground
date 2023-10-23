import socket
import time

# Server address and port
server_address = ('localhost', 12000)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initialize the sequence number
sequence_number = 1

# Number of pings to send
total_pings = 10

# Set timeout for socket operations to 1 second
client_socket.settimeout(1.0)

for i in range(1, total_pings + 1):
    # Prepare the message
    message = f'Ping {sequence_number} {time.time()}'
    
    try:
        # Send the message to the server
        client_socket.sendto(message.encode(), server_address)
        
        # Start the timer to calculate round trip time
        start_time = time.time()
        
        # Receive the response from the server
        response, server_address = client_socket.recvfrom(1024)
        
        # Calculate round trip time
        end_time = time.time()
        rtt = end_time - start_time
        
        print(f'Response from {server_address}: {response.decode()}')
        print(f'Round Trip Time: {rtt} seconds')
    except socket.timeout:
        # Handle timeout
        print('Request timed out')
    
    # Increment the sequence number
    sequence_number += 1

# Close the socket
client_socket.close()