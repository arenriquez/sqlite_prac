import sqlite3

def show_all():
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    customers = c.execute("SELECT rowid, * FROM customers").fetchall() 

    for customer in customers:
        print(customer)

    conn.commit()
    conn.close()

def add_one(first, last, email):
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    conn.commit()
    conn.close()



def delete_one_by_id(id):
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()


def email_lookup(email):
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    customer = c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,)).fetchall() 

    if not customer:
        print("Email does not exist.")
    else:
        print(customer)

    conn.commit()
    conn.close()


def update_email(id, new_email):
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    c.execute("UPDATE customers SET email = (?) WHERE rowid = (?)", (new_email, id))

    conn.commit()
    conn.close()


