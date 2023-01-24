import sqlite3


if __name__ == '__main__':
    # connect to a database
    conn = sqlite3.connect("training_db.sqlite")

    sql_cmd = '''create table customers(
    id integer primary key autoincrement,
    firstname varchar(50) not null,
    lastname varchar(50),
    city varchar(100) default 'Bangalore',
    email varchar(255) unique,
    phone varchar(50) unique
    )'''

    # create/obtain a cursor
    cur = conn.cursor()

    # execute the command using the cursor
    cur.execute(sql_cmd)
    print('Table customers created successfully!')

    # close the db resources
    conn.close()
