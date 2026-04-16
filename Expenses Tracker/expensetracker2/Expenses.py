while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Clear All Expenses")
    print("4. Show Total Spent")
    print("5. Category Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter the amount spent: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        category = input("Enter the category: ")
        description = input("Enter the description: ")

        with open("Expenses.txt", "a") as file:
            file.write(f"{amount},{category},{description}\n")

        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- All Expenses ---")
        try:
            with open("Expenses.txt", "r") as file:
                lines = file.readlines()

            print("Amount   Category   Description")
            for line in lines:
                amount, category, description = line.strip().split(",")
                print(amount, "  ", category, "  ", description)

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
                    amount, category, description = line.strip().split(",")
                    total += float(amount)

            print(f"\nTotal money spent: ₹{total}")

        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "5":
        category_totals = {}

        try:
            with open("Expenses.txt", "r") as file:
                for line in file:
                    amount, category, description = line.strip().split(",")
                    amount = float(amount)

                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

            print("\n--- Category Summary ---")
            for cat, total in category_totals.items():
                print(f"{cat}: ₹{total}")

        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")