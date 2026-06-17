import mysql.connector

conn = mysql.connector.connect(
	host="localhost",
	user="root",
	password="AQUI_VA_TU_PASSWORD",
	database="sakila"

)
cursor = conn.cursor()
query = """
SELECT c.customer_id,
	CONCAT(c.first_name, ' ', c.last_name) AS cliente,
	SUM(p.amount) AS total_gastado,
	COUNT(r.rental_id) AS total_rentas
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_gastado DESC
LIMIT 5;
"""
cursor.execute(query)

print(f"{'ID':<10} {'Cliente':>20} {'TOtal gastado':<15} {'total rentas'} ")
print("-"*60)
for row in cursor.fetchall():
	print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]}")
conn.close()






