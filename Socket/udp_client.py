import socket

# Cliente UDP (Executar como Admin)

message = "Hello UDP Server!"
bytes_to_send = str.encode(message)
server_address_port = ("127.0.0.1", 20001)
buffer = 1024

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.sendto(bytes_to_send, server_address_port)
server_msg = udp_socket.recvfrom(buffer)
msg = "Message from Server: {}".format(server_msg[0])
print(msg)