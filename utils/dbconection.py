import pymysql
import os
from dotenv import load_dotenv

load_dotenv(override=True)
con = None

def get_connection():
    global con
    if con is None or not con.open:
        con = pymysql.connect(
            charset=os.getenv("CHARSET",""),
            cursorclass=pymysql.cursors.DictCursor,
            host=os.getenv("HOST",""),
            connect_timeout=int(os.getenv("CONNECT_TIMEOUT", "10")),
            database=os.getenv("DATABASE", ""),
            password=os.getenv("PASSWORD", ""),
            read_timeout=int(os.getenv("READ_TIMEOUT", "10")),
            port=int(os.getenv("PORT", "3306")),
            user=os.getenv("USER", ""),
            write_timeout=int(os.getenv("WRITE_TIMEOUT", "10")),
        )
    return con