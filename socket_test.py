import socket
from config import HOST,PORT


print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
print(type(server_socket))
server_socket.listen(3)

client_socket, addr = server_socket.accept()

while True:

        try:

            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())


        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

	
        except KeyboardInterrupt as e:
            break

server_socket.close()
