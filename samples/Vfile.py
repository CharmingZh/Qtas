import os

class File:
    def __init__(self, Name):
        self.file = open(Name, 'r')
        self.name = Name
        self.size = os.path.getsize(self.name)

    def __del__(self):
        self.file.close()

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