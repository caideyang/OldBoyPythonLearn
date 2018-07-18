#encoding:utf-8

import socket

client = socket.socket()
client.connect(('127.0.0.1',9999))
while True:
    cmd = input(">>>").strip()
    if not cmd:
        continue
    client.send(cmd.encode("utf-8"))
    res_len = client.recv(1024)
    client.send(b"Ok")
    print("数据长度是",res_len)
    print(".......................")
    # print(int(res_len.decode()))
    receive_size = 0
    receive_data = b""
    while receive_size < int(res_len.decode()):
        data = client.recv(1024)
        print(data.decode())
        receive_size += len(data)
        #print(receive_size)
        receive_data += data
    #else:
        #print(receive_data.decode())
