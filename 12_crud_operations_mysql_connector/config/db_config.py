import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="",
        port=0,
        user="",
        password="",
        database=""
    )
    return connection
