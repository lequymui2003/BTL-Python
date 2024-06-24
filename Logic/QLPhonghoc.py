import sys
import os
# Thêm thư mục gốc (chứa thư mục Database) vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# Import module database từ thư mục Database
from Database import database


def add_phong_hoc(ten_phong):
    connection = database.create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO phonghoc (tenPhong) VALUES (%s)"
    cursor.execute(query, (ten_phong,))
    connection.commit()
    cursor.close()
    connection.close()

def update_phong_hoc(phong_id, ten_phong):
    connection = database.create_connection()
    cursor = connection.cursor()
    query = "UPDATE phonghoc SET tenPhong = %s WHERE idPhong = %s"
    cursor.execute(query, (ten_phong, phong_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_phong_hoc(phong_id):
    connection = database.create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM phonghoc WHERE idPhong = %s"
    cursor.execute(query, (phong_id,))
    connection.commit()
    cursor.close()
    connection.close()

def search_phong_hoc(ten_phong):
    connection = database.create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM phonghoc WHERE tenPhong LIKE %s"
    cursor.execute(query, ('%' + ten_phong + '%',))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_all_phong_hoc():
    connection = database.create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM phonghoc"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
