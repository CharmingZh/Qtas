# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 3:39 下午
# @Author  : Jiaming Zhang
# @FileName: Interface.py
# @Github  ：https://github.com/CharmingZh

import sys
from LogSys import Log
import Rfile
from Network import *


class Cli():
    """
        Class Cli include stuffs relating to menu stuff, user's interface looking ...
    """

    """
    def __init__(self, Stat: str, Name: str, Path: str):
        self.connStat = Stat
        self.usrName = Name
        self.curPath = Path
    """
    def printLogo(self):
        """
            just print a beautiful logo
        """
        print('    ___            _     _       ____ _        __    ')
        print('   /   \__ _ ___  (_)___| |_    /___ \ |_ __ _/ _\   ')
        print('  / /\ / _` / __| | / __| __|  //  / / __/ _` \ \    ')
        print(' / /_// (_| \__ \ | \__ \ |_  / \_/ /| |_ (_| |\ \   ')
        print('/___,\' \__,_|___/ |_|___/\__| \___,_\ \__\__,_\__/    ... is being started !\n')

    def cliHelp(self, cmd_type):
        """
            This func could print several possible helps to users
                1. "all" : mainly using in the welcome interface;
                2. "sp"  : to give specific optional args when using op wrongly
                3. to do
        """
        if cmd_type == 'all':
            print('usage: <operation> [optional] [arguments] ...')
            print('          ls :     to display all files in this directory')
            print('          pwd:     to show the currently using directory')
            print('          cd:      move to the wanted directory')
        elif cmd_type == "sp":
            print("❌ something seems going wrong")
            print("operation [optional] (arg_1) (arg_2)")
            # to do


    def pathShade(self, path: str):
        # 用户对 储存目录（Storage/[root]）以上的文件不可访问，不可见
        ret = 'root'
        path_list = path.split('/')
        count = 0
        for item in path_list:
            count += 1
            if item == 'Storage':
                break
        for i in (range(len(path_list) - count)):
            ret = ret + '/' + path_list[count + i]
        return ret

    def cliPrompt(self, Stat: str, Name: str, Path: str):
        """
            Display the prompt sign, and read the operation user typed in
            [Net state] < user's name > ( current working path ) >>> _type operation here_
        """
        # prompt_str = "[" + Stat + "] <" + Name + "> ( " + Path + " ) >>> "
        prompt_str_short = "\n👸 [" + Stat + "] <" + Name + "> ( " + self.pathShade(Path) + " ) >>> "
        # print(prompt_str_short)
        command_str = input(prompt_str_short)
        command_list = self.opRead(command_str)
        oper, opt, args = self.opSplit(command_list)
        # self.opShow(command_list)
        return oper, opt, args

    def opRead(self, opStdin):
        """
            Read an operation from stdin, delete all spaces
            retVal : opList : ['op1', 'op2', 'op3', ... ]
        """
        opList = opStdin.split(' ')
        count = 0
        for i in range(len(opList)):
            if opList[i] != '':
                count += 1
        if count == 0:
            print('No operation typed in')
            return 'help'
        retList = [' '] * count
        idx = 0
        for i in range(len(opList)):
            if opList[i] != '':
                retList[idx] = opList[i]
                idx += 1
        return retList

    def opSplit(self, opList):
        """
            Split the operation with:
                1. operation : Major Operation
                2. optional : Optional argument
                3. args : ['arg1', 'arg2', 'arg3', ... ]
        """
        operation = opList[0]
        optional = ['']
        args = ['']
        num = len(opList)
        if num != 1:
            i = 1
            if opList[1][0] == '-':
                optional = opList[1]
                i += 1
            else:
                optional.pop(0)
            for j in range(0, num - i):
                args.append(opList[i + j])
        else:
            optional.pop(0)
        args.pop(0)
        optional = optional[1:]
        return operation, optional, args

    def opShow(self, opList):
        """
            Display the correctly and splitted operation
        """
        op, opt, args = self.opSplit(opList)
        print('   The operations is: ', op)
        if opt == []:
            print('   ❌       None optional arg to show')
        else:
            print('   ✅       -->  optional : ', opt)
        if args == []:
            print('   ❌       None args to show')
        else:
            count = 1
            for i in args:
                print('   ✅          -->  args[', count, ']: ', args[count - 1])
                count += 1

    def opSelect(self, oper, opt, args):
        """
            When operation have typed in, analyse the Major oper and enter specific module
        """
        if oper == 'exit':
            print("Bye ~")
            sys.exit()
        elif oper == 'man':
            self.manPage(oper, args)
            return 0
        elif oper == 'pwd':
            print(Rfile.pwd())
            return 0
        elif oper == 'cd':
            retVal = Rfile.cd(args)
            return retVal
        elif oper == 'tree':
            if args == []:
                print('[list contents of directories in a tree-like format.]')
                Rfile.tree('.')
                return 0
            print('[list contents of directories in a tree-like format.]')
            args = args[0]
            Rfile.tree(args)
            return 0
        elif oper == 'ls':
            """
            if args == []:
                Rfile.ls()
            else:
                Rfile.ls(args[0])
                
                TO DO, delete this part for secure accessing
            """
            Rfile.ls()
            return 0
        else:
            return 0


    def manPage(self, oper, args):
        """
            *nix style man page, ignore args[i] except the first one
        """
        if args == []:
            print("What manual page do you want?")
            print("For example, try 'man net'.")
        elif args[0] == 'net':
            print("\n   ============== args ===================")
            print("      1. join     : Join Network.")
            print("      2. leave    : Leave Network.")
            print("      3. upload   : Upload File.")
            print("      4. download : Download File.")

            print("      5. ft       : Print Finger Table.")
            print("      6. nb       : Print my predecessor\n"
                  "                    and successor.")
            print("      7. exit     : terminate net server")
            print("   ============ man net ==================\n")
        elif args[0] == 'all':
            print("\n   ============== args ===================")
        else:
            print(oper, args[0])
    # to do
