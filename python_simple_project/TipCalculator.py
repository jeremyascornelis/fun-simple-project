# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person shoud pay (150.00 / 5) * 1.12
# 1 -> 150, 0.12 -> 0.12 di atas itu (cara cepat)
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

print(f"Each person should pay: ${final_amount}")
