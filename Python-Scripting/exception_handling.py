# suppose your python automation script tries to read a jenkins log file, but
# the file does not exist. how do you handle this situation, which exception will you use
# write a python script to handle this error gracefully


log_file = "pipeline.log"

try:
    with open(log_file, "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Jenkins log file does not exist")

except PermissionError:
    print("Permission denied to access the log file")

    