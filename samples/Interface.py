import sys

from LogSys import Log


class Cli:
    """
        Class Cli include stuffs relating to menu stuff, user's interface looking ...
    """
    curPath = '/root'
    connStat = 'Offline'
    usrName = 'Rrrrraulista'

    def printLogo(self):
        """
            just print a beautiful logo
        """
        print('    ___            _     _       ____ _        __    ')
        print('   /   \__ _ ___  (_)___| |_    /___ \ |_ __ _/ _\   ')
        print('  / /\ / _` / __| | / __| __|  //  / / __/ _` \ \    ')
        print(' / /_// (_| \__ \ | \__ \ |_  / \_/ /| |_ (_| |\ \   ')
        print('/___,\' \__,_|___/ |_|___/\__| \___,_\ \__\__,_\__/    ... is being started !\n')

    def cliHelp(self, type):
        """
            This func could print several possible helps to users
                1. "all" : mainly using in the welcome interface;
                2. "sp"  : to give specific optional args when using op wrongly
                3. to do
        """
        if type == 'all':
            print('usage: <operation> [optional] [arguments] ...')
            print('          ls :     to display all files in this directory')
            print('          pwd:     to show the currently using directory')
            print('          cd:      move to the wanted directory')
        elif type == "sp":
            print("❌ something seems going wrong")
            print("operation [optional] (arg_1) (arg_2)")
            # to do

    """
        Display the prompt sign, and read the operation user typed in
    """

    def cliPrompt(self):
        # [Net state] < user's name > ( current working path ) >>> _type operation here_
        log = Log()
        prompt_str = "[" + self.connStat + "] <" + self.usrName + "> ( " + self.curPath + " ) >>> "
        command_str = input(prompt_str)
        command_list = self.opRead(command_str)
        oper, opt, args = self.opSplit(command_list)
        # self.opShow(command_list)
        log.writeHistory(oper)
        if oper == 'exit':
            print("Bye ~")
            sys.exit()
        return oper, opt, args

    """
        Read an operation from stdin, delete all spaces
        retVal : opList : ['op1', 'op2', 'op3', ... ]
    """

    def opRead(self, opStdin):
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

    """
        Split the operation with:
            1. operation : Major Operation
            2. optional : Optional argument
            3. args : ['arg1', 'arg2', 'arg3', ... ]
    """

    def opSplit(self, opList):
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

    """
        Display the correctly and splitted operation
    """

    def opShow(self, opList):
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

    """
        When operation have typed in, analyse the Major oper and enter specific module
    """

    def opSelect(self):
        print('opSelect(self)')
    # to do
