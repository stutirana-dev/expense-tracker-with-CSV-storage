import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: ₹"))

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Category", "Amount"])

        writer.writerow([category, amount])

    print("Expense saved successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    total = 0

    print("\n--- Your Expenses ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["Amount"])
            print(f"{row['Category']}: ₹{amount:.2f}")
            total += amount

    print(f"Total expenses: ₹{total:.2f}\n")


def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


main()