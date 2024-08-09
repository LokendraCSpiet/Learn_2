"""
Task 2: Naive Pattern Search
Implement the naive pattern searching algorithm to find all occurrences of a pattern within a given text string.
Count the number of comparisons made during the search to evaluate the efficiency of the algorithm.
"""


def naive_pattern_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    occurrences = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences, comparisons


# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
occurrences, comparisons = naive_pattern_search(text, pattern)

print("Occurrences of pattern:", occurrences)
print("Number of comparisons made:", comparisons)