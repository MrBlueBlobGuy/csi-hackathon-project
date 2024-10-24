import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

import os


conn = mysql.connect(
    host = "localhost",
    user = "root",
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
    
def getsalt(username, cursor):
    try: 
        cursor.execute("SELECT salt FROM userdata WHERE username='%s", [username, ])
        return cursor.fetchone()
    except mysql.Error as err:
        print(f"CRITICAL ERROR OCCURED AT: {err}")