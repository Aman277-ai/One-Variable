import SpaceRemover,Calculations
import os

os.system("cls")

inputStr = input("Enter the equation with only one variable:")
spaceRemovedStr = SpaceRemover.spaceRemover(inputStr)
operatorOfVar : str = Calculations.calculations(spaceRemovedStr)[1]
answer = Calculations.calculations(spaceRemovedStr)[0]
if operatorOfVar == '-':
            answer *= -1
if operatorOfVar == '/':
            answer = 1 / answer
print(answer)