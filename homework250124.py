#1(list comp)
a = int(input("Введите число a= "))
b = int(input("Введите число b= "))
a_b = [i ** 2 for i in range(a, b)]
print(a_b)


#2(list comp)
a = int(input("Введите число a= "))
b = int(input("Введите число b= "))
a_b = [i for i in range(a, b) if i % 2 == 0]
print(a_b)


#3(list comp)
array = list(input("Введите строку: "))
array_gen = [i for i in array if i in set("ауоиэыяюеёaeiouy")]
print(array_gen)


#4(list comp)
a_b = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(a_b)


#5(list comp)
nested = [[i, i+1, i+2] for i in range(1, 8, 3)]
print(nested)


#6(dict)
DICT_STD = [
     {"name": "Ivan", "age": 15, "mark_list": [9, 8, 7, 8, 9]},
     {"name": "Alexey", "age": 14, "mark_list": [6, 4, 3, 2, 7]},
     {"name": "Alex", "age": 15, "mark_list": [5, 8, 2, 4, 7]},
     {"name": "John", "age": 16, "mark_list": [3, 8, 3, 5, 2]}]
stud_good = []
AVERAGE_MARK = 7
for stud in DICT_STD:
     marks_count = len(stud['mark_list'])
     marks_sum = sum(stud['mark_list'])
     if marks_sum / marks_count > AVERAGE_MARK:
        stud_good.append(stud)
print(stud_good)


#7(match case)
letter = input("Введите букву: ")
if letter.isalpha() and len(letter) == 1:
    match letter:
        case 'a'|'e'|'i'|'o'|'u'|'y':
            print(f"{letter} - гласная")
        case _:
            print(f"{letter} - согласная")
else:
    print("Not correct")


#8(match case)
day = input("Введите день недели: ")
match day:
    case "saturday":
        print(f"{day} - выходной")
    case "sunday":
        print(f"{day} - выходной")
    case _:
        print(f"{day} - рабочий день")