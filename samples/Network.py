import socket


def get_ip(version = 4):
    if version == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('1.1.1.1', 80))
        IP = s.getsockname()[0]
        print('1', s.getsockname()[1])
        s.close()
        print('socket has closed')
        # return socket.gethostbyname(socket.gethostname()) # some times return 127.*
        return IP
    elif version == 6:
        print('version == 6, todo')
        # to do
    else:
        print("version type wrong")

class Server:
    print()
    # to do

class Client:
    print()
    # to do

if __name__ == '__main__':
    ip = get_ip()
    print(ip)