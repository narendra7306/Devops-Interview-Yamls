import psutil

process_name = "jenkins"

process_found = False

for process in psutil.process_iter(['pid', 'name']):
    if process.info['name'] and process_name.lower() in process.info['name'].lower():
        print(f"{process_name} is running. PID: {process.info['pid']}")
        process_found = True

if not process_found:
    print(f"{process_name} is not running")

