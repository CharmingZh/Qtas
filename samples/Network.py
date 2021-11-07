# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Network.py
# @Github  ：https://github.com/CharmingZh

import time
from socket import *
import threading
import random
import os

# import Cepher
# from settings import SIZE

BUFSIZE = 10


def curNetInfo(sock: socket, version=4):
    if version == 4:
        print('current IP address is : ', sock[4][0])
        print('cureent PORT using is : ', sock[4][1])
    return sock[4][0], sock[4][1]


def get_ip(version=4):
    """
        Get the IP addr of the client
    """
    if version == 4:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('1.1.1.1', 80))
        IP = s.getsockname()[0]
        s.close()
        # return socket.gethostbyname(socket.gethostname()) # some times return 127.*
        return IP
    elif version == 6:
        print('version == 6, todo')
        # to do
    else:
        print("version type wrong")


def gen_port(num=1):
    """
        Generate a port number or a list
    """
    ports_list = [random.randrange(10000, 60000) for x in range(num)]
    if num == 1:
        # s.bind((Network.get_ip(4), 0)) is enough
        return ports_list[0]
    else:
        return ports_list


def gen_port_file():
    port_pool = gen_port(100)
    fwrite = open("data/.port_list", "w")
    for item in port_pool:
        fwrite.write('N' + str(item) + "\r\n")
        # 第一位为 N 为未使用端口，Y 为已占用端口
    fwrite.close()


def get_port():
    port_list = []
    file = open("data/.port_list", "r")
    for port in file.readlines():
        print(port)
        port = port[:-1]
        print(port)
        port_list.append(port)
    file.close()
    return port_list


def test():
    print()


class Server(threading.Thread):
    def __init__(self, port, version):
        """ 创建一个 socket """
        threading.Thread.__init__(self)
        self.setDaemon(True)  # 守护线程
        self.address = (get_ip(version), port)
        if version == 4:
            # self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock = socket(AF_INET, SOCK_STREAM)
        elif version == 6:
            self.sock = socket(AF_INET6, SOCK_STREAM)
        print("server socket get")

    def __del__(self):
        self.sock.close()
        print("server socket close")
        # to do

    def run(self):
        print("server start ...")
        self.sock.bind(self.address)
        print("server bind")
        self.sock.listen(5)
        print('server listen')
        conn, addr = self.sock.accept()
        print("remote client success connected ...")
        while True:
            data = conn.recv(BUFSIZE)
            print('Server recv:', data.decode("utf-8"))
            if not data:
                break
            file_name = data.decode('utf-8')
            if os.path.exists(file_name):
                file_size = str(os.path.getsize(file_name))
                print("Server file size of", file_name, "is ", file_size)
                conn.send(file_size.encode())
                data = conn.recv(BUFSIZE)
                print("server start trans")
                f = open(file_name, "rb")
                for line in f:
                    conn.send(line)
                f.close()
            else:
                conn.send("0001".encode())

        # to do


class Client(threading.Thread):
    def __init__(self, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.address = (get_ip(version), port)
        if version == 4:
            self.sock = socket(AF_INET, SOCK_STREAM)
        elif version == 6:
            self.sock = socket(AF_INET6, SOCK_STREAM)

    def __del__(self):
        self.sock.close()
        print('client socket close')
        self.file.close()
        print('client file close')
        # to do

    def run(self):
        print("client start ...")
        while True:
            try:
                self.sock.connect(self.address)
                break
            except:
                # 连接失败时，三秒后重新尝试连接
                count = 3
                while count >= 0:
                    print("      reconnect in ", count, "seconds")
                    time.sleep(1)
                    count -= 1
                    continue
        print("client success connected")
        timer = 100
        while timer >= 0:
            print("test", timer, "seconds")
            timer -= 1
            time.sleep(1)
        # to do
    # to do


if __name__ == '__main__':
    print(get_ip())
