#print(dir([1, 2, 3]))
from itertools import count

l_1 = [1, 2, 3, 1, 777]
l_2 = [1, 777, 999]

# l_1.append(555)
# print(l_1) # [1, 2, 3, 1, 777, 555]
#
# l_1.append(l_2)
# print(l_1) # [1, 2, 3, 1, 777, 555, [1, 777, 999]]

# l_1.extend(l_2)
# print(l_1)  # [1, 2, 3, 1, 777, 1, 777, 999]

# l_1.insert(1, 34)
# print(l_1) # [1, 34, 2, 3, 1, 777]

# print(l_1.count(1)) #к-ть відображання 1чки (кількість входженнь)

# print(l_1.index(3)) #2 шукає по індексу певний елемент
# print(l_1.index(1)) #0

# l_1.reverse()
# print(l_1) # [777, 1, 3, 2, 1] зробить реверс елементів

# l_1.pop()
# print(l_1) # по дефолту видаляє останнній, але можна вказати який ти хочеш видлити.

# l_1.remove(1)
# print(l_1) #[2, 3, 1, 777]

# new_list = l_1.copy() # or l_1[::] not new_list = l_1
# print(id(new_list))
# print(id(l_1))

# print(l_1)
# l_1.sort()
# print(l_1) #[1, 1, 2, 3, 777]

# l_4 = ['apple', 'tea', 'lemon', 'python',]
# l_4.sort(key=len, reverse=True) #['python', 'apple', 'lemon', 'tea']
# print(l_4)

# l_1.clear()
# print(l_1) #[]

# grades = [5, 3, 4, 2, 5]
# grades.sort()
# for i in grades:
#      if i >= 4:
#       print(i)

# list_1=['apple', 'tour', 'car', 'tree']
# list_2=['tree', 'dor', 'window', 'cinema']
# list_1.extend(list_2)
# for i in list_1:
#     print(f'{i} ({len(i)})')

 