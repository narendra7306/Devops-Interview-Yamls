import shutil

# Get disk usage statistics for the root filesystem
total, used, free = shutil.disk_usage("/")

# Convert bytes to GB
gb = 1024 ** 3

print(f"Total Disk Space : {total / gb:.2f} GB")
print(f"Used Disk Space  : {used / gb:.2f} GB")
print(f"Free Disk Space  : {free / gb:.2f} GB")

usage_percent = (used / total) * 100
print(f"Disk Usage       : {usage_percent:.2f}%")

# Alert if usage exceeds 80%
if usage_percent > 80:
    print("WARNING: Disk usage is above 80%!")
else:
    print("Disk usage is normal.")

