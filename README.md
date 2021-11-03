```
    _,.---._    ,--.--------.   ,---.        ,-,--.          .=-.-..=-.-. 
  ,-.' - ,  `. /==/,  -   , -\.--.'  \     ,-.'-  _\        /==/_ /==/_ / 
 /==/ ,    -  \\==\.-.  - ,-./\==\-/\ \   /==/_ ,_.'       |==|, |==|, |  
|==| - .=.  ,  |`--`\==\- \   /==/-|_\ |  \==\  \          |==|  |==|  |  
|==|  : ;=:  - |     \==\_ \  \==\,   - \  \==\ -\         /==/. /==/. /  
|==|,  '='  ,  |     |==|- |  /==/ -   ,|  _\==\ ,\        `--`-``--`-`   
 \==\ _   -    ;     |==|, | /==/-  /\ - \/==/\/ _ |        .=.   .=.     
  '.='.  ,  ; -\     /==/ -/ \==\ _.\=\.-'\==\ - , /       :=; : :=; :    
    `--`--'' `--`    `--`--`  `--`         `--`---'         `=`   `=`     
```

# What is Qtas

Qtas（Quite a Storage）is a experimental distributed storage system developed by Q-team in BJFU Advanced Computer Network sources.

# Why names Qtas?

- Q means ours team's name;
- s means this project is focusing on the development of Storage system;
- Quite a Storage includes all our wishes to finish this job && make it perfect;
- This is Qtas :)

# What's in it?

- A virtual file system supports remote managing;
- IPv6 support
- distributed storage system
- least surprising interaction surface for UNIX users
- ... still finding something cool to add

# Function List

## File System Operations
1. pwd：print work directory
`pwd [] ()`
2. cd：change directory
``
3. ls：list files
``
4. cat：
``
5. cp
``
6. mv
``
7. find
``
8. chmod
``
9. sudo
``
10. rm
``
11. tree
``
12. ...

## for Root users

## for Normal users

## Connection

1. netstat
2. QAQ

## CLI

## Log System

## Man Page

- `opRead( str ) -> list`  
To analyse a command series, and split the str into list 
with the respect of " ". Meanwhile, formatize the operations
with UNIX-Style.
- `printLogo()`
- `printHelp()`
- `opSplit( str command_list ) -> operation, optional, args`
- `opShow(command_list)`

# Working Flow
- P2P 弱化了 C/S 的概念，在网络中每一个节点既可能是server，也可以是client，可以把发起请求的称为client，而接受请求的为server；
- 把整个计算机集群看作一个大的server，发起请求的时候，谁先响应谁先处理，响应一个请求后，server端广播集群，开始处理请求；
- 需要有信号量机制，保证服务器同步；
1. client向服务器广播，发起请求寻找file1
2. 
## 打开程序

## 
