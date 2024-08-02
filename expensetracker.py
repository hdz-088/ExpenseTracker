# -------------- HDz ---------------!
# Title: Basic Expense Tracker Program
# Author: HDz(https://github.com/hdz-088/)
# Date of Creation: 2024-04-23
# Last Update: 2024-04-23
# --------------- === ---------------!

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
        
class ExpenseTracker:
    def __init__(self):
        self.expense = []
        
    def add_expense(self, expense):
        self.expense.append(expense)
        
    def remove_expense(self, index):
        if 0 <= index < len(self.expense):
            del self.expense[index]
            print("Expense removed successfully")
        else:
            print("Invalid expense index.")
            
    def view_expenses(self):
        if len(self.expense) == 0:
            print("No expenses found")
        else:
            print("Expense list:")
            for i, expense in enumerate(self.expense, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ₹{expense.amount:.2f} ")
                
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expense)
        print(f"Total Expense: ₹{total:.2f}")
        
def main():
    tracker = ExpenseTracker()
        
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expenses")
        print("2. Remove Expenses")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")
            
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            description = input("Enter the Description: ")
            amount = float(input("Enter the Amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense Logged Successfully")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
            print("Expense Removed Successfully")
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Input! Try Again.")
                
if __name__ == "__main__":
    main()