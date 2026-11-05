# suppose your jenkins pipeline generates a log file. you need to write a python
# script to read the jenkins log file, search for the word ERROR and print all the lines
# containing ERROR  

log_file = "application.log"

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
