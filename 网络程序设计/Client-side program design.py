# Client端程序设计
"""
author: yjan1016
date: 2023-01-21
reference: 洪锦魁《Python王者归来（增强版）》
IDE: Pycharm
"""
import socket
host="127.0.0.1" # 主机的 IP
port = 2255 # 连接 port 编号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 建立socket对象
s.connect((host,port)) # 绑定 IP 和 port
data = input("请输入数据: ")
s.send(data.encode())  # 转成 bytes 数据传送
# TCP/IP 的数据传送是使用 bytes 数据传送
receive_data = s.recv(1024).decode() # 接收所传来的数据同时解成字符串
print(f"接收数据{receive_data}")      # 打印接收的数据
s.close()            # 关闭 socket