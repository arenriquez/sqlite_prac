import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'jelder@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Andrew', 'Enriquez', 'aenriquez@codemy.com')")
# homie_group = [
#     ('Jimmy', 'Diaz', 'jdiaz@codemy.com'),
#     ('Bailey', 'Huynh', 'bhuynh@codemy.com'),
#     ('Kevin', 'Earle', 'jdiaz@codemy.com'),
#     ('Jenny', 'Eng', 'jeng@codemy.com')
# ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", homie_group)


# target_name = 'Andres'
# row_id = 2
# c.execute(""" UPDATE customers SET first_name = ? 
#         WHERE rowid = ? 
#     """, (target_name, row_id,))

print("Command executed successfully")

conn.commit()
conn.close()