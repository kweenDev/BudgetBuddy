# analysis.py
"""Module provides financial analysis."""

import csv
from datetime import datetime
import pandas as pd
from utils import csv_file_exists


def set_budget(monthly_budget):
    """
    Set a monthly budget.
    Args:
        monthly_budget (float): Budget for the current month.
    Returns:
        None
    """
    month = datetime.now().strftime("%Y-%m")
    with open('data/budget.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([month, monthly_budget])
    print(f"Budget of R{monthly_budget} set for {month}.")


def generate_budget_comparison():
    """
    Compare expenses against the set budget for the current month.
    Returns:
        None
    """
    current_month = datetime.now().strftime("%Y-%m")

    # Load expenses
    if csv_file_exists('data/expenses.csv'):
        expenses_df = pd.read_csv('data/expenses.csv', names=[
                                  'Date', 'Category', 'Description', 'Amount', 'Payment Method', 'Location'])
        expenses_df['Amount'] = pd.to_numeric(
            expenses_df['Amount'], errors='coerce')
        expenses_monthly = expenses_df[expenses_df['Date'].str.startswith(
            current_month)]
        total_spent = expenses_monthly['Amount'].sum()
    else:
        print("No expenses recorded for this month.")
        total_spent = 0

    # Load income
    if csv_file_exists('data/income.csv'):
        income_df = pd.read_csv(
            'data/income.csv', names=['Date', 'Source', 'Description', 'Amount'])
        income_df['Amount'] = pd.to_numeric(
            income_df['Amount'], errors='coerce')
        income_monthly = income_df[income_df['Date'].str.startswith(
            current_month)]
        total_income = income_monthly['Amount'].sum()
    else:
        print("No income recorded for this month.")
        total_income = 0

    # Load budget
    budget = None
    if csv_file_exists('data/budget.csv'):
        with open('data/budget.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == current_month:
                    budget = float(row[1])

    if budget is not None:
        print(f"Total Income: R{total_income}")
        print(f"Total Spent: R{total_spent}")
        print(f"Budget: R{budget}")
        if total_spent > budget:
            print(f"You are over budget by R{total_spent - budget}.")
        else:
            print(f"You are under budget by R{budget - total_spent}.")

        # Export detailed CSV report using Pandas
        report_df = pd.DataFrame({
            'Total Income': [total_income],
            'Total Spent': [total_spent],
            'Budget': [budget],
            'Remaining': [budget - total_spent if budget > total_spent else total_spent - budget]
        })

        report_df.to_csv(
            f'data/monthly_report_{current_month}.csv', index=False)
        print(
            f"Monthly report exported to data/monthly_report_{current_month}.csv.")
    else:
        print("No budget set for this month.")
