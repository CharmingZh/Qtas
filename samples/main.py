# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: main.py
# @Github  ：https://github.com/CharmingZh

# ============================================================================
#    System library
# ============================================================================
import select
import threading
from threading import Lock, Thread
import time
import os

# ============================================================================
#    project implemented
# ============================================================================
from Interface import *
from Vfile import *
import Cepher
from Network import *
import Rfile

# ============================================================================
#    Global Variations
# ============================================================================
USERNAME = 'Default'
CONNSTAT = {
    0: 'Online',
    1: 'Offline'
}
CURPATH = os.getcwd()
PROJPATH = CURPATH
CURPATH = os.getcwd() + '/samples/data/Storage'

CONN_LIST = []

# ============================================================================
#   Initiation objects
# ============================================================================
sock = socket(AF_INET, SOCK_STREAM)
sock.setblocking(False)  # 设置为非阻塞
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置可以重复使.绑定的信息
addr = (get_ip(4), 23180)
# addr = ('127.0.0.1', 23180)
sock.bind(addr)

def listenImpletement(sock:socket, num: int):
    sock.listen(num)
    print("Listening ...")

thread_servListen = threading.Thread(target=listenImpletement, args=(sock, 5))  # 启动一个监听，随时响应客户请求
# thread_servListen = threading.Thread(target=sock.listen, args=(5,))  # 启动一个监听，随时响应客户请求

"""
# attempt 4
def servAccept():
    while 1:
        infds, outfds, errfds = select.select([sock, ], [], [], 5)
        # 如果infds状态改变,进行处理,否则不予理会
        if len(infds) != 0:
            clientsock, clientaddr = sock.accept()
            infds_c, outfds_c, errfds_c = select.select([clientsock, ], [], [], 3)
            if len(infds_c) != 0:
                buf = clientsock.recv(8196)
                if len(buf) != 0:
                    print(buf)
            clientsock.close()
            print("clientsock closed")
        print("no data coming")
        # attempt 3
    try:
        print('servAccept start')
        r_conn, r_addr = sock.accept()  # 被动接受TCP客户的连接，等待连接的到来，收不到时会报异常
        print('connect by ', addr)
        CONN_LIST.append(r_conn)
        r_conn.setblocking(False)  # 设置非阻塞
        print('set no blocking')
    except BlockingIOError as e:
        print(e)
        pass
    # attempt 2nd
    tmp_list = [conn for conn in CONN_LIST]
    for conn in tmp_list:
        try:
            data = conn.recv(1024)  # 接收数据1024字节
            if data:
                print('收到的数据是{}'.format(data.decode()))
                conn.send(data)
            else:
                print('close conn', conn)
                conn.close()
                CONN_LIST.remove(conn)
                print('还有客户端=>', len(CONN_LIST))
        except IOError:
            pass
    """


# thread_servAccept = threading.Thread(target=servAccept)


# ============================================================================
#   functions definition
# ============================================================================

def retHandle(retVal: int):
    if retVal == 1:
        global CURPATH
        CURPATH = os.getcwd()
        return 0
    elif retVal == 2:
        global PROJPATH
        # print("retVAl = 2 handle")
        os.chdir(PROJPATH + '/samples/data/Storage')
        return 1


def showNet():
    print(addr)


if __name__ == '__main__':
    print("Qtas launching ... ")
    """
        Server socket keep listening in a 
        new thread for download purposes.
    """
    os.chdir(CURPATH)
    thread_servListen.setDaemon(True)  # Main thread exit after all thread terminated
    # thread_servAccept.setDaemon(True)

    thread_servListen.start()
    # thread_servAccept.start()

    system_thread = []  # System maintaining thread list

    system_thread.append(thread_servListen)
    # system_thread.append(thread_servAccept)

    time.sleep(0.2318)  # Love you, my little shelley, 0623 1018 forever❤️

    thread_servListen.join()
    # thread_servAccept.join()

    # cli = Cli(CONNSTAT[0], USERNAME, CURPATH)
    cli = Cli()
    log = Log(PROJPATH)

    cli.printLogo()
    cli.cliHelp(all)

    # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # s.connect()
    while True:

        oper, opt, args = cli.cliPrompt(CONNSTAT[0], USERNAME, CURPATH)
        log.writeHistory(oper)
        retVal = cli.opSelect(oper, opt, args)
        conn, Raddr = sock.accept()
        while retVal != 0:
            retVal = retHandle(retVal)
        showNet()
        cli.pathShade(CURPATH)
