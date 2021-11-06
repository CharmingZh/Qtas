

```python
# 从Thread类继承
import threading
import time
from time import sleep, ctime


# 线程类,从Thread类继承而来。
class MyThread(threading.Thread):
    # 重写父类的构造方法，其中，func是线程函数，args是传入线程函数的参数，name是线程名称
    def __init__(self, func, args, name=''):
        # 使用super函数调用父类的构造方法，并传入相应的参数值。
        super().__init__(target=func, name=name, args=args)
    # 重写父类的run方法
    def run(self):
        self._target(*self._args)


# 线程函数
def fun(index, sec):
    print('1开始执行{}，时间：{}'.format(index, ctime()))
    # 休眠sec秒
    sleep(sec)
    print('1执行完毕{}，时间：{}'.format(index, ctime()))


def fun2(a, b, c):
    print('2开始执行，时间：{}'.format(ctime()))
    # 休眠sec秒
    sleep(a + b + c)
    print(a + b + c)
    print('2执行完毕，时间：{}'.format(ctime()))

def fun3(num, k):
    print(k, "func3 start")
    for i in range(num):
        print("func3: ", i)
        time.sleep(1)

def main():
    print('开始：', ctime())
    # 创建第一个线程，并制定线程名称为“线程1”
    thread1 = MyThread(fun, (10, 4), '线程1')
    thread2 = MyThread(fun2, (4, 6, 2), '线程2')
    thread3 = MyThread(fun3, (20, 3), '线程3')
    thread1.start()
    thread2.start()
    thread3.start()
    print(thread1.name)
    print(thread2.name)
    print(thread3.name)
    thread1.join()
    thread2.join()
    thread3.join()
    print('结束：', ctime())


if __name__ == '__main__':
    main()

```
 ... and here is the result:
 
```shell
开始： Sat Nov  6 14:07:06 2021 
1开始执行10，时间：Sat Nov  6 14:07:06 2021
2开始执行，时间：Sat Nov  6 14:07:06 2021
3 func3 start线程1
线程2
线程3

func3:  0
func3:  1
func3:  2
func3:  3
1执行完毕10，时间：Sat Nov  6 14:07:10 2021
func3:  4
func3:  5
func3:  6
func3:  7
func3:  8
func3:  9
12
2执行完毕，时间：Sat Nov  6 14:07:18 2021
结束： Sat Nov  6 14:07:18 2021

Process finished with exit code 0
```