# Budget Buddy CLI

<p align="center"><img src="assets/logo.png" alt="Budget Buddy CLI logo"></p>

**Budget Buddy CLI** is a simple, command-line-based finance management tool to help you track expenses, income, savings goals, and monthly budgets. It stores data in CSV files and allows you to analyze your finances with a user-friendly interface. With additional support for exporting reports, you can easily view your financial status for each month.

## Features

- **Track Expenses**: Record expenses with categories, descriptions, amounts, payment methods, and locations.
- **Track Income**: Log various sources of income and view a detailed history of earnings.
- **Set Monthly Budgets**: Define a budget for each month and compare it with your total expenses.
- **Set and Track Savings Goals**: Set monthly savings goals and track your progress.
- **Generate Financial Reports**: Export detailed CSV reports of your income, expenses, and budgets using **Pandas**.
- **Unit Testing**: Built-in unit tests to verify core functionalities.

## Prerequisites

To run this program, you need:

- **Python 3.x** installed on your machine
- The **Pandas** library (for exporting and analyzing financial reports)

  To install Pandas, run:

  ```bash
  pip install pandas
  ```

  ## Project Structure

  The project is organized into the following files:

  - main.py: The entry point of the application, provides a menu for interacting with the system.
  - expense_manager.py: Handles adding expenses and storing them in a CSV file.
  - income_manager.py: Manages income by adding sources of income and tracking them.
  - savings_manager.py: Manages savings goals, updates savings, and tracks progress.
  - analysis.py: Provides financial analysis, budget comparison, and exporting of monthly reports.
  - utils.py: Contains utility functions such as CSV file checking and loading savings goals.
  - index.html: Contains the landing page details.
  - data/: Directory where CSV files (expenses, income, savings, and budget) are stored.
  - assets/: Directory where the logo and stylesheet for the landing page are stored.
  - tests.py: Contains unit tests for core functions.

## Getting Started

Follow the steps below to run the Budget Buddy CLI.

1. Clone the repository:

```bash
git clone https://github.com/kweenDev/budget-buddy-cli.git
```

2. Navigate to the project directory:

```bash
cd budget-buddy-cli.git
```

3. Install required dependencies (like Pandas):

```bash
pip install pandas
```

4. Run the application:

```bash
python main.py
```

## Usage

After launching the CLI, you'll be prompted with a menu to choose from the following options:

1. Add Expense: Record an expense by entering its category, description, and amount.
2. Add Income: Log an income source by specifying the source, description, and amount.
3. Set Savings Goal: Set a savings goal for the current month.
4. Update Savings: Add an amount to your savings and track progress toward the goal.
5. Set Budget: Define a budget for the current month.
6. Compare Budget vs Expenses: Compare your recorded expenses against the set budget and see whether you're over or under budget.
7. Track Savings Progress: View how much you've saved and how much more is required to reach your savings goal.
8. Run Tests: Run built-in unit tests to ensure that the core features are functioning as expected.
9. Exit: Quit the application.

   ### Example Workflow

   1. Add a salary income:

   ```bash
   Enter your choice: 2
   Enter income source (e.g., Salary): Salary
   Enter description: August Salary
   Enter the amount: 3500
   ```

   2. Add an expense for groceries:

   ```bash
   Enter your choice: 1
   Enter category: Groceries
   Enter the description: Bought vegetables
   Enter the amount: 120
   ```

   3. Set a monthly budget:

   ```bash
   Enter your choice: 5
   Enter your budget: 4000
   ```

   4. Compare budget vs expenses:

   ```bash
   Enter your choice: 6
   ```

## Data Export and Reporting

The application generates a detailed monthly report as a CSV file in the data/ directory. The report includes total income, total expenses, the set budget, and the remaining balance for the month.

    Example report file:
    ```bash
    data/monthly_report_2024-09.csv
    ```

## Running Tests

To verify the core functionality of the system, select _Run Tests_ from the main menu or manually execute the tests by running the `tests.py` file:

```bash
python tests.py
```

## Future Improvements

Here are some potential features to consider for future updates: - Support for multiple currencies - Integration with third-party APIs for fetching real-time exchange rates - Graphs and charts to visualise expenses, income, and savings trends - User authentication to store and track multiple users' financial data

## Contributing

Feel free to contribute by forking this repository and submitting pull requests. If you find any issues, open an issue on the GitHub repository.

## Author :black_nib:

- **Refiloe Radebe**<[kweenDev](https://github.com/kweenDev)>

## Acknowledgements :pray:

All work contained in this project was completed as part of my portfolio project for ALX Africa.
