
def add_expense(expenses, description, amount, budget):
    expenses.append({"Description": description, "Amount": amount})
    for expense in expenses:
        budget = budget - expense["Amount"]
        print(f"Added expense: {description}, Amount: {amount}\nBalance: {budget}")

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("expenses:")
    i = 1
    for expense in expenses:
        budget = budget - expense["Amount"]
        print(f"{i}- {expense["Description"]} => -{expense["Amount"]} => Balance: {budget}\n")
        i = i + 1

def main():
    initial_budget = float(input("Enter your budget: "))
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount, budget)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting budget app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter again")

main()