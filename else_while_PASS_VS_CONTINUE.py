# grade_list = [5, 4, 5, None, 2, 4, 3]
from operator import index

# for i in grade_list:
#     if i == 2:
#         print("We have bad mark")
#         break
#     elif i is None:
#         pass
#     else:
#         print(i)
# else:
#     print('We haven\'t bad mark')


# n=0
# while n < len(grade_list):
#     if grade_list[n] == 2:
#         print("We have bad mark")
#         break
#     elif grade_list[n] is None:
#         n = n + 1
#         continue
#     else:
#         print(grade_list[n])
#     n = n + 1
# else:
#     print("We haven't bad marks")
# print("The end")

# my_list = [2, -1, 3, 4, 6, 9, -5]
# for number in my_list:
#     if number < 0:
#         print("Less 0, keep going")
#         continue
#     if number == 0:
#         print('Zero here')
#         pass
#     print(f"Our number: {number}")
# print("END")


# numbers_list = [-3, -2, 0, 1, 2, 3]
# print ('Start check the numbers list! =)')
# for i in numbers_list:
#     if i < 0:
#         print("number less zero bro!")
#         continue
#     if i == 0:
#         print("Number zero, we should ignore")
#         pass
#     print(f"Our numbers: {i}")
# print("end")
#
# number_list = [5, 6, 7, 8, 9]
# found = False
# for i in number_list:
#     if i % 7 == 0:
#         print(f" The number {i} splited clear to 7 with index ")
#         found = True
#         break
# if not found:
#         print(f"The number splited to 7 doesn't exist on the list")
#
# print("End")

# number_list = [-5, -3, 0, 5, 6, 7, 8, 9]
# total_sum = 0
# for i in number_list:
#     if i <= 0:
#         continue
#     total_sum = total_sum + i
#
# print(f"The sum is '{total_sum}'. Sum counted from all numbers bigger than 0")
# print("The end")