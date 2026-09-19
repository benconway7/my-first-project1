# My First Python program 
name = input ("what is your name? ")
print (f"hello, {name}! Welcome to Engineering Python.")

# calculate the area of a circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(f"The area of the circle is: {area}") 

# calculate the length of the hypotenuse of a right triangle
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.hypot(a, b)
print(f"The length of the hypotenuse is: {c}")