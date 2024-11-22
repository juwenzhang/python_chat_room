import socket
import threading

# basic ipv4 create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ip address
server.bind(("0.0.0.0", 8888))

# listen ip address
server.listen()

print("server is begun!!!")

# accept link
# conn, addr = server.accept()

client_socket = {}

def handler_socket(conn):
    try:
        username = conn.recv(1024 * 4).decode()
        client_socket[conn] = username

        for client in client_socket.keys():
            client.send((f"【{username}】加入群聊").encode())

        while True:
            # receive client message
            data =  conn.recv(1024 * 4)

            send_to_many_people = data.decode()

            if send_to_many_people.startwith("@"):
                msg = send_to_many_people.split(" ")
                private_name = msg[0][1:]
                for k, v in client_socket:
                    if v == private_name:
                        k.send(f"【{username}】>>>{send_to_many_people}".encode())

            else:
                if len(client_socket) > 0:
                    for client in client_socket:
                        client.send(f"【{username}】>>>{send_to_many_people}".encode())

            # if data == "886":
            #     break

            # show message from client
            print(data.decode())

            # server_data = input(">>>")

            # server leave message to client
            # conn.send(server_data.encode())
    except Exception as e:
        client_socket.pop(conn)
        for client in client_socket.keys():
            client.send(f"【{username}】已经退出群聊...".encode())

while True:
    # accept many client link
    conn, addr = server.accept()
    # client_socket.append(conn)
    conn.send("情输入你的昵称".encode())
    client_thread = threading.Thread(target=handler_socket, args=(conn,))
    client_thread.start()

# close link
# server.close()
# conn.close()