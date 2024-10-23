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
cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
               'name VARCHAR(255),'
               'address VARCHAR(255),'
               'project_number INTEGER)')
