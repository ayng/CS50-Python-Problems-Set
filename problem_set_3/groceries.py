"""

Suppose that you’re in the habit of making a list of items you need from the grocery store.

- ✅ In a file called grocery.py, implement a program that prompts the user for items, one per line, 
- ✅ until the user inputs control-d (which is a common way of ending one’s input to a program). 
- ✅ Then output the user’s grocery list in all uppercase, 
- ✅ sorted alphabetically by item, 
- ✅ prefixing each line with the number of times the user inputted that item. 
- ✅ No need to pluralize the items. 
- ✅ Treat the user’s input case-insensitively.

"""

def main():
    empty_dict = {}
    while True:
        try:
            item = input('Please enter a grocery item: ').lower()
            if item not in empty_dict:
                empty_dict[item] = 1
                print('You just added a new entry to your dictionary.')
            else:
                empty_dict[item] += 1
                print('This existing entry has been updated')
            





        except EOFError:
            for key, value in sorted(empty_dict.items()):
                print(f'{value} {key.upper()}')
            #for key, value in empty_dict.items():
            #    print(f'{value} {key.upper()}')
            break

main()