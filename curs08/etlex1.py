import pandas
import mysql.connector
from password import parola

# extragere
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
cursor = my_db.cursor()
# cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'category VARCHAR(50),'
#                'price DECIMAL(10, 2))')
#
# cursor.execute('CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'product_id INT,'
#                'quantity INT,'
#                'order_date DATE,'
#                'FOREIGN KEY (product_id) REFERENCES products(id))')

# sql_products = 'INSERT INTO products (name, category, price) VALUES (%s, %s, %s)'
# val_products = [
#     ('Laptop', 'Electrocasnice', 1500.00),
#     ('Telefon', 'Electrocasnice', 800.00),
# ]
# cursor.executemany(sql_products, val_products)
# my_db.commit()
#
# sql = 'INSERT INTO orders (product_id, quantity, order_date) VALUES (%s, %s, %s)'
# val = [
#     (1, 2, '2023-09-01'),
#     (2, 1, '2023-09-02')
# ]
# cursor.executemany(sql, val)
# my_db.commit()

# 2. transform
query = ("SELECT o.id, p.name, p.category, o.quantity, p.price"
         " from orders o JOIN products p ON o.product_id = p.id")
df = pandas.read_sql(query, my_db)
print(df)
df['total'] = df['quantity'] * df['price']
print(df)
# 3. load
df.to_csv('raport_vanzari.csv', index=False)
# cursor.execute('CREATE TABLE raport_vanzari (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'category VARCHAR(50),'
#                'quantity INT,'
#                'price DECIMAL(10, 2),'
#                'total DECIMAL(10, 2))')
sql = "INSERT INTO raport_vanzari (name, category, quantity, price, total) VALUES (%s, %s, %s, %s, %s)"
lista = []
for item, row in df.iterrows():
    lista.append(row.tolist()[1:])
cursor.executemany(sql, lista)
my_db.commit()

