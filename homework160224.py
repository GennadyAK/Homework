def sum_list(a: list, b: list) -> list:
    c=[]
    a.extend([0,] * (len(b) - len(a)))
    b.extend([0,] * (len(a) - len(b)))
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

print(sum_list([1, 2, 3, 4], [1, 2, 3]))