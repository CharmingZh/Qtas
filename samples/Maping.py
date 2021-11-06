# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Rfile.py
# @Github  ：https://github.com/CharmingZh

import Cepher
import Network


class Chord_Node:
    """
        This is the Chord node implement
    """
    def __init__(self, IP, successor = None, prev = None):
        self.IP = Network.get_ip()
        # self.ID = self.genID()
        self.data = dict()
        self.prev = prev
        self.fingerTable = [successor]

    def myprint(self, msg):
        print(Cepher.cal_sha1(msg))
    # to do

class Chord_DHT:
    """
        DHT implement
    """
    print()
    # to do

if __name__ == '__main__':
    node = Chord_Node(1)
    print(node.IP)
    node.myprint(node.IP)
    print(type(Cepher.cal_sha1(node.IP)))