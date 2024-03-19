#1
array = "dsfsfsdfs sdfsdf sdfsdd sfdsdgvs hgfjgf sgrdhdh hfhjrthd"
array_lst = array.split()
z = sorted(array_lst, key=len)
minlen = len(z[0])
res = []
for elem in z:
    if len(elem) == minlen:
        res.append(elem)
print(res)

#1.1
array = "dsfsfsdfs sdfsdf sdfsdd sfdsdgvs hgfjgf sgrdhdh hfhjrthd"
array_lst = array.split()
word_min_len = len(min(array_lst, key=len))
res = [word for word in array_lst if len(word) == word_min_len]
print(res)


#2
num = input('Введите число: ')
z = len(num)
result = 0
if not num:
    exit(0)
for i in range(0,z):
    result += int(num[i])**z
if result == int(num):
    print(f"{num} - нарциссическое число")
else:
    print(f"{num} - число не нарциссическое")