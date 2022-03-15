import SpaceRemover,Calculations
import os
os.system("cls")

inputStr = input("Enter the equation with only one variable: ")
spaceRemovedStr = SpaceRemover.spaceRemover(inputStr)
answer = Calculations.calculations(spaceRemovedStr)
print(answer)