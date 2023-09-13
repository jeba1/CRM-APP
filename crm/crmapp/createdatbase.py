
import psycopg2


conn = psycopg2.connect(
    user='postgres', password='admin123', host='127.0.0.1', port= '5433'
)
cursor = conn.cursor()
conn.autocommit = True

sql = """CREATE DATABASE product;"""

cursor.execute(sql)
print("Database has been created successfully !!");