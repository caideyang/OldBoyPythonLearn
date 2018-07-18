#encoding:utf-8

import socket,os
server = socket.socket()
server.bind(('localhost',6969)) #绑定端口
server.listen() #监听



while True:
    conn, addr = server.accept()  # 等待连接
    # conn 就是客户端连过来而在服务端为其产生的一个连接实例
    print(addr)
    while True:
        data = conn.recv(8192)
        print("Recv: %s" % data.decode())
        if data.decode() == '':
            print("%s 端口的连接断开！" % addr[1])
            break
        conn.send(data.encode('utf-8'))
server.close()
