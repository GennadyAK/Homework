#1
def add(x, y):
    s =[]
    for i in range(len(x)):
        s.append(x[i] + y[i])
    return s
print(add())


#2
def pall(x):
    x += 1
    while str(x) != str(x)[::-1]:
        x += 1
    return x
print(pall())


#3
def get_number(word: str) -> int:
    for symbol in word:
        if symbol.isdigit():
            return int(symbol)

def custom_sort(array: str) -> str:
    sorted_list = sorted(array.split(), key=get_number)
    return " ".join(sorted_list)

print(custom_sort("is2 Thi1s T4est a3"))


#4
from random import randint

def get_random_list(count: int, start: int, end: int):
    return [randint(start, end) for _ in range(count)]
print(get_random_list(10, 1, 5))

def get_count_nunique(array: list) -> int:
    unique_elems = set(array)
    res = []
    for elem in unique_elems:
        if array.count(elem) > 1:
            res.append(elem)
    return len(res)
print(get_count_nunique(get_random_list(10, 1, 5)))


#5
def search(string: list[str], substring: str) -> list[str]:
    res = [i for i in string if i.lower().startswith(substring.lower())]
    return res
print(search())


#6
def simple(x):
    k = 0
    for i in range(2, x // 2+1):
        if (x % i == 0):
            k = k+1
    if (k <= 0):
        return "Число простое"
    else:
        return "Число не является простым"
print(simple())


#6.1
def is_prime(number: int) -> int:
    for i in range(2, int((number ** 0.5)+1)):
        if number % i == 0:
            return False
        return True

print(is_prime())