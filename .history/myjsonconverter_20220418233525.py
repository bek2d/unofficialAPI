import sqlite3
from sqlite3 import Error
import requests
import json
# establish connection to sqlite database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

#connect to database
conn = create_connection("myScrapedDatabase.db")


# function that gets an entry from sqlite table
def get_entry(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM jsonIDs WHERE id=?", (id,))
    row = cur.fetchone()
    return row

#get entry from database
row = get_entry(conn, "50329861")
o = str(*row)

response = requests.get("https://api.hh.ru/vacancies/50329861")
json_dict = response.json()
s = str(json_dict)
#connect to database
#insert json_dict into sqlite database
c = conn.cursor()
#create new table named content
c.execute("""CREATE TABLE IF NOT EXISTS content(id text, content text)""")
c.execute("INSERT INTO content VALUES (?,?)", (o, s,))
print(o)
print(s)
 
