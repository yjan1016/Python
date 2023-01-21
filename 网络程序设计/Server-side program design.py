"""
cmd查询本机地址：
1、win+R
2、cmd enter
3、ipconfig -all
"""
# Server端程序设计
"""
author: yjan1016
date: 2023-01-21
reference: 洪锦魁《Python王者归来（增强版）》
IDE: Pycharm
"""
import socket
host="127.0.0.1" # 127.0.0.1是回送地址, 它引用本地计算机。作用：供测试使用。
# 用 IPv4 地址，可
# 用 DNS 服务器 ，报错：OSError: [WinError 10049] 在其上下文中，该请求的地址无效。
# 用 IPv6 地址，报错：socket.gaierror: [Errno 11001] getaddrinfo failed
port = 2255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print(f"Server在{host}:{port}")
print("waiting for connection...")
while True:
    conn, addr = s.accept()
    print(f"目前联机网址{addr}")
    data = conn.recv(1024)
    print(data)
    conn.sendall(b"HTTP/1.1 200 OK \r\n\r\n Welcome to Deepmind")
    # 网页上显示 Welcome to Deepmind
    conn.close()
    
