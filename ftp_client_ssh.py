#encoding:utf-8

import socket
import hashlib

client = socket.socket()
client.connect(('127.0.0.1',9999))
while True:
    cmd = input(">>>").strip()
    if not cmd:
        continue
    method,filename = cmd.split()
    if method == "get":
        client.send(cmd.encode())
    server_response = client.recv(1024) #获取文件大小
    client.send("Ready to receive file !".encode("utf-8")) #发送确认
    print("数据长度是",server_response)
    print(".......................")
    # print(int(res_len.decode()))
    received_size = 0
    filename += ".new"
    f = open(filename,'wb')
    m = hashlib.md5()
    while received_size < int(server_response.decode()):
        if int(server_response.decode()) - received_size > 1024:
            size = 1024
        else:
            size = int(server_response.decode()) - received_size
        data = client.recv(size)
        m.update(data)
        received_size += len(data)
        f.write(data)
        print(received_size , server_response.decode())
    else:
        print(m.hexdigest())
        f.close()
        print("Recv Done!")
