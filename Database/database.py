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
    query = "SELECT * FROM phonghoc"
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