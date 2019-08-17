# Объединение списков. В конце дубликатов быть не должно
def union(lst1, lst2):
    new_list = lst1.copy()
    for i in lst2:
        if i not in new_list:
            new_list.append(i)
    return new_list

union([1, 2, 3], [2, 3, 4]) # [1, 2, 3, 4]
union(['a', 'b', 'c', 'd'], [1, 2, 'd', 'a', 'f']) # ['a', 'b', 'c', 'd', 1, 2, 'f']

# Пересечение списков
def intersection(lst1, lst2):
    n = []
    for i in lst2:
        if i in lst1:
            n.append(i)
    return n

intersection([1, 2, 3], [2, 3, 4]) # [2, 3]
intersection(['a', 'b', 'c', 'd'], [1, 2, 'd', 'a', 'f']) # ['a', 'd']
intersection([1, 2], [3, 4]) # []

# Вычитание список lst2 из lst1
def difference(lst1, lst2):
    n = []
    for i in lst1:
        if i not in lst2:
            n.append(i)
    return n

difference([1, 2, 3], [2, 3, 4]) # [1]
difference(['a', 'b', 'c', 'd'], ['a', 'b']) # ['c', 'd']
difference([1, 2], [1, 2]) # []

# Обатное пересечение (входят только те элементы, которые есть либо в lst1 либо в lst2, но не в оба массива)
def xor(lst1, lst2):
    n = lst1.copy()
    for i in lst2:
        if i in lst1:
            n.remove(i)
    m = lst2.copy()
    for a in lst1:
        if a in lst2:
            m.remove(a)
    return n+m


xor([1, 2, 3], [2, 3, 4]) # [1, 4]    
xor(['a', 'b'], ['c', 'd']) # ['a', 'b', 'c', 'd']

def xor_alternative(lst1, lst2):
    u = union(lst1,lst2)
    n = intersection(lst1,lst2)
    s = difference (u,n)
    return s