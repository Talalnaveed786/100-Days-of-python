print("Welcome to the tip calcultor")
bill = 0
total_bill=input("What was the total bill")
bill = bill + float(total_bill) 
percent= input("What percentage tip would you like to give? 10, 12 or 15?")
new_percent = float(percent) / 100
bill = ((bill * new_percent) + bill) 
split_bill= input("How many people to split the bill?")
bill = bill / float(split_bill)
round_bill = round(bill,2)


print(f"Your total bill is {round_bill} ")

