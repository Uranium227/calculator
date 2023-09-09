"""
Calculator for python 3


"""


import math

while True:
     try:
          function = int(input("""
                           1 +
                           2 -
                           3 *
                           4 /
                           Choose one: 
                           """))
          if(function >= 5 or function<=0):
               print("Write a number in 1 - 4")
          else:
               break
     except ValueError:
          print("Write a number")

while True:          
     try:
          firstNumber = float(input("Write First Number"))
          break
     except ValueError:
          print("Write a Number")
          
while True:
     try:
          secondNumber = float(input("Write Second Number"))
          break
     except ValueError:
          print("Write a Number")
          
          
if(function == 1):
     print(firstNumber+secondNumber)
     
elif(function == 2):
     print(firstNumber-secondNumber)

elif(function == 3):
     print(firstNumber*secondNumber)
     
elif(function == 4):
     if(secondNumber != 0):
          print(firstNumber/secondNumber)
     else:
          print("No number can be divided by 0")


