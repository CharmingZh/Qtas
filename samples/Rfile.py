# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Rfile.py
# @Github  ：https://github.com/CharmingZh

import os
import socket


def re(sock: socket):
    sock.bind()


def cd(args: list):
    if not args:
        # 没有 args 直接返回根目录，retHandle 情况 2
        print("♻️ Back to the root dir")
        return 2
    else:
        args_str = args[0]

    check = os.getcwd()
    check = check.split("/")

    if check[-1] == "Storage" and args_str == '..' \
            or args_str[0] == '.' and args_str[1] == '.' and check[-1] == "Storage":
        # 不可以访问根目录上层，retHandle 情况 0，除提示外不做任何操作
        print("❌ ERROR : You are already in the root dir!")
        return 0

    # print("cd():", args_str)
    try:
        os.chdir(args_str)
    except FileNotFoundError:
        print('Sorry! We don\'t find', args_str, '.')
    # 需要更改 cli 现实的当前工作目录
    return 1


def pwd():
    path = os.getcwd()
    return path


def tree(path, layer=0):
    try:
        listdir = os.listdir(path)
    except Exception as e:
        print(e)
        return 0
    for index, file in enumerate(listdir):
        file_path = os.path.join(path, file)
        print("      |    " * (layer - 1), end="")
        if layer > 0:
            print("      `----" if index == len(listdir) - 1 else "      |----", end="")
        if file[0] != '.':
            print("  ", file)
        if os.path.isdir(file_path):
            tree(file_path, layer + 1)

def ls():
    listdir = os.listdir('.')
    print(listdir)