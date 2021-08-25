'''
1.Write a function that takes the temperature in Celsius and converts it to Fahrenheit.
'''

def C2F(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit

temp_celsius = int(input("Please enter a temperature in °C >>>"))

temp_fahrenheit = C2F(temp_celsius)

print("Temperature = " + str(temp_celsius) + "°C")
print("Temperature = " + str(temp_fahrenheit) + "°F")

