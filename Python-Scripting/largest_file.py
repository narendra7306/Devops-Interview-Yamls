
Write a script to find the largest file in a directory

import os

directory = "/home/user/logs"

largest_file = None
largest_size = 0

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)

    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)

        if size > largest_size:
            largest_size = size
            largest_file = file_path

print("Largest file:", largest_file)
print("File size:", largest_size, "bytes")
