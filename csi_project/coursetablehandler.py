import mysql.connector as mysql
from dotenv import load_dotenv

import uuid

load_dotenv()

import os

conn = mysql.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USERNAME"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DATABASE")
)


cursor = conn.cursosr()

def add_course(coursename, teacher, description):
    try:
        luuid = str(uuid.UUID().bytes)
        cursor.execute("INSERT INTO courses (courseNAME, toughtBY, descrip, courseID) VALUES (%s, %s, %s, %s)", [coursename, teacher, description, luuid])
        cursor._connection.commit()
    except mysql.Error as error:
        print(f"CRITICAL ERROR OCCURED AT : {error}")

def find_courses(course_id=None, name=None, teacher=None, description=None):
    query = "SELECT * FROM courses WHERE 1=1"
    params = []
    
    if course_id:
        query += " AND courseID = %s"
        params.append(course_id)
    if name:
        query += " AND courseNAME = %s"
        params.append(name)
    if teacher:
        query += " AND toughtBY = %s"
        params.append(teacher)
    if description:
        query += " AND descrip = %s"
        params.append(description)
    
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except mysql.connector.Error as error:
        print(f"Error occurred: {error}")
