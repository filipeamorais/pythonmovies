import psycopg2

#url = "postgres://xbsahsxo:q8KLP4sf2WZ6uY7P-zAxSiMnwzFh67FN@kashin.db.elephantsql.com/xbsahsxo"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()

