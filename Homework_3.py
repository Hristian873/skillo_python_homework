#Problem 0
numb=int(input("Enter number: "))
if numb%2==0:
    print("The number is even")
else :
    print("The number is odd")
#Problem 1
a=0
b=0
for Numbers in range(0,101):

   if Numbers%2 ==0:
       b=Numbers+b
       print(Numbers)
print(b)

#Problem 2
answer=int(input("Enter how much is 5 + 17: "))
while answer != 22:
    print("Wrong answer try again: ")
    answer=int(input("Enter how much is 5 + 17: "))
print("Good job right answer")

#Problem 3

for numbers in range(0,1001):
    if numbers %5==0 and numbers %3 == 0:
        print("FizzBuzz")
    elif numbers %5== 0:
        print("Buzz")
    elif numbers %3==0:
        print("Fizz")
    else: print(numbers)
#Problem 4
import random
a= random.randint(1,100)
print(a)
b= int(input("Enter number between 1 and 100: "))
while b != a:
    if a < b:
        print("Too high")
    elif a > b:
        print("Too low")

    b = int(input("Enter number between 1 and 100: "))
print("You guessed it right.")

#Problem 5
a= random.randint(1,100)
b= random.randint(1,100)
answer=int(input(f"Enter how much is {a} + {b}: "))
sum = a+ b
while answer != sum:
    print("Wrong answer try again: ")
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = int(input(f"Enter how much is {a} + {b}: "))
    sum = a + b
print("Good job right answer")

#Problem 6


numb=int(input("Enter a number"))
for numbers in range(1,11):
    print(numb,"*", numbers,"=", numb*numbers)

# #Problem 7
number = 1
if number > 1:
 for i in range(2,(number//2)+1):

   if (number % i)== 0:
      print(number,"Is not a prime number")
      break
   else:
    print(number,"Is prime number")
    break
else:
    print("Is not prime Number")

#Problem 8
number = 5

for i in range(1,number+1):

    for j in range(1,i +1):
        print(j, end=" ")

    print()