#1
def counter(array: list):
    for elem in array:
        yield elem**2

a = counter(list(range(1, 11)))

print(next(a))


#2
def counter(array: list):
    for elem in array:
        if elem % 2 == 0:
            yield elem

a = counter(list(range(1, 11)))

print(next(a))


#3
def sub_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(sub_fib(20)))


#4
import random

def ran_num(a, b):
    array = []
    for i in range(10):
        num = random.randint(a, b)
        array.append(num)
    yield array

print(next(ran_num(0, 20)))


#5
