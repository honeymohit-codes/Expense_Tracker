amount = float(input("Enter the amount spent:"))
category = input("Enter the category:")
description = input("Enter the description:")
file = open("Expenses.txt", "a")
file.write(str(amount) + "," + category + "," + description + "\n")
file.close()

