import psutil
import time

# setting CPU utilization threshold
THRESHOLD = 80

# Get CPU information
physical_cpu = psutil.cpu_count(logical=False)
logical_cpu = psutil.cpu_count()

print(f"Physical CPUs : {physical_cpu}")
print(f"Logical CPUs  : {logical_cpu}")


# Continuously monitor CPU usage
while True:
    # Get CPU usage over a 1-second interval
    cpu_usage = psutil.cpu_percent(interval=1)

    print(f"Current CPU Usage : {cpu_usage}%")

    # Check if CPU usage exceeds the threshold
    if cpu_usage >= THRESHOLD:
        print("ALERT: CPU utilization has reached or exceeded 80%!")
    else:
        print("CPU utilization is within the normal range.")


    # Wait 5 seconds before checking again
    time.sleep(5)




# Explanation:

# import psutil → Imports the library used to retrieve system information.
# import time → Used to pause the script between checks.
# THRESHOLD = 80 → Sets the CPU utilization limit for generating an alert.
# psutil.cpu_count(logical=False) → Returns the number of physical CPU cores.
# psutil.cpu_count() → Returns the number of logical CPUs (including Hyper-Threading).
# psutil.cpu_percent(interval=1) → Measures average CPU usage over 1 second.
# while True: → Keeps the script running continuously.
# if cpu_usage >= THRESHOLD: → Checks whether CPU usage has reached or exceeded 80%.
# time.sleep(5) → Waits 5 seconds before the next check.

