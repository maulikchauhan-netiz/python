# Expense Tracker

from datetime import datetime

# Greeting
hour = datetime.now().hour

if 5 <= hour < 12:
    print("----------🌅 Good Morning! MAULIK----------")
elif 12 <= hour < 17:
    print("----------☀️ Good Afternoon! MAULIK----------")
elif 17 <= hour < 21:
    print("----------🌇 Good Evening! MAULIK----------")
else:
    print("----------🌙 Good Night! MAULIK----------")

print("\nWelcome to Expense Tracker, Maulik!\n")

# Store all expenses
expenses = []

while True:
    print("\n========== MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choose = int(input("Choose an option: "))

    # ---------------- Add Expense ----------------
    if choose == 1:
        print("\n---------- Add Expense ----------")

        date = input(datetime.now().strftime("%d-%m-%Y"))
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: ₹"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("✅ Expense added successfully!")

    # ---------------- View Expenses ----------------
    elif choose == 2:
        print("\n---------- All Expenses ----------")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(f"""
Date        : {expense['date']}
Category    : {expense['category']}
Description : {expense['description']}
Amount      : ₹{expense['amount']}
-----------------------------
""")

    # ---------------- Total Spending ----------------
    elif choose == 3:
        print("\n---------- Total Spending ----------")

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Spending: ₹{total}")

    # ---------------- Exit ----------------
    elif choose == 4:
        print("\n👋 Thank you for using Expense Tracker!")
        break

    # ---------------- Invalid Choice ----------------
    else:
        print("❌ Invalid option! Please try again.")