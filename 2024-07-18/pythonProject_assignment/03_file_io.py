"""
Exercise 3: File I/O
Task:
1.	Write a Python program that reads a text file and prints the number of words,
lines, and characters in the file.
2.	Write a Python program that takes a list of strings and writes them to a text file,
each string on a new line.
"""


def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            lines = text.splitlines()
            words = text.split()
            num_lines = len(lines)
            num_words = len(words)
            num_chars = len(text)

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Replace 'sample.txt' with the path to your text file
analyze_text_file('testFile.txt')


# Task 2 : create a file using list of strings
def write_strings_to_file(strings, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for string in strings:
                file.write(string + '\n')
        print(f"Strings have been written to '{filename}' successfully.")

    except IOError:
        print(f"Error: Could not write to file '{filename}'.")


# Example list of strings
strings_to_write = [
    "Hello,",
    "This is a test.",
    "Writing strings to a file.",
    "End of file."
]

# Replace 'output.txt' with the desired output file path
write_strings_to_file(strings_to_write, 'output.txt')
