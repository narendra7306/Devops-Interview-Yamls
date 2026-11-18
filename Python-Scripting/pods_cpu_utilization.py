# you are managing multiple Kubernetes deployments, and your monitoring team 
# has provided a JSON file containing pod names and their respective CPU 
# utilization percentages. Can you write a Python script that reads this JSON
# file, identifies all pods whose CPU utilization is above 80%, and prints the
# pod name along with its CPU utilization? Also explain how you would extend the 
# script to generate an alert when any pod crosses the threshold.


import json

# Read JSON file
with open("pods.json", "r") as file:
    data = json.load(file)

# Check CPU utilization
for pod in data["pods"]:
    if pod["cpu_utilization"] > 80:
        print(
            f"Pod: {pod['pod_name']}, "
            f"CPU Utilization: {pod['cpu_utilization']}%"
        )

