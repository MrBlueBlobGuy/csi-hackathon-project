import mysql.connector as mysql
from dotenv import load_dotenv

import uuid

load_dotenv()

import os

try:
    conn = mysql.connect(
        host = "localhost",
        user = "root",
        password = os.getenv("PASSWORD"),
        database = os.getenv("DATABASE")
    )
except:
    print("TODO")

cursor = conn.cursor()

