import pandas as pd
import matplotlib.pyplot as plt

def add_expense(date, category, amount, description):
    # Add a new expense to the CSV file
    new_expense = pd.DataFrame([[date, category, amount, description]],
                                columns=['Date', 'Category', 'Amount', 'Description'])
    try:
        expenses = pd.read_csv('expenses.csv')
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
    except FileNotFoundError:
        expenses = new_expense

    expenses.to_csv('expenses.csv', index=False)

def analyze_expenses():
    # Read and analyze expenses
    try:
        expenses = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        print("No expenses found. Please add expenses first.")
        return

    # Group by category and calculate total amount
    category_summary = expenses.groupby('Category')['Amount'].sum().reset_index()

    # Generate bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(category_summary['Category'], category_summary['Amount'], color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expenses by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()   # ✅ Show in Colab

    # Generate pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(category_summary['Amount'], labels=category_summary['Category'], autopct='%1.1f%%', startangle=140)
    plt.title('Expenses Distribution')
    plt.tight_layout()
    plt.show()   # ✅ Show in Colab

    print("Analysis complete. Charts displayed above.")

if __name__ == "__main__":
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully.")
        elif choice == '2':
            analyze_expenses()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
