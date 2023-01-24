import sqlite3


if __name__ == '__main__':

    with sqlite3.connect('training_db.sqlite') as conn:
        cur = conn.cursor()

        customer_id = int(input('Enter id for search: '))
        sql_cmd = 'select * from customers where id = ?'
        cur.execute(sql_cmd, (customer_id, ))

        customer = cur.fetchone()
        if customer is None:
            print(f'No customer found for id {customer_id}')
            exit(1)

        column_names = [column[0] for column in cur.description]
        for i, column_name in enumerate(column_names):
            print(f'{column_name.capitalize():20s}: {customer[i]}')

        # _, firstname, lastname, city, email, phone = customer
        #
        # print('Here is the customer data: ')
        # print(f'Name         : {firstname} {lastname}')
        # print(f'City         : {city}')
        # print(f'Email id     : {email}')
        # print(f'Phone #      : {phone}')


