import socket
from samples import Network

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((Network.get_ip(4), 0))
    s.listen(1)
    print(s)
    port = s.getsockname()[1]
    print("port = ", port)
    print(s.getsockname())
    s.close()
