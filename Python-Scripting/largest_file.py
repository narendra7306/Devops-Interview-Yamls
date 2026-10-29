
# Write a script to find the largest file in a directory

import os

directory = "/home/seelam/dev"

print(directory)

largest_file = ""
largest_size = 0

files = os.listdir(directory)

for file in files:
    file_path = os.path.join(directory, file)
    print(file_path)

    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(file_size)

        if file_size > largest_size:
            largest_size = file_size
            largest_file = file
print("Largest file:", largest_file)
print("File size:", largest_size, "bytes")

