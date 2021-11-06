import _io
import os

class File:
    def __init__(self, Name):
        self.name = Name

    def open_file(self, name):
        try:
            self.pfile = open(name, 'r')
            print('file open')
        except:
            print("open_file fail")

    def close_file(self):
        print('start close')
        self.pfile.close()
        print('file closed')

    def read_file(self):
        print("read file")
        data = "Info in the file"
        return data
        # to do

    def write_file(self, info):
        print("Write file")
        # to do

    # to do

class Dir:
    def __init__(self):
        print()
        # to do

    # to do