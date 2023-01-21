# ==========================
# title: 聊天室的 Server端程序
# author: yjan1016
# date: 2023-01-21
# reference: 洪锦魁《Python王者归来（增强版）》
# IDE: Pycharm
# ==========================
import socket
host= socket.gethostname() # 主机的域名
port = 2255                # 连接 port 编号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 建立socket对象
s.bind((host,port)) # 绑定 IP 和 port
s.listen()          # TCP 监听
print("Server端: waiting...")
conn, addr = s.accept() # 被动接收客户联机
print("Server端已经联机")
msg = conn.recv(1024).decode()
# 输入 bye 可以结束联机
while msg != "bye":
    if msg:
        print(f"显示收到内容: {msg}") # 输出 Client 信息
    mydata = input("输入传送内容: ")  # 读取输入内容
    conn.send(mydata.encode())       # 编码为 bytes 后输出
    if msg == "bye":
        break
    print("Server端: waiting...")
    msg = conn.recv(1024).decode()   # 读取输入内容
conn.close()                     # 关闭联机
s.close()
"""
一开始正常后来报错：
Traceback (most recent call last):
  File "D:/coding/untitled/Server-side of chat room.py", line 23, in <module>
    conn.send(mydata.encode())       # 编码为 bytes 后输出
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
原因：conn.close() 缩进错误
"""