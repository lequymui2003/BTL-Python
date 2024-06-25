import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_phonghoc'
    )
    return connection
def get_all_id_khoa():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idKhoa FROM khoa"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
# thêm, sửa, xóa, tìm kiếm hiển thị bảng Phòng học
def load_data():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT idPhong, tenPhong FROM phonghoc"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_phong(id_phong, ten_phong):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM phonghoc WHERE idPhong = %s OR tenPhong = %s"
    cursor.execute(query_check, (id_phong, ten_phong))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO phonghoc (idPhong, tenPhong) VALUES (%s, %s)"
    cursor.execute(query_insert, (id_phong, ten_phong))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_phong(id_phong, ten_phong):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM phonghoc WHERE idPhong = %s"
    cursor.execute(query_check, (id_phong,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE phonghoc SET tenPhong = %s WHERE idPhong = %s"
    cursor.execute(query_update, (ten_phong, id_phong))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_phong(id_phong):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM phonghoc WHERE idPhong = %s"
        cursor.execute(query, (id_phong,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_phong(ten_phong):
        
        connection = create_connection()
        cursor = connection.cursor()

        # Câu truy vấn SQL để tìm kiếm phòng học theo tên
        query = "SELECT idPhong, tenPhong FROM phonghoc WHERE tenPhong LIKE %s"
        cursor.execute(query, (f"%{ten_phong}%",))

        # Lấy tất cả các kết quả từ câu truy vấn
        result = cursor.fetchall()

        return result
# thêm, sửa, xóa, tìm kiếm hiển thị bảng môn học
def load_data_monhoc():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM monhoc"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_monhoc(id_mon, ten_mon, so_tin_chi, id_khoa):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM monhoc WHERE idMon = %s OR tenMon = %s"
    cursor.execute(query_check, (id_mon, ten_mon))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO monhoc (idMon, tenMon, soTinChi, idKhoa) VALUES (%s, %s, %s, %s)"
    cursor.execute(query_insert, (id_mon, ten_mon, so_tin_chi, id_khoa))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_MH(id_mon, ten_mon, so_tin_chi, id_khoa):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM monhoc WHERE idMon = %s"
    cursor.execute(query_check, (id_mon,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE monhoc SET tenMon = %s, soTinChi = %s, idKhoa = %s WHERE idMon = %s"
    cursor.execute(query_update, (ten_mon, so_tin_chi, id_khoa, id_mon))
    connection.commit()
    cursor.close()
    connection.close()

    return True 





