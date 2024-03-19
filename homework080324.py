#1
def check_annotations(func):
    def wrapper(*args, **kwargs):
        annotations = (func.__annotations__.values())
        arguments = [type(x) for x in args]
        if annotations == arguments:
            return True
        return False
    return wrapper

@check_annotations
def function(a: int, b: str, c: list):
    return f"a-{a}, b-{b}, c-{c}"

print(function(1, "2", [3]))


#2
def permission_check(func):
    def wrapper(user_type):
       if  user_type in ["admin", "auth_user"]:
           return "Access"
       return "Denied"
    return wrapper

@permission_check
def function(user_type: str):
    return "200"

print(function(user_type="admin"))

#2.1
def permission_check(func):
    def wrapper(*args, **kwargs):
       if "user_type" not in kwargs.keys():
           return "Not valid data"
       if kwargs["user_type"] in ["admin", "auth_user"]:
           return "Access"
       return "Denied"
    return wrapper

@permission_check
def function(user_type: str):
    return "200"

print(function("admin"))


#3
from time import sleep

def cache_decorator(func):
    count, cache = 0, {}

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        if cache and count in range(1, 3):
            return cache['cache']
        count = 0
        cache["cache"] = func(*args, **kwargs)
        return cache["cache"]
    return wrapper

@cache_decorator
def operation(num: int):
    sleep(0.5)
    return num ** 2


print(operation(3))
print(operation(4))
print(operation(5))

print(operation(6))
print(operation(7))
print(operation(8))

print(operation(9))