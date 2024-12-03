# import psycopg2

# conn = psycopg2.connect("dbname='example_db' user='postgres' host='localhost' password='7777' port='5432'")
# cur = conn.cursor()

# insert_sql = ("INSERT INTO employee (first_name)")

# cur.execute("SELECT * FROM employee")

# records = cur.fetchall()
# print(records)



# import psycopg2

# conn = psycopg2.connect("dbname='example_db' user='postgres' host='localhost' password='7777' port='5432'")
# cur = conn.cursor()
# insert_sql = ("INSERT INTO employee (first_name, last_name, email, gender, date_of_birth, country_of_birth, position)"
#               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
# cur.execute(insert_sql, (
#     "Example", "last_name_example", "example@mail.ru", "Male", "2016-11-10", "Uzbekistan", "Student"))
# conn.commit()
# cur.close()
# conn.close()


# import pandas as pd

# df = pd.read_csv("MOCK_DATA.csv")
# print(df)

import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname='example_db' user='postgres' host='localhost' password='7777'")
cur = conn.cursor()

try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS   (
            id INT, 
            first_name VARCHAR(50), 
            last_name VARCHAR(50), e
            email VARCHAR(50), 
            gender VARCHAR(50), 
            ip_address VARCHAR(50)
        );
    """)
    conn.commit()
    print("Table created successfully")
except Exception as e:
    print("Error creating table:", e)


df = pd.read_csv('MOCK_DATA.csv')

for _, row in df.iterrows():
    try:
        cur.execute("""
            INSERT INTO mock_data (id, first_name, last_name, email, gender, ip_address) 
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (row['id'], row['first_name'], row['last_name'], row['email'], row['gender'], row['ip_address']))
        conn.commit()
        print(f"Row inserted: {row['id']}, {row['first_name']}")
    except Exception as e:
        print("Error inserting row:", e)

conn.close()

print('Xamidov Qattiqbekmas')