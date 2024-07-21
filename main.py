#task 1
print("Hello world")

#task 2
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your color")
print (f"My name is {name}, I am {age} years old, and my favorite color is {color}")

#task 3
x=int(input("Enter length: "))
y =int(input("Enter width: "))
sum = 2*x +2*y
print(sum)
#task 4
Temp=int(input("Enter degrees in Farenheit: "))
Cels = (Temp-32) * (5/9)
#task 5
print("Enter two numbers: ")
x= int(input("First number: "))
y =int(input("Second number: "))

print(x+y,x-y,x*y,x/y)

#task 6

import math
r=int(input("Enter radius: "))
area = math.pi * r*r
circ = 2*math.pi*r
print(area,circ)

# task 7
numb=int(input("Enter number: "))
if numb%2==0:
    print("The number is even")
else :
    print("The number is odd")
#task 8
vote_check=int(input("Enter your age: "))
if vote_check<18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
#task 9
some_string=input("Enter a sentence:")
print (len(some_string))

#task  10
str1=input("Enter first sentence ")
str2=input("Enter second sentence ")
str3 = str1 + str2
print (str3)