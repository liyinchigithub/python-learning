#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test57_ asyncio_test.py
# https://blog.csdn.net/bluehawksky/article/details/106283636
# 异步函数的定义

import asyncio
import time

'''
    # 普通函数定义
    def add2(x):
        print(x+2)
        return x+2

    # 异步函数的定义
    async def add3(x):
        print("in async fun add")
        return x+3
    
    调用普通的函数只需要 result = add2(2),这时函数就可以得到运行，并且将结果4返回给result,如果使用result = add3(2),此时再打印 result 呢？
    得到的是一个coroutine对象，<coroutine object add3 at 0x000002ED564A5048>，并不是2+3=5这个结果，怎样才能得到结果呢？
    协程函数想要执行需要放到[事件循环]里执行。
    
    Eventloop 是asyncio应用的核心,把一些异步函数注册到这个事件循环上，事件循环会循环执行这些函数,当执行到某个函数时，如果它正在等待I/O返回，如
    它正在进行网络请求，或者sleep操作，事件循环会暂停它的执行去执行其他的函数；当某个函数完成I/O后会恢复，下次循环到它的时候继续执行。因此，这些
    异步函数可以协同(Cooperative)运行：这就是事件循环的目标
    
    import asyncio
    loop = asyncio.get_event_loop()
    async def add3(x):
        print("in async fun add")
        return x+3
    result = loop.run_until_complete(add3(2))
    print(result)

    #运行的结果是
    #in async fun add
    #5
    
    或者使用
    
    [await 关键字]来修饰函数的调用，如result = await add3(2),但是await只能用在协程函数中，所以想要用await关键字就还需要定义一个协程函数
    async def add3(x):
    print("in async fun add")
    return x+3

    async def main():
        result = await add3(2)
        return result
        
    但最终的执行还是需要放到一个事件循环中进行.
'''

# 定义一个协程函数
async def testa(x):
    print("in test a")
    await asyncio.sleep(3)
    print("Resuming a")
    return x

# 定义一个协程函数
async def testb(x):
    print("in test b")
    await asyncio.sleep(1)
    print('Resuming b')
    return x

# 定义一个协程函数
async def main():
    start = time.time()
    resulta = await testa(1)# 协程函数testa执行完毕后，返回结果1
    resultb = await testb(2)# 协程函数testb执行完毕后，返回结果2
    print("test a result is %d"%resulta)
    print("test b result is %d"%resultb)
    print("use %s time"%(time.time()-start))

if __name__ == '__main__':
    loop = asyncio.get_event_loop() # 获取一个事件循环
    loop.run_until_complete(main()) # 将协程函数注册到事件循环中，并执行