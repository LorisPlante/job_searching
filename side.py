import sqlite3

DATABASE = 'database.db'
SCHEMA = 'db_schema.sql'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

with open(SCHEMA, 'r') as f:
    schema = f.read()
connection.executescript(schema)

query = "INSERT INTO jobs (job_type, job_status, job_date, job_compagny_name, job_name, job_location, job_description) VALUES (?, ?, ?, ?, ?, ?, ?)"
cursor.execute(query, ("Alternance", "Non", "21/07/2024", "Renault", "Mécanicien", "14 rue du porche, 87510 Mulouse, France", "Ce poste consiste a réparer des voiture et avoir des cours"))
connection.commit()

rows = cursor.execute("SELECT * FROM jobs")
for row in rows:
    print(row)


