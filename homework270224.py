#1
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} -> {v}")

func(integer=1, double=2.4, array='hello', empty=[])


#2
def my_func_1():
    print("In my_func_1")
    def my_func_2():
        print("In my_func_2")
        def my_func_3():
            print("In my_func_3")
            def my_func_4():
                print("In my_func_4")
                def my_func_5():
                    print("In my_func_5")
                return my_func_5()
            return my_func_4()
        return my_func_3()
    return my_func_2()


my_func_1()
print("END")


#3
def crreate_multiplications(n):
    return [lambda x, i=i: x * i for i in range(n)]

print(crreate_multiplications(3)[0](4))