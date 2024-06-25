import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_phonghoc'
    )
    return connection

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

    # Kiểm tra trùng lặp ID phòng hoặc Tên phòng
    query_check = "SELECT * FROM phonghoc WHERE idPhong = %s OR tenPhong = %s"
    cursor.execute(query_check, (id_phong, ten_phong))
    if cursor.fetchone():
        # Đóng cursor và kết nối
        cursor.close()
        connection.close()
        return False  # Trả về False nếu ID phòng hoặc Tên phòng đã tồn tại

    # Thực thi truy vấn để thêm dữ liệu
    query_insert = "INSERT INTO phonghoc (idPhong, tenPhong) VALUES (%s, %s)"
    cursor.execute(query_insert, (id_phong, ten_phong))

    # Lưu thay đổi vào cơ sở dữ liệu
    connection.commit()

    # Đóng cursor và kết nối
    cursor.close()
    connection.close()

    return True

def update_phong(id_phong, ten_phong):
    connection = create_connection()
    cursor = connection.cursor()

    # Kiểm tra xem phòng học có tồn tại không
    query_check = "SELECT * FROM phonghoc WHERE idPhong = %s"
    cursor.execute(query_check, (id_phong,))
    if not cursor.fetchone():
        cursor.close()
        connection.close()
        return False  # Trả về False nếu phòng học không tồn tại

    # Cập nhật thông tin phòng học
    query_update = "UPDATE phonghoc SET tenPhong = %s WHERE idPhong = %s"
    cursor.execute(query_update, (ten_phong, id_phong))

    # Lưu thay đổi vào cơ sở dữ liệu
    connection.commit()

    # Đóng cursor và kết nối
    cursor.close()
    connection.close()

    return True  # Trả về True nếu cập nhật thành công
# Hàm xóa phòng học từ cơ sở dữ liệu
def delete_phong(id_phong):
        # Kết nối đến cơ sở dữ liệu
        connection = create_connection()
        cursor = connection.cursor()

        # Xây dựng câu lệnh SQL để xóa phòng học với ID_Phong nhất định
        query = "DELETE FROM phonghoc WHERE idPhong = %s"
        cursor.execute(query, (id_phong,))

        # Lưu thay đổi vào cơ sở dữ liệu
        connection.commit()

        # Đóng cursor và kết nối
        cursor.close()
        connection.close()

        return True