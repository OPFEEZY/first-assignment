print("welcome to tip calculator")
bill = int(input("what is the total bill? $ "))
tip = int(input("how much tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the bill? "))


tip_as_percent = tip / 150
total_tip = bill * tip_as_percent
total_bill = bill * total_tip
bill_per_person = total_bill / people
print(round(bill_per_person))
