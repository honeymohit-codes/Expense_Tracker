import random
from datetime import datetime


# -------- Quote from file --------
def show_quote():
    try:
        with open("quotes.txt", "r") as file:
            quotes = file.readlines()
        print("\n💡 Quote:", random.choice(quotes).strip())
    except FileNotFoundError:
        print("\n💡 Stay motivated and track expenses!")


# -------- Add Expense --------
def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid number!")
        return

    category = input("Enter the category: ")
    description = input("Enter the description: ")
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("Expenses.txt", "a") as file:
        file.write(f"{amount},{category},{description},{date_time}\n")

    print("✅ Expense added!")


# -------- View Expenses --------
def view_expenses():
    print("\n--- Expenses ---")
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, dt = line.strip().split(",")
                print(amount, "|", category, "|", description)
    except FileNotFoundError:
        print("No expenses found.")


# -------- View with Date & Time --------
def view_with_datetime():
    print("\n--- Expenses with Date & Time ---")
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, dt = line.strip().split(",")
                print(amount, "|", category, "|", description, "|", dt)
    except FileNotFoundError:
        print("No expenses found.")


# -------- Total Spent --------
def total_spent():
    total = 0
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                total += float(line.split(",")[0])
        print(f"\n💰 Total spent: ₹{total}")
    except FileNotFoundError:
        print("No data found.")


# -------- Search by Category --------
def search_category():
    search = input("Enter category to search: ")
    try:
        with open("Expenses.txt", "r") as file:
            found = False
            for line in file:
                amount, category, description, dt = line.strip().split(",")
                if category.lower() == search.lower():
                    print(amount, "|", category, "|", description, "|", dt)
                    found = True
            if not found:
                print("No matching category found.")
    except FileNotFoundError:
        print("No data found.")


# -------- Expenses Below 500 --------
def below_500():
    print("\n--- Expenses Below ₹500 ---")
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, dt = line.strip().split(",")
                if float(amount) < 500:
                    print(amount, "|", category, "|", description, "|", dt)
    except FileNotFoundError:
        print("No data found.")


# -------- Expenses Below 1000 --------
def below_1000():
    print("\n--- Expenses Below ₹1000 ---")
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, dt = line.strip().split(",")
                if float(amount) < 1000:
                    print(amount, "|", category, "|", description, "|", dt)
    except FileNotFoundError:
        print("No data found.")


# -------- Daily Budget Check --------
def budget_check():
    total = 0
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                total += float(line.split(",")[0])

        if total < 500:
            print("🟢 Under ₹500. Great control!")
        elif total < 1000:
            print("🟡 Between ₹500 and ₹1000. Be careful!")
        else:
            print("🔴 Above ₹1000! Slow down!")

    except FileNotFoundError:
        print("No data found.")


# -------- Highest Expense --------
def highest_expense():
    highest = 0
    record = ""

    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount = float(line.split(",")[0])
                if amount > highest:
                    highest = amount
                    record = line.strip()

        if record:
            amount, category, description, dt = record.split(",")
            print("\n⭐ Highest Expense:")
            print(amount, "|", category, "|", description, "|", dt)
        else:
            print("No expenses found.")

    except FileNotFoundError:
        print("No data found.")


# -------- Clear Expenses --------
def clear_expenses():
    confirm = input("Delete all data? (yes/no): ")
    if confirm.lower() == "yes":
        open("Expenses.txt", "w").close()
        print("All data cleared.")


# -------- Main Menu --------
while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View with Date & Time")
    print("4. Total Spent")
    print("5. Search by Category")
    print("6. Expenses below ₹500")
    print("7. Expenses below ₹1000")
    print("8. Daily Budget Check")
    print("9. Clear All Expenses")
    print("10. Show Highest Expense")
    print("11. Show Motivational Quote")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_with_datetime()
    elif choice == "4":
        total_spent()
    elif choice == "5":
        search_category()
    elif choice == "6":
        below_500()
    elif choice == "7":
        below_1000()
    elif choice == "8":
        budget_check()
    elif choice == "9":
        clear_expenses()
    elif choice == "10":
        highest_expense()
    elif choice == "11":
        show_quote()
    elif choice == "12":
        break
    else:
        print("Invalid choice.")