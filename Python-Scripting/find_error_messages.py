How do you read a log file and find ERROR messages?

log_file = "application.log"

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
