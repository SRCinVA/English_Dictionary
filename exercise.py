import mysql.connector  # to establish a connection to the DB

con = mysql.connector.connect( # notice that everything is a string
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

# to query data

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay'")
results = cursor.fetchall()

print(results)  # the resulting list is a large group of tuples.

