log_file = "pipeline.log"

try:
    with open(log_file, "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Jenkins log file does not exist")

except PermissionError:
    print("Permission denied to access the log file")

    
    