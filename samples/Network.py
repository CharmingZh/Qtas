import time
from socket import *
import threading
import random


# import Cepher
# from settings import SIZE



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


def get_ip(version=4):
    """
        Get the IP addr of the client
    """
    if version == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('1.1.1.1', 80))
        IP = s.getsockname()[0]
        print('1', s.getsockname()[1])
        s.close()
        print('socket has closed')
        # return socket.gethostbyname(socket.gethostname()) # some times return 127.*
        return IP
    elif version == 6:
        print('version == 6, todo')
        # to do
    else:
        print("version type wrong")


class Server(threading.Thread):
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
        # to do

    def run(self):
        print("server start ...")
        self.sock.bind(self.address)
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        print("remote client success connected ...")
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
        # to do

    def __del__(self):
        self.sock.close()
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
    ip = get_ip()
    print(ip)
    print("gen ports")
    print(gen_port(1))
    print(gen_port(10))
