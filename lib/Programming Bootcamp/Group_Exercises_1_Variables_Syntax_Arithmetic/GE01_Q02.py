"""
Pizzas are measured using the diameter and can be Small (25cm), Medium (30cm), Large (35cm), or X-Large (40cm). Assume circular pizza. The area of a circle is
a.Calculate the area of each of the pizzas
b.Write a program that takes in a size of pizza (in cm) and returns the area of the pizza
	Remember that radius is half of the diameter!
	Make sure you display the result to the user!
"""

#Part(a)

#import math and use "π"
import math
mathPI = math.pi
#Calculate area using formula
small_area = int(mathPI * (25 / 2) ** 2)
#print result
print("Area of Small Pizza is " + str(small_area) + "cm^2")

##part(B)

#input diameter value
pizza_diameter = int(input("please enter a diameter>>>"))

#convert diameter to radius
pizza_radius = (1 / 2) * pizza_diameter

#circle formula
pizza_area = int(mathPI * (pizza_radius ** 2))

#print result
print("Area of " + str(pizza_diameter) + "cm pizza is " + str(pizza_area))
