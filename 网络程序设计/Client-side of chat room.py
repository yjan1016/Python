# ==========================
# title: 聊天室的 Client端程序
# author: yjan1016
# date: 2023-01-21
# reference: 洪锦魁《Python王者归来（增强版）》
# IDE: Pycharm
# ==========================
import socket
host= socket.gethostname() # 主机的域名
port = 2255                # 连接 port 编号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 建立socket对象
s.connect((host,port)) # 绑定 IP 和 port
print("Client端已经联机")
msg = ''
# 输入 bye 可以结束联机
while msg != "bye":
    mydata = input("输入传送内容: ")  # 读取输入内容
    s.send(mydata.encode())          # 编码为 bytes 后输出
    if msg == "bye":
        break
    print("Client端: waiting...")
    msg = s.recv(1024).decode()      # 读取输入内容
    print(f"显示收到内容: {msg}")     # 输出Server讯息
s.close()