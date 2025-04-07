def main():
    while True:
        try:
            date = input('Please enter a date in formats mm-dd-YYYY (i.e.,10/06/1995), or Month Day, Year (i.e., October 6, 1995): ')
            if date.count('/') == 2:
                print('Correct')
            elif date.startswith(('January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December')):
                valid_month = date.startswith(('January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'))
                print(valid_month)
        except:
            pass

main()