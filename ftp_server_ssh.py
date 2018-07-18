#encoding:utf-8

import  socket,os,time
import hashlib
server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
server.bind(('0.0.0.0',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print("New Connect : ",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        method,filename = data.decode().split()
        if method == "get":#如果是下载命令，则判断filename是否存在
            if os.path.isfile(filename):
                file_size = os.stat(filename).st_size #获取文件大小
                f = open(filename,'rb')
                conn.send(str(file_size).encode())#发送文件大小
                client_ack = conn.recv(1024) #等待客户端确认,防止粘包
                m = hashlib.md5()
                for line in f:
                    m.update(line)
                    conn.send(line)
                print(m.hexdigest())
            print("send done")
server.close()

