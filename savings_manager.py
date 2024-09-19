# savings_manager.py
"""Module manages savings goals and tracks progress against goals."""

import csv
from utils import csv_file_exists, load_savings_goal
from datetime import datetime

SAVINGS_FILE = 'data/savings.csv'


def set_savings_goal(goal):
    """
    Set a savings goal for the current month.
    Args:
        goal (float): The savings goal for the month.
    Returns:
        None
    """
    with open(SAVINGS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Goal", "Saved", "Month"])
        writer.writerow([goal, 0, datetime.now().strftime("%Y-%m")])
    print(f"Savings goal of R{goal} set for this month.")


def update_savings(amount):
    """
    Update the savings progress for the current month.
    Args:
        amount (float): The amount saved in the current update.
    Returns:
        None
    """
    goal_data = load_savings_goal()
    if goal_data:
        goal, saved, month = goal_data
        new_saved = float(saved) + amount
        remaining = float(goal) - new_saved
        print(
            f"Updated saved amount: R{new_saved}. You have R{remaining} remaining.")
        with open(SAVINGS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Goal", "Saved", "Month"])
            writer.writerow([goal, new_saved, month])
    else:
        print("No savings goal set.")
