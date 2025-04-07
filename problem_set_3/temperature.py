"""

Write a program named temperature.py that converts a temperature from Fahrenheit to Celsius.

-- ✅Prompt the user for a temperature in Fahrenheit.
-- ✅ If the user enters something other than a number, catch the exception and prompt them again.
-- ✅ Ensure the temperature entered is within a realistic range (-100°F to 150°F).
    -- Use assert to enforce this.
-- Print the converted temperature rounded to one decimal place.
-- Use a finally clause to print a friendly message like "Thank you for using the converter!" at the end, regardless of errors.

"""

def main():
    while True:
        try:
            temp = float(input('Please enter a temperature in Fahrenheit: '))
            assert -100 <= temp <= 150
            celcius = ((temp - 32) * 5) / 9
            print(f'Temperature in Celcius: {celcius:.1f}')
            break
        except ValueError as e:
            print('Please enter only numerical values.')
        except AssertionError as e:
            print('Your input temperature is not within acceptable boundaries. Please try again.')
        finally:
            print('Thank you for using the converter.')

main()

