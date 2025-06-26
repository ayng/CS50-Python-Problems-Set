"""

In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

- convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage 
    rounded to the nearest int between 0 and 100, inclusive. 
- If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. 
- If Y is 0, then convert should raise a ZeroDivisionError.

- gauge expects an int and returns a str that is:
    "E" if that int is less than or equal to 1,
    "F" if that int is greater than or equal to 99,
    and "Z%" otherwise, wherein Z is that same int.

"""

def main():
    try:
        response = input("Fraction: ")
        perc = convert(response)
        print(gauge(perc))
    except (ValueError, ZeroDivisionError) as e:
        print(e)
    
    # My original response below
    # response = input('Fraction: ') # Request fraction
    # perc = convert(response) # Convert the fraction and store it in a variable called perc
    # print(gauge(perc)) # Print the output from gauge which is powered by the value from perc

# Goal: Return the response as a percentage
def convert(fraction):
        try:
            if fraction.count('/') == 1: # Verify a fraction was entered
                x, y = fraction.split('/') # Split the fraction into X and Y

                # Convert X to integer
                if x.isnumeric():
                     x = int(x)
                else:
                     raise ValueError('Error: Value X is not numeric.')
                
                # Convert Y to integer
                if y.isnumeric():
                     y = int(y)
                else:
                     raise ValueError('Error: Value Y is not numeric.')
                
                # Ensure Y is not Zero
                if y == 0:
                     raise ZeroDivisionError("Error: Y can't be zero.")

                
                # Ensure X smaller than Y
                if x <= y:
                     pass
                else:
                     raise ValueError("Error: X can't be larger than Y")
                
                # Return the function as an integer
                answer = round(((x / y) * 100))
                return answer
            else:
                raise ValueError('Error: Not a fraction')
            
        except ValueError as e:
            raise
        except ZeroDivisionError as e:
             raise

def gauge(percentage):
    if percentage <= 1:
         return f'E'
    elif percentage >= 99:
         return f'F'
    else:
         return f'{percentage}%'

if __name__ == "__main__":
    main()