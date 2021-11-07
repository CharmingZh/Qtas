> @Time    : 2021/11/6 3:45 下午\
@Author  : Jiaming Zhang\
@FileName: Way to get IP address.md\
@Github  : https://github.com/CharmingZh

[出现原因]：

- TCP协议为了提高传输效率，发送方往往需要收集定量的数据才会封装给
  底层并发送，若出现连续`send(data)`，TCP会把该数据进行整合(直到
  装满数据缓冲区)，这样就造成了粘包数据;

- 接收方接收方的粘包是由于接收用户相关进程不及时接收数据，从而导致
  粘包问题，这是因为接收方先把接收到的数据放在系统接受缓冲区，用户
  进程从该缓冲区取定量的数据，但**若下一包数据到达前，缓冲区的数据没
  有及时的被用户进程取走**，则下一包数据与前一包部分数据在系统缓冲区
  ，就可能导致用户设定的进程缓冲区从系统缓冲区取走两个包的部分数据
  ，从而导致粘包;

[解决办法]：

-  发送方在send()之前，先向接收方发送数据总量大小，并通过双端
   确认，server端发送数据包，然后接收方通过按数据量大小循环设
   立缓冲区接收数据;

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