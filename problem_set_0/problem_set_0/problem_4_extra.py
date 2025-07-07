# Einstein’s E = mc²

# Concept: Mathematical operations and user input/output.

"""
Practice Problems:
1.	Kinetic Energy Calculator

Write a program kinetic_energy.py that calculates the kinetic energy of an object given its mass and velocity. 
The formula is  KE = \frac{1}{2}mv^2 . Prompt the user for mass and velocity as integers.
Example:
Input: mass: 10, velocity: 2
Output: Kinetic energy: 20 Joules
"""

m = int(input("Enter mass: "))
v = int(input("Enter velocity: "))
k = int((1/2) * m * (v**2))
print(f"Kinetic energy: {k} Joules")

"""
2.	Body Mass Index (BMI) Calculator

Write a program bmi_calculator.py that calculates BMI using the formula  BMI = \frac{weight}{height^2} , where weight is in kilograms and height is in meters. 
Prompt the user for weight and height and output the BMI.
Example:
Input: weight: 70, height: 1.75
Output: BMI: 22.86
"""

w = int(input("Enter weight: "))
h = float(input("Enter height: "))
bmi = (w / (h**2))
print(f"BMI: {bmi:.2f}")

"""
3.	Convert Light Years

Write a program light_years.py that converts a distance in light-years to kilometers. Assume  1 \, \text{light-year} = 9.46 \times 10^{12} \, \text{km} . 
Prompt the user for a distance in light-years and output the distance in kilometers.
"""

l = int(input("Distance in light-years: "))
km = l * (9.46 * (10**12))
print(f"{l} ligh-years in KM is {km:,.0f}")