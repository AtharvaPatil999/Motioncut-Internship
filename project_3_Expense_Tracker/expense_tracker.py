import data_storage
import analysis

def main():
    data_storage.init_db()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. View Category-wise Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport, Bills): ")
            description = input("Enter description: ")
            data_storage.add_expense(date, amount, category, description)
            print("Expense added successfully!")
        
        elif choice == '2':
            expenses = data_storage.fetch_expenses()
            print("\nAll Expenses:")
            for exp in expenses:
                print(exp)
        
        elif choice == '3':
            analysis.generate_monthly_summary()
        
        elif choice == '4':
            analysis.generate_category_summary()
        
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
