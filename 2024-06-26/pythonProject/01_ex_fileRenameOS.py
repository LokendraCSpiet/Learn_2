import os

filename = "sample.txt"
if os.path.exists(filename):
    os.rename(filename, 'sample_renamed.txt')
    print(f"{filename} has been renamed to sample_renamed.txt")
else:
    print(f"{filename} does not exist")