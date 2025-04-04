# 🔐 EDS Audit Log CLI

A secure and lightweight command-line interface (CLI) tool built in Python for simulating and interacting with audit logs from a PostgreSQL database. Created for internal use by Eagle Defense Systems (EDS), this tool supports basic functionality for log insertion and querying, aiding GRC, compliance, and threat analysis simulations.

---

## 🚀 Features

- Insert mock audit log events for testing
- Fetch the 5 latest security logs
- Uses PostgreSQL + `psycopg2` with `.env` for credential security
- Clean CLI experience, ideal for local testing and training environments

---

## 📁 Project Structure

eds_audit_log_cli/ │ ├── db_connector.py # Main CLI script (Insert/Fetch logs) ├── .env # Environment variables (DB credentials) ├── .gitignore # Hides .env and venv from Git ├── venv/ # Virtual environment └── README.md # This file

🔐 Security Notes
Sensitive credentials are loaded from .env using python-dotenv

.env and venv/ are both ignored from Git tracking

Only safe to use on local test environments, not for production

📚 Requirements
Python 3.9+ (3.13 tested)

PostgreSQL (running locally or remote)

psycopg2-binary

python-dotenv

🧠 Inspiration
This CLI tool is part of EDS Labs, where Eagle Defense Systems prototypes internal security GRC utilities.

🏷 Tags
#PostgreSQL #CyberSecurity #PythonCLI #AuditLogs #EDSLabs #GRC #SecurityTools
