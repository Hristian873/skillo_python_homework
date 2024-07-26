# # Exercise 1: Online Shopping Discount
#
#
# # Given a variable `total_amount` representing the total amount in the shopping cart,
# # write a program that prints a discount message if the total amount is over $100,
# # and always prints a thank you message.
#
# total_amount= 120  # Fill in the total amount here
# if total_amount> 100:
#     print("You have discount by 20%")
# print("Thank you for shopping!")
# ...
#
# # Exercise 2: Temperature Checker
#
# # Given a variable `temperature` representing the current temperature in Celsius,
# # write a program that prints "Warm" if the temperature is greater than or equal to 25 degrees Celsius,
# # otherwise print "Cool".
#
# temperature = 22  # Fill in the temperature here
# if temperature >=25:
#     print("Warm")
# else:
#     print("Cool")
# ...
#
# # Exercise 3: Time of the Day
#
# # Given a variable `hour` representing the current hour (in 24-hour format),
# # write a program that prints "Good Morning" if the hour is before 12 (12 inclusive),
# # "Good Afternoon" if the hour is between 12 and 17 (17 inclusive),
# # and "Good Evening" if the hour is after 17.
#
# hour = 25  # Fill in the hour here
# if hour<12:
#     print("Good morning")
# elif 12<hour<=17:
#     print("Good Afternoon")
# elif 17<hour<24:
#     print("Good evening")
# else:
#     print("This hour does'nt exist")
#
# # Exercise 4: Secret Message
#
# # Given a variable `message` representing a secret message,
# # write a program that prints "Message found" if the message is not empty,
# # otherwise print "No message".
#
# message = ""  # Fill in the message here
#
# if message:
#     print("Message found")
# else:
#     print("No message!")
#
#     # Exercise 5: List Iteration
#
#     # You have a list of fruits. Write a program that iterates over each fruit in the list and prints each fruit's name.
#
# fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]
#
# for fruit in fruits:
#         print(fruit)
#
#
#     # Exercise 6: Range Iteration
#
#     # Write a program that prints all the even numbers from 1 to 20 using a for loop and the range() function.
# for a in range(0,21):
#     if a%2 == 0:
#         print(a)
#         a +=a
#
#
#     # Exercise 7: While Loop
#
#     # Write a program using a while loop to find the sum of all numbers from 1 to 100.
# a=0
# b=0
# while a in range(0,101):
#     b=a+b
#     a+=1
# print(b)
#
#
#     # Exercise 8: Number of Friends
#
#     # Write a program that asks how many friends you have and then asks for each of their names.
#
# num_friends = int(input("How many friends do u have: "))
# list_friends = []
# for names in range(num_friends):
#         namess=input(f"What is the name of ur friend number:  {names + 1}  ")
#         list_friends.append(namess)
# print(list_friends)
#
# # Exercise 9: Guess the Number
#     # Write a program that has a number and keeps asking the user to input a number until the user guesses it.
#
# secret_number = 42
# for    answer in range(0,1000):
#     answer=int(input("Guess the right number: "))
#     if answer == secret_number:
#         print("You have guessed it")
#         break
#     else:
#         print("Try again")
#         continue
#
#
# # Exercise 10: Multiplication Table
#
#     # Generate the multiplication table for the numbers 1 to 9.
# a=0
# b=0
# for a in range(0,9):
#     a += 1
#     for b in range(0,10):
#      sum = (a*b)
#
#      b+=1
#      print(sum)
#
#     # Exercise 11: continue
#
#     # Do the same as in Exercise 6 but do not print the number 10. Use `continue` do achieve this
#
# for a in range(0, 21):
#         if a % 2 == 0:
#             if a == 10:
#                 continue
#             print(a)
#             a += a
#
#
#     # Exercise 12: Password Checker
#
#     # Write a program that asks the user to enter a password. If the password is correct, print a message saying
#     # "Access granted" and end the program. If the user enters the wrong password three times, print "Access denied" and
#     # end the program..
#
#
correct_password = "learnpythonwithskillo"
a= 0

while a<3:
    password_checker = input("Enter password: ")
    if password_checker == correct_password and a <3:
        print("Access Granted!")
        break
    else:
        print("Access denied")
        a += 1
if a == 3 :
    print("No more attempts!")




