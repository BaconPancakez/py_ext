import automation as am
import pyvelp as pv
import scraping as s


# Display a simple menu for the user to choose from
print("Select an option:")
print("1. Automation")
print("2. Pyvelp")
print("3. Scraping")

# Get the user's choice
choice = int(input('Which one would you like to select? '))

# Based on the user's choice, call the corresponding function
if choice == 1:
    print('running automation....')
    am.automation()
elif choice == 2:
    print('running pv_velp task....')
    pv.pyvelp()
elif choice == 3:
    print('running web scraping...')
    s.scraping()
else:
    print("Invalid choice. Please select 1, 2, or 3.")
