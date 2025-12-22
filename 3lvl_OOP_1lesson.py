# class MyFirstClass:
#     def say_hello(self):
#         print('Hello')
#
# my_first_class = MyFirstClass()
# my_first_class.say_hello()
#
# str_1 = 'Hi'
# print(type(str_1))
# print(str_1.lower())
#
# print (type(my_first_class))
#
# print('#'*30)
# print(dir(my_first_class))
# print('#'*30)
# print(dir(str_1))
from cgitb import reset


# class MorningGreeter:
#     def say_good_morning(self):
#         print('Good morning')
# my_class = MorningGreeter()
# my_class.say_good_morning()

# class Bank:
#     def exchange_rate_usd(self):
#       price = {"USD": 42.0}
#       change_uah_sum = float(input("Input sum of UAH please: "))
#       exchange = change_uah_sum / price["USD"]
#       print(f"You will have {exchange:.2f} USD for Your's {change_uah_sum} Hryvnas")
#
#     def exchange_rate_eur(self):
#         price = {"EUR": 45.5}
#         change_uah_sum = float(input("Input sum of UAH please: "))
#         exchange = change_uah_sum / price["EUR"]
#         print(f"You have the {exchange:.2f} EUR for Your's {change_uah_sum} Hryvnas")
#
#     def card_expire_date(self):
#         card_expire = int(input("Enter card creating year: "))
#         expire_date = card_expire + 1
#         print(f"Your card will end at {expire_date} year")
#
#
# my_bank_class = Bank()
# my_bank_class.exchange_rate_usd()
# my_bank_class.exchange_rate_eur()
# my_bank_class.card_expire_date()

def squared_number():
    try:
       number_str = input("Enter the number for count in square: ")
       return float (number_str)
    except ValueError:
        print("You wrong bro")
        return squared_number()

class Mathematics:
    def calculate_square(self):
     number = squared_number()
     result = number ** 2
     print(f"The result is {result}")
     return result
#my_math_instance = Mathematics()
#result_final = my_math_instance.calculate_square()



ss

