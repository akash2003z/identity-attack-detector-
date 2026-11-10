<<<<<<< HEAD
<CodeBlock language="markdown" editable>
# Identity Attack Detector – Stolen Login, Caught 🛡️

Project Overview
Identity Attack Detector is a beginner-friendly cybersecurity project that analyzes simulated login activity to identify potentially suspicious account access.

It uses Python-based security rules and a Streamlit dashboard to display login statistics, risk levels and security alerts.
Features
- Suspicious Login Detection: Identifies unfamiliar login locations and unknown devices.
- Risk Scoring: Assigns risk scores to login attempts.
- Brute-Force Detection: Flags accounts with repeated failed login attempts.
- Impossible Travel Detection: Identifies logins from different locations within a short time.
- Security Alert Log: Displays detected security events and their severity.
- Interactive Login Filter: Filters login records by success or failure.
- Data Visualization: Displays login activity and risk distribution charts.
- CSV Export: Allows users to download login records for further analysis.
Technologies Used
- Python
- Streamlit
- Pandas
- Visual Studio Code
- Git and GitHub
Project Structure
Identity-Attack-Detector/
│
├── app.py
├── dashboard.py
└── README.md


How to Run the Project
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL


2. Open the project folder
cd Identity-Attack-Detector


3. Install dependencies
py -m pip install streamlit pandas


4. Run the dashboard
py -m streamlit run dashboard.py


Detection Rules
The demonstration uses rule-based risk scoring:
Indicator	Risk Points
Unfamiliar location	30
Unknown device	30
Failed login	10

Risk levels:
- LOW: 0–19
- MEDIUM: 20–49
- HIGH: 50 or above
These thresholds are demonstration values, not industry standards.
Important Limitations
- The project currently uses simulated login records.
- It is not connected to a real authentication system.
- Its alerts indicate suspicious patterns, not confirmed attacks.
- Impossible-travel detection uses simplified location and time comparisons.
- The detection rules are intended for learning and demonstration.
Learning Outcomes
Through this project, I practised:
- Python programming fundamentals
- Working with login activity records
- Rule-based security detection
- Basic risk scoring
- Identifying suspicious authentication patterns
- Building interactive dashboards using Streamlit
- Exporting security data into CSV format
Disclaimer
This project is developed for educational and defensive cybersecurity learning purposes. It uses fictional data and does not access real user accounts or credentials.

Project: Identity Attack Detector – Stolen Login, Caught

Author: Akash
</CodeBlock>
=======
# identity-attack-detector-
A Python-based cybersecurity project for detecting suspicious login activity using risk scoring and a Streamlit dashboard.
>>>>>>> 19dc898ec2f31a0ee2032ed9a6d8a04f8f322e33
