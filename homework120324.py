from time import sleep


#1
def uppper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

    return wrapper

@upper
def say_hi(name: str):
    return f"{name}, Hello!"


#2
def exception(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(type(e))
    return wrapper

@exception
def say_hi(name: str):
    raise ValueError


#3
def exception(func):
    def wrapper(*args, **kwargs):
        print("Задержка")
        sleep(2)
        func(*args, **kwargs)
    return wrapper

@exception
def say_hi(name: str):
    print("hello")


#4
