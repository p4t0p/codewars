l = [1, 10, 30, 12, 5, 0, -3, 18, 4]

# 1
# Вывести в консоль все элементы списка l больше n
def print_all_bigger(n):
    for i in l:
        if n < i:
            print (i)
    

# 2
# Вывести в консоль все нечетные элементы списка l
def print_all_odd(l):
    for i in l:
        if i%2 == 1:
            print (i)
    


m = ['1', 10, 30, None, 'Hello', 0, -3, '18', 4, 5.12]

# 3
# написать функцию, которая фильтрует список выкивывая из него все, что не является числом
def filtr_notnum(list):
    nums = []  
    for i in list:
        if type (i) is int or type (i) is float:
            nums.append(i)
    return nums