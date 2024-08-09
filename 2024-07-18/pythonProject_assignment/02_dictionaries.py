"""
Exercise 2: Dictionaries
Task:
1.	Create a dictionary to store the names and ages of five people.
2.	Write a function that takes this dictionary and returns the name of the oldest person.
3.	Write a function that adds a new person to the dictionary.
"""
people = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 20,
    'David': 28,
    'Eve': 22
}

print("Initial dictionary:", people)


def find_oldest_person(people_dict):
    oldest_person = None
    max_age = -1

    for name, age in people_dict.items():
        if age > max_age:
            max_age = age
            oldest_person = name

    return oldest_person


oldest_name = find_oldest_person(people)
print("Oldest person:", oldest_name)


def add_person(people_dict, name, age):
    people_dict[name] = age


# Adding a new person
add_person(people, 'Fiona', 26)
print("Updated dictionary:", people)
