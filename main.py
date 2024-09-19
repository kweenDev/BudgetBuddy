# main.py

import expense_manager
import savings_manager
import income_manager
import analysis
from tests import run_tests


def main():
    """
    Main function to drive the Budget Buddy CLI program.
    """
    print("Welcome to Budget Buddy CLI!")

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Set Savings Goal")
        print("4. Update Savings")
        print("5. Set Budget")
        print("6. Compare Budget vs Expenses")
        print("7. Track Savings Progress")
        print("8. Run Tests")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category: ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            expense_manager.add_expense(category, description, amount)

        elif choice == '2':
            source = input("Enter income source (e.g., Salary): ")
            description = input("Enter description: ")
            amount = float(input("Enter the amount: "))
            income_manager.add_income(source, description, amount)

        elif choice == '3':
            goal = float(input("Enter your savings goal: "))
            savings_manager.set_savings_goal(goal)

        elif choice == '4':
            amount = float(input("Enter the amount to save: "))
            savings_manager.update_savings(amount)

        elif choice == '5':
            budget = float(input("Enter your budget: "))
            analysis.set_budget(budget)

        elif choice == '6':
            analysis.generate_budget_comparison()

        elif choice == '7':
            savings_manager.track_savings_progress()

        elif choice == '8':
            run_tests()

        elif choice == '9':
            print("Thank you for using Budget Buddy CLI. Goodbye!")
            break

        else:
            print("Oh no! That's an invalid choice. Please try again.")


if __name__ == "__main__":
    main()
