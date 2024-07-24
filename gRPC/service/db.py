import psycopg2
import os
import json
from dotenv import load_dotenv  # type: ignore

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


def get_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password = DB_PASS
    )
    cur = conn.cursor()
    cur.execute('select * from data;') 
    data = [{'id': id_, 'text': test} for id_, test in cur.fetchall()]
    conn.close()
    return data


get_data()