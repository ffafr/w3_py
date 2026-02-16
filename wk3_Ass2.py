class Category:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.spent = 0

class FinanceApp:
    def __init__(self):
        self.categories = {}
        self.balance = 0

    def add_category(self, name, budget):
        self.categories[name] = Category(name, budget)

    def log_transaction(self, amount, cat_name, is_income=False):
        if cat_name not in self.categories:
            self.add_category(cat_name, 0)

        if is_income:
            self.balance += amount
            print(f"Successfully added ${amount} to balance.")
        else:
            self.balance -= amount
            self.categories[cat_name].spent += amount
            print(f"Recorded expense of ${amount} in {cat_name}.")
            
            # Budget Check
            cat = self.categories[cat_name]
            if cat.budget > 0 and cat.spent > cat.budget:
                print(f"⚠️  ALERT: Over budget in {cat_name} by ${cat.spent - cat.budget}!")

    def show_report(self):
        print("\n--- FINANCIAL SUMMARY ---")
        print(f"Current Balance: ${self.balance}")
        print("-" * 25)
        for name, cat in self.categories.items():
            budget_str = f"Budget: ${cat.budget}" if cat.budget > 0 else "No Budget"
            print(f"{name.upper()}: Spent ${cat.spent} | {budget_str}")
        print("-" * 25)

# --- TERMINAL INTERFACE ---

app = FinanceApp()

print("Welcome to your Personal Finance Tracker!")

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Set/Update Category Budget")
    print("4. View Report")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        try:
            amt = float(input("Enter income amount: "))
            desc = input("Enter source (e.g., Salary): ")
            app.log_transaction(amt, desc, is_income=True)
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "2":
        try:
            amt = float(input("Enter expense amount: "))
            cat = input("Enter category (e.g., Food, Rent): ")
            app.log_transaction(amt, cat, is_income=False)
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "3":
        cat_name = input("Enter category name: ")
        try:
            budget_amt = float(input(f"Enter monthly budget for {cat_name}: "))
            app.add_category(cat_name, budget_amt)
            print(f"Budget for {cat_name} set to ${budget_amt}")
        except ValueError:
            print("Invalid budget amount.")

    elif choice == "4":
        app.show_report()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")