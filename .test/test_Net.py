import socket
import os
import re


def get_ip(version = 4):
    if version == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('1.1.1.1', 80))
        IP = s.getsockname()[0]
        print('1', s.getsockname()[1])
        s.close()
        print('socket has closed')
        return IP
    elif version == 6:
        # print(socket.gethostname())
        ip = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)
        print(type(ip))
        for item in ip:
            print(type(item))
            print(item)
        # to do
    else:
        print("version type wrong")


if __name__ == '__main__':
    #ip = get_ip(4)
    #print(ip)
    get_ip(6)