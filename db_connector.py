from dotenv import load_dotenv
import os
import psycopg2

# Load .env values
load_dotenv()

# ✅ DB Connector
def connect_db():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


def insert_log():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO audit_logs (event_type, event_severity, source_ip, user_id)
        VALUES ('LOGIN_FAILURE', 'HIGH', '192.168.1.100', 101);
    """)
    conn.commit()
    print("✔️ Log inserted.")
    cur.close()
    conn.close()

def fetch_logs():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT 5;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("🔍 EDS Audit Log CLI")
    print("1. Insert a new log")
    print("2. Fetch latest logs")
    choice = input("Select option (1 or 2): ")

    if choice == "1":
        insert_log()
    elif choice == "2":
        fetch_logs()
    else:
        print("Invalid option.")
