#1
def sort_pupl(n: list) -> list:

    sorted_list = sorted(n, key=lambda x: int(x['Возраст']), reverse=True)
    return sorted_list

print(sort_pupl([{'Имя': 'Сергей', 'Возраст': 15, 'Оценки': [7, 8, 6, 8, 4]},
     {'Имя': 'Анна', 'Возраст': 111, 'Оценки': [4, 5, 6, 5, 4]},
     {'Имя': 'Алексей', 'Возраст': 13, 'Оценки': [8, 8, 6, 8, 7]},
     {'Имя': 'Ирина', 'Возраст': 113, 'Оценки': [7, 6, 6, 2, 4]}]))


#2
def sum_tree(tree: list) -> int:
    result = 0
    for item in tree:
        if isinstance(item, list):
            result += sum_tree(item)
        else:
            result += item
    return result

print(sum_tree([1, 2, [6, 4, [18, 9], 3], 31, [42]]))

#2.1(странно работает)
import re

def sum_tree(tree: list) -> int:
    res = 0
    a = re.findall('[-+]?\d+', tree)
    return sum(list(map(int, a)))

print(sum_tree([1, 2, [6, 4, [18, 9], 3], 31, [42]]))
