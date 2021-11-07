> @Time    : 2021/11/7 1:58 上午\
@Author  : Jiaming Zhang\
@FileName: A pitfall of threadthreading.Thread() in python.md\
@Github  : https://github.com/CharmingZh

The topic of this article is to explain the differences between
two ways of calling thread function below:

Thread(target=function name, args=arguments to function), but 
later I thought I had to enter more targets, args and two = 
signs, so I thought it was a good idea to use threading. 
`hread( function name (function argument))` to open a thread
, practice a program, run the results are the same as the 
previous method of writing the results, and then write 
according to this omission, until encountered a 
multi-threaded program, found that the program is written 
to run only one thread, puzzled, and then found that if 
written as threading. `Thread(function name(function argument))`
, even thread `name.start()` do not need to write, 
the program will run directly, so separate the write is to
prevent the merge interpreter to write directly as a 
function to run, this is my understanding.

```python
thread1 = threading.Thread(target=threadfunc, args=(1,2))
thread2 = threading.Thread(target=threadfunc(arg1=1,arg2=2))
```
Thread corresponding to the target parameter is actually trying
to receive a function type of parameters, this time only write
the function name, which is equivalent to the function of the
object passed to the target, this is also called "function of 
the callback", why is called "function callback "it?  