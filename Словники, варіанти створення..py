# my_list = [10, [99, 109, 1,], "hello"]
# print("===list value===")
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
from http.cookiejar import uppercase_escaped_char
from lib2to3.fixes.fix_asserts import NAMES
from locale import currency

# my_dict = {"first_key":"first_calue", 777: [34, 1000], (45, 1): 4324}
# print(my_dict["first_key"])
# print(my_dict[777])
# print(my_dict[(45, 1)])

# dict_1 = {"first_key": "first_value", "second_key": "second_value"}
# print(type(dict_1))
# print(dict_1)
#
# dict_2 = dict([["first_kety", "first_value"], ["second_key", "second_value"]])
# print(type(dict_2))
# print(dict_2)

# dict_3 = dict.fromkeys(["key_1", "key_2", "key_3"], "values")
# print(type(dict_3))
# print(dict_3)


# my_conv = {"USD": 40.44, "EUR": 45.55,}
# currency_my = input("Input the currency USD or EUR: ").upper()
# change_sum = float(input("Input the sum for change the currency please: "))
# exchange_rate = my_conv[currency_my]
# result_UAH = change_sum * exchange_rate
# print(f"For {change_sum} {currency_my} you get {result_UAH:.2f} UAH.")
#
price = {"USD": 40, "EUR": 50}
currency=input("Input currency (USD or EUR): ").upper()
change_sum=float(input("Input the sum UAH for change please: "))
exchange=price[currency]
result=change_sum*exchange
print(f" For your {change_sum} you get {result} UAH")

# subjects = { 'audi', "club",  "Arsenal"}
# meaning = 0
# subjects_dict = dict.fromkeys(subjects, meaning)
# print(subjects_dict)

# objects_hobby = {"karate", "dance", "hiking"}
# point_hobby = 0
# dictionary = dict.fromkeys(objects_hobby, point_hobby)
# print(dictionary)

# students_grades = {"Alex": [2, 1, 20, 33], "Arsene": [4, 2, 20, 33]}
# avarage_points = {}
# for name, grades in students_grades.items():
#     total_sum = sum(grades)
#     count = len (grades)
#     avarage = total_sum / count
#     avarage_points[name]=avarage
#
# print("answer: ", avarage_points)

baba = {"baba1": [2, 3, 4], "daha": [5, 6, 77]}
loh={}
for name, money in baba.items():
    #all_money = sum(money)
    count = len(money)
    avarage = count
    loh = avarage
    print("anwer: ", loh)
