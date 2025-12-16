from wsgiref.validate import assert_

from pyexpat.errors import messages

#list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list_a[0])
#print(list_a[-1]) #Перший індекс з кінця
#(list_a[:5]) # : зріз від нуля до 5 буде
# new_list = list_a[:5]
# print(list_a)
# print(new_list)

#print(list_a[2:]) #від вказаного елементу до останнього включно.
# message = "don't subscribe"
# print(message[6:])
# print(message[6:].upper())
#print(list_a[-5:-2]) #між 5 елементом з кінця включно, та другим елементом з кінця не включно
#print(list_a[-2:-5]) #Якщо неправильно то повернеться пустий список
# print(list_a[::2]) #Кожен другий елемент виводиться
#print(list_a[::-1]) #Послідовність задом вперед. Задача на Поліндром.
#print(list_a[8:2:-1]) #В відємну сторону та змінюючи порядок
#print(list_a[8:2:-2]) #від'ємний крок [9, 7, 5]


# list_1 = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list_1[1::2])

# text = 'Python is awesome!'
# print(text[10:])

# palik=input('введіть паліндром: ')
# print(palik[::-1])
# assert (palik)
palindrome=(input('enter characters to check for palindrome: '))
assert palindrome == palindrome[::-1], "it's no palindrome"
print(f'{palindrome} - it`s a palindrome')

# f_string = f'Hi, my name is {name}. I am {age} years old'
# print(f_string)
#
# assert concatenate_string == f_string
# print(f'Hi, my name is {name.upper()}. I am {age + 10} years old')

#_string = f'In the city {Location}.