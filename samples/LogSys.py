import errno
import os
import time
import Interface


class Log:
    """
        Log class includes three features:
            1. user's(client) operation history would write into a file
            2. Error check system check
            3. System stability required
    """

    def writeHistory(self, cmd_str):
        date_full = self.getTime()
        date = date_full[:10]
        path = os.getcwd()
        path = path + "/samples/.log/"
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
