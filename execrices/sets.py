# Объединение списков. В конце дубликатов быть не должно
def union(lst1, lst2):
    pass

union([1, 2, 3], [2, 3, 4]) # [1, 2, 3, 4]
union(['a', 'b', 'c', 'd'], [1, 2, 'd', 'a', 'f']) # ['a', 'b', 'c', 'd', 1, 2, 'f']

# Пересечение списков
def intersection(lst1, lst2):
    pass

intersection([1, 2, 3], [2, 3, 4]) # [2, 3]
intersection(['a', 'b', 'c', 'd'], [1, 2, 'd', 'a', 'f']) # ['a', 'd']
intersection([1, 2], [3, 4]) # []

# Вычитание список lst2 из lst1
def difference(lst1, lst2):
    pass

difference([1, 2, 3], [2, 3, 4]) # [1]
difference(['a', 'b', 'c', 'd'], ['a', 'b']) # ['c', 'd']
difference([1, 2], [1, 2]) # []

# Обатное пересечение (входят только те элементы, которые есть либо в lst1 либо в lst2, но не в оба массива)
def xor(lst1, lst2):
    pass


xor([1, 2, 3], [2, 3, 4]) # [1, 4]
xor(['a', 'b'], ['c', 'd']) # ['a', 'b', 'c', 'd']