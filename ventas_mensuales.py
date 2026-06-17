import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt



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

#convierte Mes a numero y ordena
df['mes']=pd.to_numeric(df['mes'])
df = df.sort_values('mes')


#grafico de ventas mensuales 
plt.figure(figsize=(10, 5))
plt.plot(df['mes'], df['total_ventas'], marker='o', linewidth=2, color='#1f77b4')
plt.title('Ventas mensuales - Base sakila ', fontsize=14, fontweight='bold')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales $')
plt.xticks(df['mes'])
plt.grid(True, alpha=0.3)
plt.tight_layout()

#guarda la imagen
plt.savefig('ventas_mensuales.png', dpi=300)
plt.show()

print("grafico guardado como ventas_mensuales.png")


conn.close()
print("csv generado: ventas_mensuales.csv ")
print(df.head)






































