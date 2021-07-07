import socket

# Servidor UDP (Executar como Admin)

host = "127.0.0.1"
port = 20001
buffer = 1024
message = "Hello UDP Client!"
bytes_to_send = str.encode(message)

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind((host, port))
print("UDP Server UP and Listening!")

while(True):
    bytes_address_pair = udp_socket.recvfrom(buffer)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]
    client_msg = "Message from Client: {}".format(message)
    client_ip  = "Client IP Address: {}".format(address) 
    print(client_msg)
    print(client_ip)
    udp_socket.sendto(bytes_to_send, address)