# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Rfile.py
# @Github  ：https://github.com/CharmingZh

"""
    System library
"""
import socket
import threading
from threading import Lock, Thread
import time
import os

'''
    project implemented
'''
from Interface import *
from Vfile import *
import Cepher

if __name__ == '__main__':
    """
    t1 = threading.Thread(target=run, args=('t1', ))
    t2 = threading.Thread(target=run, args=('t2', ))
    t1.start()
    t2.start()
    """
    cli = Cli()
    cli.printLogo()
    cli.cliHelp(all)
    # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # s.connect()
    while True:
        oper, opt, args = cli.cliPrompt()
        cli.opSelect(oper, opt, args)

