# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Rfile.py
# @Github  ：https://github.com/CharmingZh

import errno
import os
import time


class Log:
    """
        Log class includes three features:
            1. user's(client) operation history would write into a file
            2. Error check system check
            3. System stability required
    """
    def __init__(self, path:str):
        self.Path = path

    def writeHistory(self, cmd_str):
        date_full = self.getTime()
        date = date_full[:10]
        path = self.Path + "/samples/.log/"
        path = path + date
        file = open(path, "a+")
        str = self.getTime() + " Operation: " + cmd_str + '\n'
        # str = ".test writeHistory()"
        file.write(str)
        file.close()

    def getTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    log = Log()
