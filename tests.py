def run_tests():
    """
    A simple function to run unit tests for core functionalities.
    """
    print("\n--- Running Tests ---")
    try:
        from expense_manager import add_expense
        add_expense("Groceries", "Milk", 25.00)
        print("Test 1 (Add Expense): Passed")

        from savings_manager import set_savings_goal, update_savings
        set_savings_goal(1000.00)
        update_savings(500.00)
        print("Test 2 (Savings Goal): Passed")

        from income_manager import add_income
        add_income("Salary", "August Salary", 3000.00)
        print("Test 3 (Add Income): Passed")

        from analysis import set_budget, generate_budget_comparison
        set_budget(10000.00)
        generate_budget_comparison()
        print("Test 4 (Budget Comparison): Passed")

    except Exception as e:
        print(f"Test failed: {e}")
