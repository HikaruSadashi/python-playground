import socket
import time

server_address = ('localhost', 12000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sequence_number = 1
total_pings = 10
client_socket.settimeout(1.0)

for i in range(1, total_pings + 1):
    message = f'Ping {sequence_number} {time.time()}'
    
    try:
        client_socket.sendto(message.encode(), server_address)
        start_time = time.time()
        response, server_address = client_socket.recvfrom(1024)
        end_time = time.time()
        rtt = end_time - start_time
        
        print(f'Response from {server_address}: {response.decode()}')
        print(f'Round Trip Time: {rtt} seconds')
    except socket.timeout:
        print('Request timed out')
    
    sequence_number += 1

client_socket.close()
