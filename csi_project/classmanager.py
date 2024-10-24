import mysql.connector as mysql

from dotenv import load_dotenv

import uuid

load_dotenv()

import os

conn = mysql.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DATABASE")
)

cursor = conn.cursor()


def add_class(starttime, endtime, courseid):
    try:
        query = """
        INSERT INTO classes (starttime, endtime, courseid) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (starttime, endtime, courseid))
        cursor._connection.commit()
        print("Class added successfully")

    except mysql.errors as e:
        print(f"Failed to insert into MySQL table {e}")
