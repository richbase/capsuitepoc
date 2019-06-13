# python 3
from flask import Flask
import createDatabase as cd
import mysql.connector
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection
import MySQLdb
from sqlite3 import OperationalError
import uuid
from flask_mail import Mail, Message
import numpy as np

password = ""
confirm_password = ""

app = Flask(__name__)
mail = Mail(app)

def password_confirm():
    password = input("enter password: ")
    confirm_password = input("confirm password: ")

    while True:
        flag = False
        if password == confirm_password:

            break
        else:
            print("enter matching passwords")
            password_confirm()

        if flag:
            break
        break
    return password, confirm_password
    pass

def register():
    companyName = input("enter company Name: ")
    email = input("provide your email: ")
    password_confirm()

    # establish a database connection connecting to a catalog

    db = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="connect_to_sql_server",
        pool_size=1,
        pool_reset_session=True,
        host="localhost",  # your host, usually localhost
        user="root",  # your username
        passwd="root",  # your password
        db="catalog"
    )

    # create a connection object
    connection_object = db.get_connection()

    # you must create a Cursor object. It will let
    cur = connection_object.cursor()

    uniqueUserID = str(uuid.uuid4())
    databaseName = uniqueUserID.replace("-", "")

    # you execute all the queries you need and create a unique database name
    cur.execute("insert into catalog(databaseID, CIN) values (%s,%s)", (databaseName, companyName))
    cd.createdb(databaseName)
    emialVarificationCode(email)

    # terminate the database connection
    cur.close()


def emialVarificationCode(email):
    with app.app_context():
        app.config['DEBUG'] = True
        app.config['MAIL_SERVER'] = 'Outlook.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_DEBUG'] = app.debug
        app.config['MAIL_USERNAME'] = "masolejoseph@live.com"
        app.config['MAIL_PASSWORD'] = "mcjoemasole11210"
        app.config['MAIL_DEFAULT_SENDER'] = ""
        app.config['MAIL_MAX_EMAILS'] = None
        app.config['MAIL_SUPPRESS_SEND'] = app.testing
        app.config['MAIL_ASCII_ATTACHMENTS'] = False

        #mail = Mail()
        mail.connect()
        varificationCode = str(np.random.randint(1000, 2000))

        msg = Message("Your Varification code is: " + varificationCode,
                      recipients=[email])

        mail.send(msg)

emialVarificationCode("masolejoseph@gmail.com")





