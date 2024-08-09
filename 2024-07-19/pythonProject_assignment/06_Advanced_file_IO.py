"""
Exercise 6: Advanced File I/O
Task:
1.	Write a Python program that reads a CSV file and prints the contents in a formatted table.
2.	Write a Python program that writes a list of dictionaries to a CSV file, with each dictionary
representing a row.
"""

import csv
from tabulate import tabulate


# Task 1: Read a CSV file and print the contents in a formatted table
def print_csv_as_table(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            # Read the header
            headers = next(reader)
            # Read the rows
            rows = [row for row in reader]

        # Print the table
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
csv_filename = 'testFile.csv'  # Replace with your CSV file path
print_csv_as_table(csv_filename)

import csv


# Task 2: Write a list of dictionaries to a CSV file
def write_dicts_to_csv(filename, data):
    if not data:
        print("No data to write.")
        return

    # Extract the headers from the first dictionary
    headers = data[0].keys()

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            # Write the header
            writer.writeheader()
            # Write the data
            writer.writerows(data)

        print(f"Data successfully written to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
data_to_write = [
    {"name": "Alice", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 34, "city": "Los Angeles"},
    {"name": "Charlie", "age": 40, "city": "Chicago"}
]

csv_filename = 'output.csv'  # Replace with your desired CSV file path
write_dicts_to_csv(csv_filename, data_to_write)
