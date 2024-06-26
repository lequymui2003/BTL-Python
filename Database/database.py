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
def get_all_csvc():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT id, ten FROM cosovatchat"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def get_all_phonghoc():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT idPhong, tenPhong FROM phonghoc"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def get_all_name_khoa():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idKhoa FROM khoa"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
def get_all_name_lop():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idLop FROM lop"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
def get_all_name_Phong():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idPhong FROM phonghoc"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
def get_all_name_GV():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idGiangVien FROM giangvien"
        cursor.execute(query)
        results = cursor.fetchall()
        return [row[0] for row in results]
def get_all_name_Mon():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT idMon FROM monhoc"
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
# thêm, sửa, xóa, tìm kiếm hiển thị bảng Giảng viên
def load_dataGV():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT idGiangVien, tenGV, sdt, idKhoa FROM giangvien"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_GV(id_GV, ten_GV, sdt, id_Khoa):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM giangvien WHERE idGiangVien = %s"
    cursor.execute(query_check, (id_GV,))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO giangvien (idGiangVien,tenGV, sdt, idKhoa ) VALUES (%s, %s, %s, %s)"
    cursor.execute(query_insert, (id_GV, ten_GV, sdt, id_Khoa))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_GV(id_GV, ten_GV, sdt, id_Khoa):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM giangvien WHERE idGiangVien = %s"
    cursor.execute(query_check, (id_GV,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE giangvien SET tenGV = %s, sdt = %s, idKhoa = %s WHERE idGiangVien = %s"  
    cursor.execute(query_update, (ten_GV, sdt, id_Khoa, id_GV))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_GV(id_GV):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM giangvien WHERE idGiangVien = %s"
        cursor.execute(query, (id_GV,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_GV(ten_GV):
        
        connection = create_connection()
        cursor = connection.cursor()

       
        query = "SELECT idGiangVien, tenGV, sdt, idKhoa FROM giangvien WHERE tenGV LIKE %s"
        cursor.execute(query, (f"%{ten_GV}%",))

   
        result = cursor.fetchall()

        return result
# thêm, sửa, xóa, tìm kiếm hiển thị bảng cơ sở vật chất
def load_dataCSVC():
    connection = create_connection()
    cursor = connection.cursor()
    query = """SELECT 
                    ctcosovatchat.stt, 
                    ctcosovatchat.id, 
                    cosovatchat.ten, 
                    ctcosovatchat.idPhong, 
                    phonghoc.tenPhong, 
                    ctcosovatchat.SoLuongTot, 
                    ctcosovatchat.SoLuongXau 
                FROM 
                    ctcosovatchat 
                JOIN 
                    cosovatchat ON ctcosovatchat.id = cosovatchat.id 
                JOIN 
                    phonghoc ON ctcosovatchat.idPhong = phonghoc.idPhong"""
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_CSVC(id_CSVC, id_Phong, SoLuongTot, SoLuongXau):

    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM ctcosovatchat WHERE id = %s AND idPhong = %s"
    cursor.execute(query_check, (id_CSVC, id_Phong))
    if cursor.fetchone():
        cursor.close()
        connection.close()
        return False  

    query_insert = "INSERT INTO ctcosovatchat (id, idPhong, SoLuongTot, SoLuongXau ) VALUES (%s, %s, %s, %s)"
    cursor.execute(query_insert, (id_CSVC, id_Phong, SoLuongTot, SoLuongXau))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_CSVC(id_CSVC, id_Phong, SoLuongTot, SoLuongXau):
    connection = create_connection()
    cursor = connection.cursor()

    query_check = "SELECT * FROM ctcosovatchat WHERE id = %s"
    cursor.execute(query_check, (id_CSVC,))
    if not cursor.fetchall():
        cursor.close()
        connection.close()
        return False  

    query_update = "UPDATE ctcosovatchat SET  SoLuongTot = %s, SoLuongXau = %s WHERE id = %s AND idPhong = %s"  
    cursor.execute(query_update, (SoLuongTot, SoLuongXau, id_CSVC, id_Phong))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_CSVC(stt):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM ctcosovatchat WHERE stt = %s"
        cursor.execute(query, (stt,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_CSVC(ten_Phong):
        
        connection = create_connection()
        cursor = connection.cursor()

       
        query = """SELECT 
                    ctcosovatchat.stt, 
                    ctcosovatchat.id, 
                    cosovatchat.ten, 
                    ctcosovatchat.idPhong, 
                    phonghoc.tenPhong, 
                    ctcosovatchat.SoLuongTot, 
                    ctcosovatchat.SoLuongXau 
                FROM 
                    ctcosovatchat 
                JOIN 
                    cosovatchat ON ctcosovatchat.id = cosovatchat.id 
                JOIN 
                    phonghoc ON ctcosovatchat.idPhong = phonghoc.idPhong
                WHERE phonghoc.tenphong LIKE %s    
                    """
        cursor.execute(query, (f"%{ten_Phong}%",))

   
        result = cursor.fetchall()

        return result
# thêm, sửa, xóa, tìm kiếm hiển thị bảng xếp lịch
def load_dataXeplich():
    connection = create_connection()
    cursor = connection.cursor()
    query = """SELECT 
                    id,
                    idKhoa,
                    idLop,
                    idGV,
                    idMon,
                    idPhong,
                    Date,
                    ThoiGian,
                    tinhTrang
                FROM 
                    xeplich 
                    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_Xeplich(ten_Phong, ten_Khoa, ten_Mon, ten_GV, ten_Lop, ngay, thoigian, tinhTrang):

    connection = create_connection()
    cursor = connection.cursor() 

    query_insert = "INSERT INTO xeplich (idKhoa, idLop, idGV, idMon, idPhong, Date, ThoiGian, tinhTrang ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query_insert, (ten_Khoa, ten_Lop, ten_GV, ten_Mon, ten_Phong, ngay, thoigian, tinhTrang))
    connection.commit()
    cursor.close()
    connection.close()

    return True
def update_Xeplich(id, ten_Phong, ten_Khoa, ten_Mon, ten_GV, ten_Lop, ngay, thoigian, tinhTrang):
    connection = create_connection()
    cursor = connection.cursor()

    query_update = """UPDATE xeplich SET  idKhoa = %s, idLop = %s, 
    idGV = %s, idMon = %s, idPhong = %s, Date = %s, ThoiGian = %s, TinhTrang = %s
    WHERE id = %s"""  
    cursor.execute(query_update, (ten_Khoa, ten_Lop, ten_GV, ten_Mon, ten_Phong, ngay, thoigian, tinhTrang, id))
    connection.commit()
    cursor.close()
    connection.close()

    return True 
def delete_Xeplich(id):
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM xeplich WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

        return True
def search_Xeplich(tinhTrang):
        
        connection = create_connection()
        cursor = connection.cursor()

       
        query = """SELECT 
                    id,
                    idKhoa,
                    idLop,
                    idGV,
                    idMon,
                    idPhong,
                    Date,
                    ThoiGian,
                    tinhTrang
                FROM 
                    xeplich 
                WHERE tinhTrang LIKE %s    
                    """
        cursor.execute(query, (f"%{tinhTrang}%",))

   
        result = cursor.fetchall()

        return result




