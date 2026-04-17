import random
from datetime import datetime

FILE_NAME = "Expenses.txt"

quotes = [
    "Money saved is money earned.",
    "Track today, relax tomorrow.",
    "Control money, or money will control you.",
    "Every rupee has a purpose.",
    "Think before you spend.",
    "Financial discipline is a superpower.",
    "Track. Save. Grow.",
]

def show_quote():
    print("\n💡 Quote:", random.choice(quotes))


def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid number.")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category},{description},{now}\n")

    print("✅ Expense added!")
    show_quote()


def read_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip().split(",") for line in file]
    except FileNotFoundError:
        return []


def view_expenses():
    data = read_expenses()
    if not data:
        print("No expenses found.")
        return

    print("\nAmount | Category | Description")
    for amount, category, description, _ in data:
        print(amount, "|", category, "|", description)


def view_with_datetime():
    data = read_expenses()
    if not data:
        print("No expenses found.")
        return

    print("\nAmount | Category | Description | Date & Time")
    for amount, category, description, dt in data:
        print(amount, "|", category, "|", description, "|", dt)


def total_spent():
    data = read_expenses()
    total = sum(float(entry[0]) for entry in data)
    print(f"\n💰 Total spent: ₹{total}")


def search_category():
    data = read_expenses()
    cat = input("Enter category to search: ")

    for amount, category, description, dt in data:
        if category.lower() == cat.lower():
            print(amount, "|", category, "|", description, "|", dt)


def below_amount(limit):
    data = read_expenses()
    print(f"\nExpenses below ₹{limit}")
    for amount, category, description, dt in data:
        if float(amount) < limit:
            print(amount, "|", category, "|", description, "|", dt)


def daily_budget_check():
    data = read_expenses()
    today = datetime.now().strftime("%d-%m-%Y")

    total_today = 0
    for amount, _, _, dt in data:
        if today in dt:
            total_today += float(amount)

    print(f"\nToday's spending: ₹{total_today}")

    if total_today > 1000:
        print("⚠️ You crossed ₹1000 today! Control spending!")
    elif total_today > 500:
        print("⚠️ You crossed ₹500 today! Be careful!")
    else:
        print("✅ Good control today!")


def clear_expenses():
    confirm = input("Delete all expenses? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("All data cleared.")


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
    print("10. Show Motivational Quote")
    print("11. Exit")

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
        below_amount(500)
    elif choice == "7":
        below_amount(1000)
    elif choice == "8":
        daily_budget_check()
    elif choice == "9":
        clear_expenses()
    elif choice == "10":
        show_quote()
    elif choice == "11":
        break
    else:
        print("Invalid choice.")