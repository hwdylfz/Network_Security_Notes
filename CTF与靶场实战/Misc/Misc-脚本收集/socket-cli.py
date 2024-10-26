#coding:utf-8
from socket import *
print("=====================TCP客户端v1.0=====================");
HOST = '172.16.18.86'  #服务器ip地址
PORT = 32864  #通信端口号
BUFSIZ = 1024  #接收数据缓冲大小
ADDR = (HOST, PORT)
print("向客户端 %s 通过 %d 端口尝试发起连接...."%(HOST,PORT))
tcpCli = socket(AF_INET, SOCK_STREAM)  #创建客户端套接字
tcpCli.connect(ADDR)  #发起TCP连接
while True:
    print("连接成功，请输入需要传输的数据(报文)中...")
    data = input('>')#接收用户输入
    if not data:
        data = "GET / HTTP/1.1\r\n<html><body><h1>Host: locallhost\r\nBaby,it's me,open the door!</h1></body></html>\r\n"#若无输入，则发送默认报文
        break
    tcpCli.send(bytes(data,'utf-8'))  # 客户端发送消息，发送字节数组
    while True:
        break
    data = tcpCli.recv(BUFSIZ)   #接收回应消息，接收到的是字节数组
    if not data:   #如果接收服务器信息失败，或没有消息回应
        break
    print(data.decode('utf-8'))  #打印回应消息，或者str(data,"utf-8")
tcpCli.close() #关闭客户端socket