from datetime import datetime

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Clear All Expenses")
    print("4. Show Total Spent")
    print("5. Category Summary")
    print("6. Exit")
    print("7. View Date & Time")
    print("8. Search by Category")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter the amount spent: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        category = input("Enter the category: ")
        description = input("Enter the description: ")
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("Expenses.txt", "a") as file:
            file.write(f"{amount},{category},{description},{date_time}\n")

        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- All Expenses ---")
        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description, date_time = line.strip().split(",")
                    print(amount, " ", category, " ", description)
        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "3":
        confirm = input("Are you sure? This will delete all data (yes/no): ")
        if confirm == "yes":
            open("Expenses.txt", "w").close()
            print("All expenses cleared!")

    elif choice == "4":
        total = 0
        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description, date_time = line.strip().split(",")
                    total += float(amount)
            print(f"\nTotal money spent: ₹{total}")
        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "5":
        category_totals = {}
        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description, date_time = line.strip().split(",")
                    amount = float(amount)
                    category_totals[category] = category_totals.get(category, 0) + amount

            print("\n--- Category Summary ---")
            for cat, total in category_totals.items():
                print(f"{cat}: ₹{total}")
        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "7":
        print("\n--- Expenses with Date & Time ---")
        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description, date_time = line.strip().split(",")
                    print(amount, " ", category, " ", description, " ", date_time)
        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "8":
        search_cat = input("Enter category to search: ")
        print(f"\n--- Expenses for {search_cat} ---")
        found = False
        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description, date_time = line.strip().split(",")
                    if category.lower() == search_cat.lower():
                        print(amount, " ", category, " ", description)
                        found = True

            if not found:
                print("No expenses found for this category.")
        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")