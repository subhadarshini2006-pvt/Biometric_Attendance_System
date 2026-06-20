import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=admin123""  # Leave blank if you don't use a password, or type it here
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")
    print("🚀 Success! 'attendance_system' database is ready.")
    cursor.close()
    mydb.close()
except Exception as e:
    print(f"❌ Error connecting to MySQL: {e}")
