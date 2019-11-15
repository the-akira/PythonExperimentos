import socket

# Rodar com python3

def Main():
	host = '127.0.0.1'
	port = 556

	server = ('127.0.0.1', 555)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	s.bind((host,port))

	message = input("-> ")
	while message != 'q':
		s.sendto(message.encode('utf-8'), server)
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print("Received from server: "+data)
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()