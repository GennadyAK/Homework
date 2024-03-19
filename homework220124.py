#1
n = list(input("Введите список: ").split(","))
for elem in range(len(n)):
   n[elem] = int(n[elem]) ** 2
print(n)


#2
n = list(input("Введите список: ").split(","))
res = []
for elem in n:
    if len(elem) >= 5:
        res.append(elem)
print(res)


#3
n = list(input("Введите числа: ").split(","))
res = []
for elem in n:
    if int(elem) % 2 == 0:
        res.append(elem)
print(res)


#4
n = input("Введите числа: ").split(",")
res = []
for elem in n:
    if int(elem) % 2 == 0:
         res.append(int(elem) ** 2)
print(f"Сумма = {sum(res)}")


#5
n = input("Введите список: ").split(", ")
res = []
for elem in n:
    if elem.startswith('b'):
        res.append(elem)
print(res)


#6
n = list(input("Введите список: ").split(", "))
res = []
for elem in n:
    if int(elem) in range(10, 20):
        res.append(elem)
print(res)


#7
a = [1, 2, 3, 4, 5, -2, 3]
for i in a:
    if i < 0:
        print(False)
        exit(0)
print(True)


#8
arra_list = ['123', 'esdgsdg12', '123w']
res =[]
for i in arra_list:
    if i.isdi
