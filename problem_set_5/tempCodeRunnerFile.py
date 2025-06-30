
def main():
    response = input('Fraction: ') # Request fraction
    perc = convert(response) # Convert the fraction and store it in a variable called perc
    print(gauge(perc)) # Print the output from gauge which is powered by the value from perc

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
                else:
                     pass
                
                # Ensure X smaller than Y
                if x < y:
                     pass
                else:
                     raise ValueError("Error: X can't be larger than Y")
                
                # Return the function as an integer
                answer = round(((x / y) * 100))
                return answer
            else:
                raise ValueError('Error: Not a fraction')
            
        except ValueError as e:
            print(f'{e}')
        except ZeroDivisionError as e:
             print(f'{e}')

def gauge(percentage):
    if percentage <= 1:
         return f'E'
    elif percentage >= 99:
         return f'F'
    else:
         return f'{percentage}%'


if __name__ == "__main__":
    main()