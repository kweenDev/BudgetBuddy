# utils.py
"""This module contains utility functions, including data persistence (loading/saving CSV data) and unit testing."""

import os
import csv


def csv_file_exists(filename):
    """
    Check if a CSV file exists.
    Args:
        filename (str): The filename to check.
    Returns:
        bool: True if file exists, False otherwise.
    """
    return os.path.exists(filename)


def load_savings_goal():
    """
    Load the current savings goal from the CSV file.
    Returns:
        tuple: (goal, saved, month) or None if no goal exists.
    """
    if csv_file_exists('data/savings.csv'):
        with open('data/savings.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            return next(reader, None)
    return None
