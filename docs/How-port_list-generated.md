Because of the TCP connected required port parts between 
nodes in the Internet. Our project generated random port 
descriptor which would be saved in every node using our 
program.

The generating program is here to look.

```python
import random

def gen_port(num=1):
    """
        Generate a port number or a list
    """
    ports_list = [random.randrange(10000, 60000) for x in range(num)]
    if num == 1:
        # s.bind((Network.get_ip(4), 0)) is enough
        return ports_list[0]
    else:
        return ports_list

def gen_port_file():
    port_pool = gen_port(100)
    fwrite = open("data/.port_list", "w")
    for item in port_pool:
        fwrite.write(str(item) + "\r\n")
    fwrite.close()

def get_port():
    port_list = []
    file = open("data/.port_list", "r")
    for port in file.readlines():
        print(port)
        port = port[:-1]
        print(port)
        port_list.append(port)
    file.close()
    return port_list

if __name__ == '__main__':
    gen_port_file()
    port_list = get_port()
    print(port_list)
    print(type(port_list))
```
... and the result is:
```shell
['48087', '28589', '55749', '49297', '49954', ...]
<class 'list'>
```
With the file `/data/port_list`, server/client could call
them to make sure they are using the same port pair.

We only give user the `get_port() -> port_list:list` API to
insure security and consistency issues.

Make sure you have a GLOBAL VAR to maintain the used port
list.