#!python
"""
Group Exercises: Section 1 Exercise 1

Celsius can be converted to Fahrenheit as follows F=(°C × 95)+32.

(a) Calculate the smelting (0C) and boiling (100C) points of water at 1 atm in Fahrenheit
(b) Write a program which takes a temperature in Celsius and converts it to Fahrenheit

Make sure you display the result to the user!


DISCLAIMER:
This is only ONE way of solving the problem.
There are many different ways that you can approach this problem and achieve the same goal!

"""
## Part (a)

# Use formula to calculate values
tempZero = (0 * (9 / 5) + 32)
tempOneHundred = (100 * (9 / 5) + 32)

# Print results
# Remember to convert integers to strings!
print("0C = " + str(tempZero) + "F")
print("100C = " + str(tempOneHundred) + "F")

# Obtain temperature in °C from the user
# Note: A type conversion (String -> Int) is required
#define Celsius
Celsius = int(input("please enter a celsius: "))
Fahrenheit = (Celsius * (9 / 5))+ 32
print(Fahrenheit)