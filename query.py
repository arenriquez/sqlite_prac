import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

customers = c.execute("SELECT rowid, * from customers").fetchall() #equivalent is just print(c.fetchall()), other options are fetchone() and fetchmany(# of first few records wanted)
print(customers)

# target_name = "Andrew"
# rows = c.execute(
#     "SELECT rowid, email FROM customers WHERE first_name = ?",
#     (target_name,),
# ).fetchall()
# print(rows)

# names = [i[0] for i in customers]
# print(names)

# print("NAME " + "\t\tEMAIL")
# print("-----" + "\t\t-------")
# for customer in customers:
#     print(customer[0] + " " + customer[1] + "\t" + customer[2])

target_letter = 'J%'
j = c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE ? or last_name LIKE ? ORDER BY last_name DESC", (target_letter, target_letter)).fetchall()
print(j)

print("Command executed successfully")

conn.commit()
conn.close()