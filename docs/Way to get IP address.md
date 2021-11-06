I just still couldn't understand how to get a valid IPv6
addr, so you could see the `version == 6` condition left with
a `# to do ` mark.
```python
from socket import *

def get_ip(version=4):
    """
        Get the IP addr of the client
    """
    if version == 4:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('1.1.1.1', 80))
        IP = s.getsockname()[0]
        s.close()
        # return socket.gethostbyname(socket.gethostname()) # some times return 127.*
        return IP
    elif version == 6:
        print('version == 6, todo')
        # to do
    else:
        print("version type wrong")
```