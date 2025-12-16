# our_string = 'Hello world'

# print(our_string.upper()) #HELLO WORLD
# print(our_string.lower())
# print(our_string.count('l'))
# print(our_string.count('ll'))
# print(our_string.count('l', 2))
# print(our_string.count('l', 3, 7 )
# print(our_string.find('o'))
# print(our_string.rfind('o'))
# print(our_string.find('apple'))
# print(our_string.index('apple') # not found
# print(our_string.replace('Hello', 'hi'))
# print(our_string.replace(' ', ''))
# print(our_string.isalpha()) #false
# print('sfasdf'. isalpha())  #True
# print(our_string.isdigit())
# print('text'.rjust(33))
# print('text'.rjust(10, '!'))
# print('text'.ljust(10, '!'))
# new_string = '  hi   '
# print(new_string.strip())
# print((new_string.lstrip()))
# print(new_string.rsplit())
# print(our_string)
# our_string = our_string.upper()
# print(our_string)

# str=input('Введіть рядок наш користувачу:')
# # print(str.replace('пізда повна', 'заміняй мат лапух'.upper()))
# #print(str.count('') -1)
# empty=str.find('a')
# if empty == -1:
#   print("there is no any 'a' in your string")
# else:
#   print(str.replace('a','*'))

str=input('прокоментуйте сьогоднішню гру будь ласка, але мати ми приберемо: ')
empty=str.find('бля')
if empty == -1:
    print('молодець, що без матів')
else:
    print(str.replace('бля', 'МАТ'))