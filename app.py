
from datetime import datetime

print("IDENTITY ATTACK DETECTOR")
print("========================")

# Trusted employee information
trusted_location = "Kerala, India"
trusted_device = "Personal Laptop"

# Sample login records
login_records = [
    {"employee": "Akash", "time": "09:00", "location": "Kerala, India", "device": "Personal Laptop", "status": "Success"},
    {"employee": "Akash", "time": "09:15", "location": "USA", "device": "Unknown Device", "status": "Success"},
    {"employee": "Akash", "time": "09:20", "location": "USA", "device": "Unknown Device", "status": "Failed"},
    {"employee": "Akash", "time": "09:21", "location": "USA", "device": "Unknown Device", "status": "Failed"},
    {"employee": "Akash", "time": "09:22", "location": "USA", "device": "Unknown Device", "status": "Failed"},
    {"employee": "Akash", "time": "09:23", "location": "USA", "device": "Unknown Device", "status": "Failed"},
    {"employee": "Akash", "time": "09:24", "location": "USA", "device": "Unknown Device", "status": "Failed"}
]

# Track failed login attempts
failed_attempts = {}

# Store previous successful login
previous_login = {}

print("\nLOGIN SECURITY ANALYSIS")
print("-----------------------")

for login in login_records:

    employee = login["employee"]
    location = login["location"]
    device = login["device"]
    status = login["status"]
    login_time = datetime.strptime(login["time"], "%H:%M")

    risk_score = 0
    warnings = []

    # Rule 1: Unfamiliar location
    if location != trusted_location:
        risk_score += 30
        warnings.append("Unfamiliar location")

    # Rule 2: Unknown device
    if device != trusted_device:
        risk_score += 30
        warnings.append("Unknown device")

    # Rule 3: Failed login
    if status == "Failed":
        risk_score += 10
        warnings.append("Failed login")

        if employee not in failed_attempts:
            failed_attempts[employee] = 0

        failed_attempts[employee] += 1

    # Rule 4: Impossible travel
    if status == "Success":

        if employee in previous_login:

            old_location = previous_login[employee]["location"]
            old_time = previous_login[employee]["time"]

            time_difference = (
                login_time - old_time
            ).total_seconds() / 60

            if old_location != location and 0 <= time_difference <= 60:
                warnings.append("Possible impossible travel")

        previous_login[employee] = {
            "location": location,
            "time": login_time
        }

    # Risk level
    if risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 20:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # Display results
    print("\nEmployee:", employee)
    print("Time:", login["time"])
    print("Location:", location)
    print("Device:", device)
    print("Login status:", status)
    print("Risk score:", risk_score)
    print("Risk level:", risk_level)

    if warnings:
        print("Warnings:", ", ".join(warnings))

    if risk_score >= 50:
        print("ALERT: Suspicious login activity!")

# Brute force analysis
print("\nFAILED LOGIN ANALYSIS")
print("---------------------")

for employee, count in failed_attempts.items():

    print("Employee:", employee)
    print("Failed attempts:", count)

    if count >= 5:
        print("ALERT: Possible brute force attack!")

print("\nSECURITY MONITORING COMPLETED")
print("=============================")
