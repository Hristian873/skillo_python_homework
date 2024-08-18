#Problem 0
def sum_elements(arr):
    result = 0
    for numbers in arr:
        result += numbers
    return result
print(sum_elements([1,2,3,4,5,10]))

#Problem 1
def simple_calculator(num1, num2):
    num3 = num1 + num2
    print(num3)
    num3 = num1 * num2
    print(num3)
    num3 = num1 - num2
    print(num3)
    num3 = num1 / num2
    return num3

print(simple_calculator(2,3))

#Problem 2
import geometry
print(geometry.rectangle_area(2,3))
print(geometry.triangle_area(3,1))

#Problem 3

def cel_far():
    Cel=int(input("Enter degree in Celsius "))
    Farenheit =(9/5)*Cel +32
    return Farenheit
def far_cel():
    Far=float(input("Enter degree in Farenheit "))
    Celsius= (Far -32 )/(9/5)
    return Celsius

print(cel_far())
print(far_cel())

#Problem 4

def factorial(n):
    if n<0:
      return False
    elif n== 0:
        return 1
    else:
        factors =n * factorial(n-1)
    return factors

print(factorial(3))

#Problem 5

