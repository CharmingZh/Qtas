import threading
import time
import test_SHA
def func1():
    while True:
        print("This is thread 1")
        time.sleep(5)

def func2():
    print("The second thread 2")
    time.sleep(5)
"""
threads = []
t1 = threading.Thread(target=func1(), args=None)
t2 = threading.Thread(target=func2(), args=None)

threads.append(t1)
threads.append(t2)
"""
if __name__ == '__main__':
    """
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    while True:
        print("This is main()")
        time.sleep(1)
    """
    print(test_SHA.calSha("hello", 512))