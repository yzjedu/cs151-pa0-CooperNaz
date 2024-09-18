# Programmers:  Cooper Nazar
# Course:  CS151, Professor Yalew
# Due Date: 9/18/2024
# Programming Assignment:  PA 00
# Problem Statement:  Calculate the approximate volume of a cup to substitute for measuring cups.
# Data In: Height and radius in centimeters.
# Data Out:  Approximate volume in milliliters, as well as the number of cups.
# Credits (1): Volume of a Cylinder |Formula, Derivation, Surface Area and Examples (byjus.com)
# Credits (2): 100,000 Digits of Pi (uiuc.edu)
# Credits (3): How Many Milliliters in One Cup? A Complete Measurement Conversion Guide - 2024 - MasterClass

#Provide the purpose of the program.
print("This program calculates the approximate volume of a cup.")
print("Use a cylindrical cup for the most accurate results.")

#Prompt the user to input values for radius and height.
cylinder_height = float(input("Enter the height of the cup in centimeters: "))
cylinder_radius = float(input("Enter the radius of the cup in centimeters: "))
pi = 3.141592653589793

#Calculate the volume of the cup.
cylinder_volume = cylinder_height * (cylinder_radius ** 2) * pi
cylinder_volume = float(cylinder_volume)

#Calculate the number of cups (measurement) the cup can hold.
cup_measure = float(cylinder_volume / 236)

#Round the outputs to two decimal places.
cylinder_volume = f'{cylinder_volume:.2f}'
cup_measure = f'{cup_measure:.2f}'

#Output the volume in milliliters and how many cups (measurement) the cup can hold.
print("The cup can hold around", cylinder_volume, "milliliters maximum.")
print("The cup can hold around", cup_measure, "cups maximum.")