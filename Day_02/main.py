# Takes the bill total, tip percentage, and number of people to split the bill
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculations
tip_percentage = tip / 100
tip_total = tip_percentage  * bill
bill_total = bill + tip_total
price_per_person = bill_total / people

# Output
print(f"Every person should pay: ${price_per_person:.2f}")