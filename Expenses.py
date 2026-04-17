import os
import hashlib
import datetime
import random

EXPENSE_FILE = "Expenses.txt"
PASS_FILE = "pass.key"

# ---------------- PASSWORD SYSTEM ---------------- #

def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

def set_password():
    p = input("Set new password: ")
    with open(PASS_FILE, "w") as f:
        f.write(hash_pass(p))
    print("Password set!\n")

def check_password():
    if not os.path.exists(PASS_FILE):
        set_password()

    p = input("Enter password: ")
    with open(PASS_FILE, "r") as f:
        real = f.read()

    if hash_pass(p) == real:
        print("Access granted!\n")
    else:
        print("Wrong password!")
        exit()

def change_password():
    old = input("Enter old password: ")
    with open(PASS_FILE, "r") as f:
        real = f.read()

    if hash_pass(old) == real:
        set_password()
    else:
        print("Wrong old password!\n")

# ---------------- QUOTES ---------------- #

quotes = [
    "Money saved is money earned.",
    "Track today, relax tomorrow.",
    "Small savings make big wealth.",
    "Be smarter than your expenses.",
    "Every rupee matters.",
    "Control money or it controls you."
]

def show_quote():
    print("\n💡", random.choice(quotes), "\n")

# ---------------- EXPENSE FUNCTIONS ---------------- #

def add_expense():
    try:
        amount = float(input("Amount: "))
    except:
        print("Invalid amount!\n")
        return

    category = input("Category: ")
    desc = input("Description: ")
    dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{amount},{category},{desc},{dt}\n")

    print("Expense added!\n")

def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No data.\n")
        return

    with open(EXPENSE_FILE) as f:
        for line in f:
            a,c,d,dt = line.strip().split(",")
            print(f"₹{a} | {c} | {d}")

def view_with_dt():
    if not os.path.exists(EXPENSE_FILE):
        print("No data.\n")
        return

    with open(EXPENSE_FILE) as f:
        for line in f:
            a,c,d,dt = line.strip().split(",")
            print(f"₹{a} | {c} | {d} | {dt}")

def total_spent():
    total = 0
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                a = float(line.split(",")[0])
                total += a
    print(f"\nTotal Spent: ₹{total}\n")

def search_category():
    cat = input("Enter category: ")
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                if cat.lower() in line.lower():
                    print(line.strip())
    print()

def below_limit(limit):
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                a = float(line.split(",")[0])
                if a < limit:
                    print(line.strip())
    print()

def budget_check():
    budget = float(input("Enter daily budget: "))
    total = 0
    today = datetime.datetime.now().strftime("%d-%m-%Y")

    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE) as f:
            for line in f:
                a,c,d,dt = line.strip().split(",")
                if today in dt:
                    total += float(a)

    print(f"Today spent: ₹{total}")
    if total > budget:
        print("⚠️ Budget exceeded!\n")
    else:
        print("Within budget 👍\n")

def clear_all():
    confirm = input("Type YES to confirm: ")
    if confirm == "YES":
        open(EXPENSE_FILE, "w").close()
        print("All data cleared!\n")

def highest_expense():
    if not os.path.exists(EXPENSE_FILE):
        print("No data.\n")
        return

    max_line = None
    max_amt = 0

    with open(EXPENSE_FILE) as f:
        for line in f:
            a = float(line.split(",")[0])
            if a > max_amt:
                max_amt = a
                max_line = line.strip()

    print("\n🏆 Highest Expense:")
    print(max_line, "\n")

# ---------------- MAIN MENU ---------------- #

check_password()

while True:
    print("""
====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. View with Date & Time
4. Total Spent
5. Search by Category
6. Expenses below ₹500
7. Expenses below ₹1000
8. Daily Budget Check
9. Clear All Expenses
10. Show Motivational Quote
11. Change Password
12. Show Highest Expense
13. Exit
""")

    ch = input("Choice: ")

    if ch == "1": add_expense()
    elif ch == "2": view_expenses()
    elif ch == "3": view_with_dt()
    elif ch == "4": total_spent()
    elif ch == "5": search_category()
    elif ch == "6": below_limit(500)
    elif ch == "7": below_limit(1000)
    elif ch == "8": budget_check()
    elif ch == "9": clear_all()
    elif ch == "10": show_quote()
    elif ch == "11": change_password()
    elif ch == "12": highest_expense()
    elif ch == "13":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")