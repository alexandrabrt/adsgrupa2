import mysql.connector
from password import parola

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
cursor = my_db.cursor()
# cursor.execute("CREATE DATABASE adsgrupa2")
# cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(255),'
#                'address VARCHAR(255),'
#                'project_number INTEGER)')
# cursor.execute('SHOW TABLES')
# for x in cursor:
#     print(x)
# cursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY,"
#                "first_name VARCHAR(255),"
#                "last_name VARCHAR(255),"
#                "email VARCHAR(255))")
# cursor.execute('SHOW TABLES')
# for x in cursor:
#     print(x)
# cursor.execute('ALTER TABLE projects ADD COLUMN varsta INTEGER')
# cursor.execute('ALTER TABLE projects DROP COLUMN varsta')
# sql = 'INSERT INTO projects (name, address, project_number) VALUES (%s, %s, %s)'
# val = [
#     ('Petre', 'Bucuresti', 123),
#     ('Amalia', 'Ploiesti', 321),
#     ('Mihai', 'Bacau', 224)
# ]
# cursor.executemany(sql, val)
# my_db.commit()
sql = 'UPDATE projects SET address="Bucuresti" where id=2'
cursor.execute(sql)
my_db.commit()
