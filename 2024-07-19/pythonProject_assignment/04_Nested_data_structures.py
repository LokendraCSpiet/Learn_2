"""
Exercise 4: Nested Data Structures
Task:
1.	Create a list of dictionaries, where each dictionary contains details of a
person (name, age, city).
2.	Write a function that takes this list and returns a list of names of people who are older
than 30.
"""

# Task 1: Create a list of dictionaries with details of people
people = [
    {"name": "Alice", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 34, "city": "Los Angeles"},
    {"name": "Charlie", "age": 40, "city": "Chicago"},
    {"name": "David", "age": 22, "city": "Miami"},
    {"name": "Eva", "age": 31, "city": "San Francisco"}
]


# Task 2: Function to get names of people older than 30
def get_names_older_than_30(people_list):
    return [person['name'] for person in people_list if person['age'] > 30]


names_older_than_30 = get_names_older_than_30(people)
print("People older than 30:", names_older_than_30)
