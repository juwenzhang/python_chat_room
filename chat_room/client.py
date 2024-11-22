import socket
import threading

# basic ipv4 create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect server
client.connect(("127.0.0.1", 8888))


def receive_message(_client):
    while True:
        data = _client.recv(1024 * 4)
        print(data.decode())

def send_message(_client):
    while True:
        client_data = input()
        _client.send(client_data.encode())

# while True:
#     try:
        # client_data = input(">>>")
        #
        # # send message
        # client.send(client_data.encode())
        #
        # # get message from server
        # data =  client.recv(1024 * 4)
        #
        # if data == "886":
        #     break
        #
        # # show message
        # print(data.decode())


    # except ConnectionAbortedError:
        # break

# close client
# client.close()

threading.Thread(target=receive_message, args=(client,)).start()
threading.Thread(target=send_message, args=(client,)).start()