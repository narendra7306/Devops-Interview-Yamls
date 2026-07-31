import psutil

# Get memory details
memory = psutil.virtual_memory()

# Convert bytes to GB
gb = 1024 ** 3

print(f"Total Memory     : {memory.total / gb:.2f} GB")
print(f"Available Memory : {memory.available / gb:.2f} GB")
print(f"Used Memory      : {memory.used / gb:.2f} GB")
print(f"Memory Usage     : {memory.percent}%")


if memory.percent > 80:
    print("WARNING: Memory usage is above 80%")
    sys.exit(1)
else:
    print("Memory usage is normal.")

