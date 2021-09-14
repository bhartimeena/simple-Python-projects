import random
import math
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
x = random.randint(lower, upper)
# print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
 
guees = int(input("Enter your guess "))

if guees==x:
    print("you are hit!")
elif guees>x:
    print("you're guess is too high! ")
elif guees<x:
    print("You're guess is too low!")