import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='', 
        database='db_phonghoc'  
    )
    return connection
