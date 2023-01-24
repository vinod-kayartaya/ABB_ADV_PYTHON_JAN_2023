import sqlite3
import csv


if __name__ == '__main__':

    with sqlite3.connect('training_db.sqlite') as conn:
        cur = conn.cursor()
        sql_cmd = 'delete from customers'  # delete all customers unconditionally
        cur.execute(sql_cmd)
        conn.commit()
        print('Table customers is now empty!!')
        sql_cmd = 'insert into customers (firstname, lastname, email, phone, city) values (?, ?, ?, ?, ?)'

        print('Importing data from customers.csv file...')

        with open('customers.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # skip the header
            count = 0
            for row in reader:
                count += 1
                firstname, lastname, email, phone, city = row
                cur.execute(sql_cmd, (firstname, lastname, email, phone, city))

            conn.commit()
            print(f'Successfully imported {count} customers data.')
