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
# cursor.execute('CREATE TABLE sales (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'reqion VARCHAR(50),'
#                'category VARCHAR(50),'
#                'sales_amount DECIMAL(10, 2),'
#                'sale_date DATE)')
# sql = 'INSERT INTO sales (reqion, category, sales_amount, sale_date) values (%s, %s, %s, %s)'
# val = [
#     ('EST', 'Electrocasnice', 3000.00, '2024-01-01'),
#     ('VEST', 'LEGUME', 500.00, '2024-01-02'),
#     ('EST', 'Mobilier', 3000.00, '2024-02-01'),
# ]
# cursor.executemany(sql, val)
# my_db.commit()

# 2
query = 'SELECT * FROM sales'
df_sales = pandas.read_sql(query, my_db)
print(df_sales)
df_sales_grupat = df_sales.groupby('reqion')['sales_amount'].sum().reset_index()
print(df_sales_grupat)

# 3
df_sales_grupat.to_csv('raport_vanzari_pe_regiuni.csv', index=False)
