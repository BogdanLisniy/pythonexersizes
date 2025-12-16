# print("Hi")
# name = input("What is your name?: ")
# print(name, "Nice to meet you")
#
# print("Hi")
# name = input("What is your name?: ")
# print(name, "Nice to meet you")
#
# print("Hi")
# name = input("What is your name?: ")
# print(name, "Nice to meet you")


# def foo():
#     print("Hi there, bro!!")
#     name = input("What is your name?: ")
#     print(name, "Nice to meet you")
# foo()
# foo()
# foo()

# def congratulation():
#     print("Congrats to you bro! For who the greetings?")
#     greetings=input("Fill in the name: ")
#     print("Greate!")
#     print(f"Greetings to you {greetings} and best wishes!\n")
# congratulation()
# congratulation()

# def one_plus_one():
#     print("I'll summ your and your friend money")
#     your_money=int(input('Input your money: '))
#     print('And your friend needed too')
#     friend_money=int(input("Input friend money"))
#     print("Ok, I'll calculate the sum")
#     total=your_money+friend_money
#     print(f"You both has a {total} money\n")
# one_plus_one()
# one_plus_one()

# def orestovich():
#     print('Hello, fill in the list')
#     list_1= int(input('Input the list: '))
#     list_2 = int(input('Input the list '))
#     list_3 = int(input('Input the list '))
#     calc = (list_1 + list_2 + list_3) / 3
#     avarage = (f"Avarage of three will be {calc}")
#     print(avarage)
#
# orestovich()
# orestovich()

def our_list():
    print("Enter numbers separated by spaces")
    numbers = input("Enter data: ")
    number_list = [float(num) for num in numbers.split()]
    avg = sum(number_list) / len(number_list)
    print(f"Avarage is: {avg}\n")
our_list()
our_list()





