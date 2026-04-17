import random
from datetime import datetime

quotes = [
    "Do not save what is left after spending, spend what is left after saving.",
    "Beware of little expenses. A small leak will sink a great ship.",
    "Money grows when you control it.",
    "Every rupee saved is a rupee earned.",
    "Track your money or your money will track you."
]

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Expenses.txt", "a") as file:
        file.write(f"{amount},{category},{description},{date_time}\n")

    print("Expense added successfully!")

def view_expenses():
    try:
        with open("Expenses.txt", "r") as file:
            lines = file.readlines()

        print("\nAmount | Category | Description | Date & Time")
        print("-" * 55)
        for line in lines:
            amount, category, description, date_time = line.strip().split(",")
            print(f"{amount} | {category} | {description} | {date_time}")

    except FileNotFoundError:
        print("No expenses found.")

def total_spending():
    total = 0
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount = float(line.split(",")[0])
                total += amount
        print(f"Total spending: {total}")
    except FileNotFoundError:
        print("No expenses found.")

def clear_expenses():
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        open("Expenses.txt", "w").close()
        print("All expenses cleared!")

def search_by_category():
    cat = input("Enter category to search: ")
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, date_time = line.strip().split(",")
                if category.lower() == cat.lower():
                    print(f"{amount} | {category} | {description} | {date_time}")
    except FileNotFoundError:
        print("No expenses found.")

def search_by_amount(limit):
    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, date_time = line.strip().split(",")
                if float(amount) < limit:
                    print(f"{amount} | {category} | {description} | {date_time}")
    except FileNotFoundError:
        print("No expenses found.")

def daily_budget_check():
    budget = float(input("Enter your daily budget: "))
    today = datetime.now().strftime("%Y-%m-%d")
    spent = 0

    try:
        with open("Expenses.txt", "r") as file:
            for line in file:
                amount, category, description, date_time = line.strip().split(",")
                if today in date_time:
                    spent += float(amount)

        print(f"Today's spending: {spent}")
        if spent > budget:
            print("You crossed your daily budget!")
        else:
            print("You are within budget!")

        print("\n💡 Quote:", random.choice(quotes))

    except FileNotFoundError:
        print("No expenses found.")

# ================= MAIN MENU =================

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Clear All Expenses")
    print("5. Search by Category")
    print("6. Show expenses below 500")
    print("7. Show expenses below 1000")
    print("8. Daily Budget Check")
    print("9. Show a Motivational Quote")
    print("10. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        clear_expenses()

    elif choice == "5":
        search_by_category()

    elif choice == "6":
        search_by_amount(500)

    elif choice == "7":
        search_by_amount(1000)

    elif choice == "8":
        daily_budget_check()

    elif choice == "9":
        print("\n💡 Quote:", random.choice(quotes))

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")