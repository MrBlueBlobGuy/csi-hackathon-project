import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

import os

conn = mysql.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USERNAME"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DATABASE")
)
cursor = conn.cursor()

def verifylogininfo(username, hashedsaltedpassword, cursor):
    try:
        cursor.execute("SELECT hashedsaltedpassword from userdata WHERE username=%s", [username, ])
        a = cursor.fetchone()
        print(a)
        return True if hashedsaltedpassword == a[0] else False
    except mysql.Error as err:
        print(f'CRITICAL ERROR OCCURED AT: {err}')
        return False
    
def getsaltfromdb(username, cursor):
    try: 
        cursor.execute("SELECT salt FROM userdata WHERE username='%s", [username, ])
        return cursor.fetchone()[0]
    except mysql.Error as err:
        print(f"CRITICAL ERROR OCCURED AT: {err}")

def add_entry(username, hashedsaltedpassword, id, usertype, salt, cursor):
    try:
        cursor.execute("INSERT INTO userdata (username, hashedsaltedpassword, id, usertype, salt) VALUES (%s, %s, %d, %s, %s)", [username, hashedsaltedpassword, id, usertype, salt])
        cursor._connection.commit()

    except Exception as err:
        print(f"CRITICAL ERROR OCCURED AT: {err}")