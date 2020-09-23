#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def main():
    a = fib(6)
    print('test fib(6)=', a)

print(__name__)
if __name__ == '__main__':
    print(__name__)
    main()

