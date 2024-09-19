# expense_manager.py

import csv
from datetime import datetime
from utils import csv_file_exists

EXPENSE_FILE = 'data/expenses.csv'


def add_expense(category, description, amount, payment_method=None, location=None):
    """
    Add an expense to the CSV file with multi-category support and flexible input.
    Args:
        category (str): The category of the expense.
        description (str): A brief description of the expense.
        amount (float): The amount spent.
        payment_method (str, optional): The method of payment used for the expense.
        location (str, optional): The location where the expense was made.
    Returns:
        None
    """
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            category,
            description,
            amount,
            payment_method or "N/A",
            location or "N/A"
        ])
    print(f"Added expense: {category}, {description}, R{amount}")
