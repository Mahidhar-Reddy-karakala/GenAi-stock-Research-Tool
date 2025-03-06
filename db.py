import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

# Supabase Session Pooler (Alternative for IPv4 Networks)
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")  # Replace with actual password
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Successfully connected to Supabase!")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM infosys;")
    rows = cursor.fetchall()  # Fetch all data

    # Print the results
    for row in rows:
        print(row)
    conn.close()
except Exception as e:
    print("❌ Failed to connect:", e)