
import requests
import re
import json
from requests.auth import HTTPBasicAuth

# Jenkins configuration
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "php-app"
BUILD_NUMBER = "lastBuild"

USERNAME = "admin"
API_TOKEN = "your-jenkins-api-token"

# Fetch Jenkins console logs
def get_jenkins_logs():

    url = (
        f"{JENKINS_URL}/job/{JOB_NAME}/"
        f"{BUILD_NUMBER}/consoleText"
    )

    response = requests.get(
        url,
        auth=HTTPBasicAuth(USERNAME, API_TOKEN),
        timeout=30
    )

    response.raise_for_status()

    return response.text


# Identify common errors
def analyze_logs(logs):

    error_patterns = {
        "Docker Build Failure": [
            r"docker build.*failed",
            r"failed to solve",
            r"no space left on device",
            r"failed to compute cache key"
        ],

        "Dependency Issues": [
            r"unable to locate package",
            r"dependency resolution failed",
            r"package .* not found",
            r"could not install"
        ],

        "Test Failures": [
            r"tests failed",
            r"test failures",
            r"assertionerror",
            r"pytest.*failed"
        ],

        "Kubernetes Deployment Failure": [
            r"ImagePullBackOff",
            r"CrashLoopBackOff",
            r"deployment .* exceeded its progress deadline",
            r"error when applying"
        ],

        "Terraform Errors": [
            r"Error:",
            r"terraform apply.*failed",
            r"Error acquiring the state lock",
            r"Invalid value"
        ],

        "Jenkins Pipeline Errors": [
            r"script returned exit code [1-9]",
            r"Finished: FAILURE",
            r"ERROR:"
        ]
    }

    detected_errors = {}

    for category, patterns in error_patterns.items():

        for pattern in patterns:

            matches = re.findall(
                pattern,
                logs,
                re.IGNORECASE
            )

            if matches:
                detected_errors[category] = list(set(matches))
                break

    return detected_errors


# Generate report
def generate_report(errors):

    print("\n========== JENKINS BUILD ANALYSIS ==========")

    if not errors:
        print("No matching errors detected.")
    else:
        for category, matches in errors.items():

            print(f"\nCategory: {category}")

            for error in matches:
                print(f"Detected: {error}")

    print("\n============================================")


# Main execution
if __name__ == "__main__":

    try:
        print("Fetching Jenkins pipeline logs...")

        logs = get_jenkins_logs()

        print("Analyzing pipeline logs...")

        errors = analyze_logs(logs)

        generate_report(errors)

        # Save analysis report
        with open("jenkins_analysis.json", "w") as file:
            json.dump(errors, file, indent=4)

        print("\nReport saved: jenkins_analysis.json")

    except requests.RequestException as error:
        print(f"Jenkins API error: {error}")
