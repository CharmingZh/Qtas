'''
    System library
'''
import socket
import threading
from threading import Lock, Thread
import time
import os
'''
    project implemented
'''
from Interface import Cli
from Vfile import File

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

    #s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    #s.connect()
    while True:
        cli.cliPrompt()
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print('IP = ', args.host)
    """