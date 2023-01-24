import sqlite3

if __name__ == '__main__':

    with sqlite3.connect('training_db.sqlite') as conn:
        cur = conn.cursor()

        with open('customers.sql') as file:
            sql_script = file.read()

        cur.executescript(sql_script)
        conn.commit()
        print('Data from customers.sql loaded into customers table successfully!')
