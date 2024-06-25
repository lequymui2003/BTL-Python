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
def delete_MH(id_mon):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM monhoc WHERE idMon = %s"
        cursor.execute(query, (id_mon,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_MH(ten_MH):
        
        connection = create_connection()
        cursor = connection.cursor()

        # Câu truy vấn SQL để tìm kiếm phòng học theo tên
        query = "SELECT * FROM monhoc WHERE tenMon LIKE %s"
        cursor.execute(query, (f"%{ten_MH}%",))

        # Lấy tất cả các kết quả từ câu truy vấn
        result = cursor.fetchall()

        return result
# thêm, sửa, xóa, tìm kiếm hiển thị bảng lớp học
def load_dataLH():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM lop"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_LH(id_lop, ten_lop, id_khoa):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM lop WHERE idLop = %s OR tenLop = %s"
    cursor.execute(query_check, (id_lop, ten_lop))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO lop (idLop, tenLop, idKhoa) VALUES (%s, %s, %s)"
    cursor.execute(query_insert, (id_lop, ten_lop, id_khoa))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_LH(id_lop, ten_lop, id_khoa):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM lop WHERE idLop = %s"
    cursor.execute(query_check, (id_lop,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE lop SET tenLop = %s, idKhoa = %s WHERE idLop = %s"
    cursor.execute(query_update, (ten_lop, id_khoa, id_lop))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_LH(id_Lop):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM lop WHERE idlop = %s"
        cursor.execute(query, (id_Lop,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_LH(ten_lop):
        
        connection = create_connection()
        cursor = connection.cursor()

       
        query = "SELECT * FROM lop WHERE tenLop LIKE %s"
        cursor.execute(query, (f"%{ten_lop}%",))

   
        result = cursor.fetchall()

        return result
# thêm, sửa, xóa, tìm kiếm hiển thị bảng Khoa
def load_dataKhoa():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM khoa"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_Khoa(id_khoa, ten_Khoa):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM khoa WHERE idKhoa = %s OR tenKhoa = %s"
    cursor.execute(query_check, (id_khoa, ten_Khoa))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO khoa (idKhoa, tenKhoa) VALUES (%s, %s)"
    cursor.execute(query_insert, (id_khoa, ten_Khoa))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_Khoa(id_khoa, ten_khoa):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM khoa WHERE idkhoa = %s"
    cursor.execute(query_check, (id_khoa,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE khoa SET tenKhoa = %s WHERE idKhoa = %s"
    cursor.execute(query_update, (ten_khoa,id_khoa))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_Khoa(id_Khoa):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM khoa WHERE idkhoa = %s"
        cursor.execute(query, (id_Khoa,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_Khoa(ten_Khoa):
        
        connection = create_connection()
        cursor = connection.cursor()

       
        query = "SELECT * FROM khoa WHERE tenKhoa LIKE %s"
        cursor.execute(query, (f"%{ten_Khoa}%",))

   
        result = cursor.fetchall()

        return result













