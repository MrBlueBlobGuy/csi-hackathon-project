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

cursor = conn.cursor()

