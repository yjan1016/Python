# ==========================
# title: 温度转换的 Server端程序
# author: yjan1016
# date: 2023-01-21
# reference: 洪锦魁《Python王者归来（增强版）》
# IDE: Pycharm
# ==========================
import socket
host= "127.0.0.1" # 主机的域名
port = 2255                # 连接 port 编号
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 建立socket对象
s.bind((host,port)) # 绑定 IP 和 port
print("Server端: 绑定完成, waiting...")
f, addr = s.recvfrom(1024)  # 被动接收客户数据
print(f"received from {addr}")
c = f.decode()
c = (float(c)-32)*5/9
mydata = str(c)
s.sendto(mydata.encode(),addr)
s.close()