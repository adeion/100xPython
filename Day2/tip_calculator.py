print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $ "))
tip = float(input("How much tip would you like to give - 10, 12, or 15? ")) 
people = int(input("How many people will split the bill? "))
amount =  (((tip * bill)/100) + bill)/ people
print("Each person should pay $%.2f"%amount)