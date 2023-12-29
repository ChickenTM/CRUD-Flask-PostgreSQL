import psycopg2

conn = psycopg2.connect(
        host = "localhost",
        database = "EmployeeDB",
        user = "postgres",
        password = "password123")

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS employees;')
cur.execute('CREATE TABLE employees (id serial PRIMARY KEY,'
                                     'name varchar (30) NOT NULL,'
                                     'email varchar (50) NOT NULL,'
                                     'phone varchar (10) NOT NULL);'
                                      )
cur.execute('INSERT INTO employees (name, email, phone)'
            'VALUES (%s, %s, %s)',
            ('Sample Name', 'sample@abc.com', '1234567890')
            )

conn.commit()

cur.close()
conn.close()

