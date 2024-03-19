r = list(range(1, 101))
print(r)

def binary_search(n, array):
    start, finish = array[0], array[-1]
    tryy = []
    while start < finish:
        middle = (start + finish) // 2
        if n == middle:
            return n
        if n > middle:
            start = middle
            print("Попытка")
        elif n < middle:
            finish = middle
            print("Попытка")

print(binary_search(77, r))