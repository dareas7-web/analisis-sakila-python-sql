import mysql.connector
import pandas as pd


# conexion a sakila
conn = mysql.connector.connect(
    host="localhost",
    user="root", #cambia si usas otro usuario
    password="123qwasZ@",
    database="sakila"
)

#query sql: ventas por mes
query= """
SELECT 
    YEAR(payment_date) AS año,
    MONTH(payment_date) AS mes,
    COUNT(payment_id) AS cantidad_rentas,
    SUM(amount) AS total_ventas
FROM payment
GROUP BY YEAR(payment_date), MONTH(payment_date)    
ORDER BY año, mes;

"""
#Ejecuta y guarda CSV
df = pd.read_sql(query, conn)
df.to_csv('ventas_por_mes.csv', index=False, encoding='utf-8')

conn.close()
print("csv generado: ventas_mensuales.csv ")
print(df.head)






































