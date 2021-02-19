import mysql.connector  # to establish a connection to the DB

con = mysql.connector.connect( # notice that everything is a string
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

# to query data

cursor = con.cursor()

word = input("Enter a word, please: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
results = cursor.fetchall()

# first, make sure that it's a sensible word (like before)
if results:

# you need to construct a loop to pull out the tuples (which are separate definitions)
    for result in results:
        print(result[1]) # result[1] would have printed just the definitions

else:
    print("We need a real word, please!")
