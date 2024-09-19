# income_manager.py

import csv
from datetime import datetime
from utils import csv_file_exists

INCOME_FILE = 'data/income.csv'


def add_income(source, description, amount):
    """
    Add an income source to the CSV file.
    Args:
        source (str): The source of the income (e.g., salary, freelance).
        description (str): A description of the income.
        amount (float): The amount earned.
    Returns:
        None
    """
    with open(INCOME_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime(
            "%Y-%m-%d"), source, description, amount])
    print(f"Added income: {source}, {description}, R{amount}")


def view_income():
    """
    View income records from the CSV file.
    Returns:
        None
    """
    if not csv_file_exists(INCOME_FILE):
        print("No income records found.")
        return

    print(f"{'Date':<15}{'Source':<20}{'Description':<30}{'Amount':<10}")
    with open(INCOME_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            date, source, description, amount = row
            print(f"{date:<15}{source:<20}{description:<30}{amount:<10}")
