# Tip Calculator

# Concept: Parsing and converting string inputs.

"""
Practice Problems:
1.	Sales Tax Calculator
Write a program sales_tax.py that accepts a price as a string (e.g., $100.50) and a sales tax rate as a percentage string (e.g., 5%). Calculate the total price after tax.
Example:
Input: Price: $100.50, Tax: 5%
Output: Total: $105.53
"""

def main():
    price = dollars_to_float(input("Price: "))
    tax = percent_to_float(input("Tax: "))
    total = price + ((price * tax) / 100)
    print(f"Total: {total:.2f}")

def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    p = p.replace("%", "")
    return float(p)

main()


"""
2.	Currency Converter
Write a program currency_converter.py that accepts an amount in dollars (e.g., $50.00) and converts it to euros at a given exchange rate (e.g., 1 USD = 0.85 EUR).
Example:
Input: Amount: $50.00, Exchange rate: 0.85
Output: Converted amount: 42.5 EUR
"""

def main():
    dollars = dollars_converted(input("Amount: "))
    exchange_rate = float(input("Exchange Rate: "))
    converted_amount = dollars * exchange_rate
    print(f"Converted Amount: {converted_amount:.2f} EUR")

def dollars_converted(d):
    d = d.replace("$", "")
    return float(d)

main()

"""
3.	Percentage Increase Calculator
Write a program percent_increase.py that accepts an initial amount and a percentage increase, then calculates the new amount.
Example:
Input: Initial amount: $200, Increase: 10%
Output: New amount: $220
"""

def main():
    initial_amount = amount_converted(input("Initial amount: "))
    increase = increase_converted(input("Increase: "))
    new_amount = initial_amount + (initial_amount * increase)
    print(f"New amount: {new_amount:.2f}")

def amount_converted(d):
    d = d.replace("$","")
    return float(d)

def increase_converted(i):
    i = i.replace("%", "")
    return float(i)/100

main()