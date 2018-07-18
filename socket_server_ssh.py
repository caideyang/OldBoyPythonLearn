#encoding:utf-8

import  socket,os,time

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
        print("执行指令",data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "Cmd has no output..."
        res_size = str(len(cmd_res))
        print(res_size)
        conn.send(res_size.encode("utf-8"))  #先发数据大小给客户端
        #time.sleep(0.5)
        client_ack = conn.recv(1024)#发送数据后等待客户端确认,防止粘包
        conn.send(cmd_res.encode("utf-8"))
server.close()

