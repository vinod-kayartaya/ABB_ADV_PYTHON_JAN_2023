import sqlite3

if __name__ == '__main__':

    with sqlite3.connect('training_db.sqlite') as conn:
        # no need to call conn.close()
        cur = conn.cursor()
        sql_cmd = 'insert into customers (firstname, lastname, email, phone) values (?, ?, ?, ?)'

        choice = 'y'
        while choice in ('', 'y'):
            firstname = input('Enter firstname: ')
            lastname = input('Enter lastname: ')
            email = input('Enter email: ')
            phone = input('Enter phone: ')
            cur.execute(sql_cmd, (firstname, lastname, email, phone))
            print('Data inserted successfully!')

            choice = input('Do you want to add another? (y) ')

        conn.commit()
