# ==========================
# title: 温度转换的 Client端程序
# author: yjan1016
# date: 2023-01-21
# reference: 洪锦魁《Python王者归来（增强版）》
# IDE: Pycharm
# ==========================
import socket
host= "127.0.0.1" # 主机的域名
port = 2255                # 连接 port 编号
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 建立socket对象
mydata = input("请输入华氏温度: ")
s.sendto(mydata.encode(),(host,port))
print(f"摄氏温度: {s.recv(1024).decode()}")
s.close()