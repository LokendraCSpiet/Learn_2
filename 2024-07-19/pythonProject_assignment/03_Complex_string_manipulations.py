"""
Exercise 3: Complex String Manipulations
Task:
1.	Write a Python program that takes a sentence from the user and reverses the order of the words.
2.	Write a Python function that takes a string and returns a dictionary with the count of
each vowel in the string.
"""


# Task 1: Reverse the order of words in a sentence
def reverse_words(sentence):
    reversed_words = sentence.split(" ")[::-1]
    rev_sentence = " ".join(reversed_words)
    return rev_sentence


user_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_sentence)
print("Reversed sentence:", reversed_sentence)


# Task 2: Count vowels in a string and return a dictionary
def count_vowels(input_string):
    # vowels = 'aeiouAEIOU'
    vowels = 'aeiou'
    # Initialize an empty dictionary to store counts
    vowel_cnt = {vowel: 0 for vowel in vowels}

    for char in input_string:
        if char in vowels:
            vowel_cnt[char.lower()] += 1

    return vowel_cnt


input_string = input("Enter a string: ")
vowel_counts = count_vowels(input_string)
print("Vowel counts:", vowel_counts)



