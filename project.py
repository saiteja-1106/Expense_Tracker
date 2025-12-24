       
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense(date, category, amount):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)

        # add header only once
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])

        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_all_expenses():
    total_amount = 0

    if not os.path.isfile(FILE_NAME):
        print("No expenses found.\n")
        return

    print("\nDate        Category        Amount")
    print("-" * 35)

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            if len(row) != 3:
                continue

            print(f"{row[0]}   {row[1]}        {row[2]}")
            total_amount += float(row[2])

    print("-" * 35)
    print("Total Amount:", total_amount, "\n")


def main():
    while True:
        print(":: Welcome to Expense Tracker ::")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = datetime.now().strftime("%Y-%m-%d")
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(date, category, amount)

        elif choice == "2":
            view_all_expenses()

        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

