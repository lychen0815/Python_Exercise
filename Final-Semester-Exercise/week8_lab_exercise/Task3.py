'''
Task: Let's write a function calc_bmi(): that asks user to input his/her weight(kg) and height(m) one by one and prints out the BMI of the user. The Body Mass Index(BMI) can be calculated by the following formula:

๐ต๐๐ผ=๐ค๐๐๐โ๐กโ๐๐๐โ๐ก2

The user input is expected to be a float number.
If the user input is not a float number, the function will print "Invalid input."
If the height is 0, the function will print "Height cannot be zero."
No matter the user inputs are valid or not, the function will print out "End." at last.
'''
def calc_bmi():
    weight = input('please enter your weight: ')
    height = input('please enter your height: ')
    try:
        bmi = float(weight) / float(height)
    except ValueError:
        print('Invalid input')
    else:
        print('Your bmi is ', bmi)
    finally:
        print('End.')

calc_bmi()




















