import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

c.execute("""CREATE TABLE customers (
        first_name varchar(20),
        last_name varchar(20),
        email varchar(50)
    )""")

conn.commit()
conn.close()