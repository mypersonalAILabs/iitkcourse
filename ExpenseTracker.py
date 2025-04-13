import csv
from datetime import datetime

# Global variables
expenses = []
monthly_budget = 0
filename = "expenses.csv"

def add_expense():
    print("\nAdd New Expense")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    category = input("Enter category (e.g., Food, Travel): ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    description = input("Enter description: ").strip()
    
    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("\nNo expenses to display.")
        return
    
    print("\nAll Expenses:")
    print("-" * 60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | Description")
    print("-" * 60)
    
    for expense in expenses:
        try:
            print(f"{expense['date']:<12} | {expense['category']:<15} | ${expense['amount']:<9.2f} | {expense['description']}")
        except KeyError:
            print("Skipping invalid expense entry")
    print("-" * 60)

def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("\nEnter your monthly budget: $"))
        print(f"Budget set to ${monthly_budget:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def track_budget():
    if monthly_budget <= 0:
        print("\nPlease set your monthly budget first.")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    remaining = monthly_budget - total
    
    print("\nBudget Tracking:")
    print(f"Total expenses: ${total:.2f}")
    print(f"Monthly budget: ${monthly_budget:.2f}")
    
    if total > monthly_budget:
        print("⚠️ Warning: You have exceeded your budget!")
    else:
        print(f"You have ${remaining:.2f} left for the month.")

def save_expenses():
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"\nExpenses saved to {filename}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses():
    global expenses
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
            # Convert amount to float
            for expense in expenses:
                expense['amount'] = float(expense['amount'])
        print(f"\nExpenses loaded from {filename}")
    except FileNotFoundError:
        print("\nNo saved expenses found. Starting fresh.")
    except Exception as e:
        print(f"Error loading expenses: {e}")

def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Monthly Budget")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")

def main():
    load_expenses()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_expenses()  # Auto-save before exit
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
