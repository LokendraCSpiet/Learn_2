"""
Exercise 7: Dictionary Operations
Task:
1.	Write a Python program that takes a dictionary of student names and their scores.
Calculate and print the average score.
2.	Write a function that takes this dictionary and returns a new dictionary with the students
who scored above the average.
"""


# Task 1: Calculate and print the average score
def calculate_average_score(scores_dict):
    if not scores_dict:
        print("No scores available.")
        return

    total_score = sum(scores_dict.values())
    number_of_students = len(scores_dict)
    average_score = total_score / number_of_students

    return average_score


# Task 2: Get students who scored above the average
def students_above_average(scores_dict, average_score):
    if not scores_dict:
        return {}
    # Create a dictionary with students who scored above the average
    above_average_students = {name: score for name, score in scores_dict.items() if score > average_score}
    return above_average_students


student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

average_score = calculate_average_score(student_scores)
print(f"Average score: {average_score:.2f}")

above_average = students_above_average(student_scores, average_score)
print("Students who scored above average:", above_average)
