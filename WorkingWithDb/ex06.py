import sqlite3


if __name__ == '__main__':

    with sqlite3.connect('training_db.sqlite') as conn:
        cur = conn.cursor()

        city = input('Enter city to search: ')
        cmd = 'select * from customers where city = ?'

        cur.execute(cmd, (city, ))
        rows = cur.fetchall()

        if len(rows) > 1:
            print(f'{"Name":30s} {"Email address":30s} {"Phone#":15s}')
            print('='*77)
            for row in rows:
                _, firstname, lastname, city, email, phone = row
                print(f'{(firstname+" "+lastname):30s} {email:30s} {phone:15s}')
            print('='*77)
        elif len(rows) == 1:
            print('Here is the customer data: ')
            _, firstname, lastname, city, email, phone = rows[0]
            print(f'Name         : {firstname} {lastname}')
            print(f'City         : {city}')
            print(f'Email id     : {email}')
            print(f'Phone #      : {phone}')
        else:
            print(f'No data found for a customer in city {city}')

