import mysql.connector
from mysql.connector import pooling
import psycopg2

productID = input("id: ")
x = int(productID)
productName = input("name: ")
productDescription = input("description: ")
productCategory = input("categoty: ")


# establish a database connection connecting to a catalog

db = psycopg2.connect(
    host='capsuite.postgres.database.azure.com',
    database='Capsuite',
    user='capsuite@capsuite',
    password='Cap@_100',
    port=5432
)

# create a connection object
connection_object = db

# you must create a Cursor object. It will let
cur = connection_object.cursor()

# you execute all the queries you need and create a unique database name
cur.execute("insert into products(productID,productName,productDescription,productCategory) values (%s,%s,%s,$s)", (x, productName, productDescription, productCategory))

# terminate the database connection
cur.close()