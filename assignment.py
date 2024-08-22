
#Ex2.1
import math
from random import random, randint

name = input("Enter your name: ")
print("Hello", name,"!")

#Ex2.2
radius = float(input("Enter your radius: "))
area = math.pi*radius*radius
print("The area of the circle is", area)

#Ex2.3
length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
area = 2*(length+width)
print("The area of the rectangle is", area)

#Ex2.4
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
Sum = num1+num2+num3
product = num1*num2*num3
average = Sum/3
print("The sum is", Sum, "and the product is", product, "and the average is", average)

#Ex2.5
talents = float(input("Enter your number of talents: "))
pounds = float(input("Enter your number of pounds: "))
lots = float(input("Enter your number of lots: "))
totalpounds = (talents*20)+pounds
totallots = (totalpounds*32)+lots
totalgrams = totallots*13.3
kilograms = int(totalgrams/1000)
grams = float(totalgrams%1000)
print(f" The weight in modern units: {kilograms} kilograms and {grams:.2f} grams")
from random import randint

#Ex2.6
num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
num4 = randint(1,6)
num5 = randint(1,6)
num6 = randint(1,6)
num7 = randint(1,6)
print(f"first code is {num1}{num2}{num3}, and second code is {num4}{num5}{num6}{num7}")








