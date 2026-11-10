
import streamlit as st
import pandas as pd
from datetime import datetime

# Dashboard settings
st.set_page_config(
    page_title="Identity Attack Detector",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Identity Attack Detector")
st.caption("Security Monitoring Dashboard")
st.divider()

# Simulated login records
login_records = [
    {"Employee": "Akash", "Time": "09:00", "Location": "Kerala, India", "Device": "Personal Laptop", "Status": "Success"},
    {"Employee": "Akash", "Time": "09:15", "Location": "USA", "Device": "Unknown Device", "Status": "Success"},
    {"Employee": "Akash", "Time": "09:20", "Location": "USA", "Device": "Unknown Device", "Status": "Failed"},
    {"Employee": "Akash", "Time": "09:21", "Location": "USA", "Device": "Unknown Device", "Status": "Failed"},
    {"Employee": "Akash", "Time": "09:22", "Location": "USA", "Device": "Unknown Device", "Status": "Failed"},
    {"Employee": "Akash", "Time": "09:23", "Location": "USA", "Device": "Unknown Device", "Status": "Failed"},
    {"Employee": "Akash", "Time": "09:24", "Location": "USA", "Device": "Unknown Device", "Status": "Failed"}
]

df = pd.DataFrame(login_records)

# Calculate login statistics
total_logins = len(df)
successful_logins = len(df[df["Status"] == "Success"])
failed_logins = len(df[df["Status"] == "Failed"])

# Calculate suspicious activity
suspicious_locations = len(df[df["Location"] != "Kerala, India"])
unknown_devices = len(df[df["Device"] == "Unknown Device"])

high_risk_logins = 0

for _, login in df.iterrows():
    risk_score = 0

    if login["Location"] != "Kerala, India":
        risk_score += 30

    if login["Device"] == "Unknown Device":
        risk_score += 30

    if login["Status"] == "Failed":
        risk_score += 10

    if risk_score >= 50:
        high_risk_logins += 1

# Dashboard metrics
st.subheader("Login Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Logins", total_logins)
col2.metric("Successful Logins", successful_logins)
col3.metric("Failed Logins", failed_logins)
col4.metric("High Risk Logins", high_risk_logins)

st.divider()

# Security alerts
st.subheader("Security Alerts")

col5, col6, col7 = st.columns(3)

col5.metric("Suspicious Locations", suspicious_locations)
col6.metric("Unknown Devices", unknown_devices)
col7.metric("Failed Attempts", failed_logins)

if failed_logins >= 5:
    st.error("🚨 Possible brute force attack detected!")

if suspicious_locations > 0:
    st.warning("⚠️ Unfamiliar login location detected!")

if unknown_devices > 0:
    st.warning("⚠️ Unknown device detected!")

st.warning(
    "⚠️ Possible impossible travel: Kerala to USA within 15 minutes."
)

st.divider()

# Login activity table
st.subheader("Login Activity")


# Interactive login filter
st.subheader("Filter Login Activity")

selected_status = st.selectbox(
    "Select Login Status",
    ["All", "Success", "Failed"]
)

if selected_status == "All":
    filtered_df = df
else:
    filtered_df = df[df["Status"] == selected_status]

st.dataframe(filtered_df, use_container_width=True)

st.write("Records displayed:", len(filtered_df))


# Export login records
st.divider()
st.subheader("📥 Export Security Logs")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Login Records (CSV)",
    data=csv_data,
    file_name="identity_security_logs.csv",
    mime="text/csv"
)




# Login activity chart
st.divider()
st.subheader("Login Activity Overview")

login_counts = df["Status"].value_counts()

st.bar_chart(login_counts)

# Risk distribution chart
st.subheader("Risk Level Distribution")

risk_counts = {
    "LOW": 0,
    "MEDIUM": 0,
    "HIGH": 0
}

for _, login in df.iterrows():

    score = 0

    if login["Location"] != "Kerala, India":
        score += 30

    if login["Device"] == "Unknown Device":
        score += 30

    if login["Status"] == "Failed":
        score += 10

    if score >= 50:
        risk_counts["HIGH"] += 1
    elif score >= 20:
        risk_counts["MEDIUM"] += 1
    else:
        risk_counts["LOW"] += 1

st.bar_chart(risk_counts)


# Security Alert Log
st.divider()
st.subheader("🚨 Security Alert Log")

alerts = []

if failed_logins >= 5:
    alerts.append({
        "Alert": "Possible brute-force attack",
        "Severity": "HIGH",
        "Details": f"{failed_logins} failed login attempts detected"
    })

if suspicious_locations > 0:
    alerts.append({
        "Alert": "Unfamiliar location",
        "Severity": "MEDIUM",
        "Details": "Login from an untrusted location"
    })

if unknown_devices > 0:
    alerts.append({
        "Alert": "Unknown device",
        "Severity": "MEDIUM",
        "Details": "Login from an unrecognized device"
    })


# Dynamic impossible travel detection

previous_successful_login = {}
impossible_travel_details = []

for _, login in df.iterrows():

    employee = login["Employee"]

    if login["Status"] == "Success":

        current_time = datetime.strptime(
            login["Time"], "%H:%M"
        )

        if employee in previous_successful_login:

            previous = previous_successful_login[employee]

            old_location = previous["Location"]
            old_time = previous["Time"]

            minutes = (
                current_time - old_time
            ).total_seconds() / 60

            if old_location != login["Location"] and 0 <= minutes <= 60:

                impossible_travel_details.append(
                    f"{old_location} to {login['Location']} "
                    f"within {minutes:.0f} minutes"
                )

        previous_successful_login[employee] = {
            "Location": login["Location"],
            "Time": current_time
        }

for detail in impossible_travel_details:
    alerts.append({
        "Alert": "Possible impossible travel",
        "Severity": "HIGH",
        "Details": detail
    })


if alerts:
    alert_df = pd.DataFrame(alerts)
    st.dataframe(alert_df, use_container_width=True)
else:
    st.success("No suspicious activity detected.")





