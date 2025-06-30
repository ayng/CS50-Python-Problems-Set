"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, 
-- implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:
"""

"""
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
"""

"""
-- Then output that same date in YYYY-MM-DD format. 
-- If the user’s input is not a valid date in either format, prompt the user again. 
-- Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

# Chat GPT: What are the basic building blocks of typing in Python?
# Tell me about method chaining (already asked and took screenshot)
# Check out the following Git channels: https://github.com/karan/Projects https://github.com/dipakkr/A-to-Z-Resources-for-Students
# See ChatGPT thread for more great channels to follow

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}


def main():
    while True:
        try:
            # Ask the user for input
            date = input('Please enter a date in formats mm-dd-YYYY (i.e.,10/06/1995), or Month Day, Year (i.e., October 6, 1995): ')
            # Determine if path 1
            if date.count('/') == 2:
                month, day, year = date.split('/') # Split if date in path 1 format.

                # Validate month input for path 1
                if month.isnumeric():
                    if len(month) == 1:
                        month = '0' + month
                    elif len(month) == 2:
                        pass
                    else:
                        raise ValueError('Invalid month entry. Not enough characters. Please try again.')
                else:
                    raise ValueError('Invalid month entry. Not numeric. Please try again.')
                
                # Validate day input for path 1
                if day.isnumeric():
                    if len(day) == 1:
                        day = '0' + day
                    elif len(day) == 2:
                        pass
                    else:
                        raise ValueError('Invalid day entry. Too many characters. Please try again.')
                else:
                    raise ValueError('Invalid day entry. Not numeric. Please try again.')
                
                # Validate year input for path 1
                if year.isnumeric():
                    if len(year) == 4:
                        pass
                    else:
                        raise ValueError('Invalid year entry. Not the correct year format. Please try again.')
                else:
                    raise ValueError('Invalid year entry. Not numeric. Please try again.')

                # Print output
                print(f'{year}-{month}-{day}')
                break
            # Determine if path 2
            elif date.startswith(('January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December')):
                month, day, year = date.split(' ')

                # Format the month
                month = month.strip()
                if month in months:
                    month_num = months[month]
                else:
                    raise ValueError('You entered an invalid month date, please try again.')
                
                # Format the day
                day = day.replace(',', '').strip() # remove ',' and whitespace
                if day.isnumeric():
                    day = int(day)
                    if day < 10:
                        day_num = '0' + str(day)
                    elif 10 >= day <= 31:
                        day_num = str(day)
                    elif day > 31:
                        raise ValueError('You entered an invalid day date, please try again.')
                else:
                    raise ValueError('Your day date is not numeric.')
                
                # Format the year                    
                if year.isnumeric():
                    if len(year) == 4:
                        year = str(year)
                    else:
                        raise ValueError('Invalid year format. Please try again.')
                else:
                    raise ValueError('Your year date is not numeric.')
                
                # Print the output
                print(f'{year}-{month_num}-{day_num}')
                break

            else:
                raise ValueError('Please enter a valid date format.')
            
        except ValueError as e:
            print(f'Error: {e}')

main()



