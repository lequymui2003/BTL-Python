import sys
import os
import hashlib
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Database import database



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 592)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(200, 60, 361, 481))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtHoVaTen = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtHoVaTen.setGeometry(QtCore.QRect(10, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtHoVaTen.setFont(font)
        self.txtHoVaTen.setObjectName("txtHoVaTen")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtUsername = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtUsername.setGeometry(QtCore.QRect(10, 170, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPassword = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtPassword.setGeometry(QtCore.QRect(10, 250, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtEmail.setGeometry(QtCore.QRect(10, 330, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.btnDangky = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDangky.setGeometry(QtCore.QRect(100, 400, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnDangky.setFont(font)
        self.btnDangky.setObjectName("btnDangky")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btnDangky.clicked.connect(self.handleRegister)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Đăng ký"))
        self.label.setText(_translate("Dialog", "Họ và tên:"))
        self.txtHoVaTen.setPlaceholderText(_translate("Dialog", "Nhập họ và tên"))
        self.label_2.setText(_translate("Dialog", "Tên đăng nhập:"))
        self.txtUsername.setPlaceholderText(_translate("Dialog", "Nhập tên đăng nhập"))
        self.label_3.setText(_translate("Dialog", "Mật khẩu:"))
        self.txtPassword.setPlaceholderText(_translate("Dialog", "Nhập mật khẩu"))
        self.label_4.setText(_translate("Dialog", "Email:"))
        self.txtEmail.setPlaceholderText(_translate("Dialog", "Nhập Email"))
        self.btnDangky.setText(_translate("Dialog", "Đăng ký"))

    # Hàm mã hóa mật khẩu
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def handleRegister(self):
        ho_va_ten = self.txtHoVaTen.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        email = self.txtEmail.text()

        # Kiểm tra xem người dùng đã nhập đầy đủ thông tin chưa
        if not ho_va_ten or not username or not password or not email:
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Vui lòng nhập đầy đủ thông tin.", QtWidgets.QMessageBox.StandardButton.Ok)
            return
        
         # Kiểm tra định dạng email
        if not email.endswith("@gmail.com"):
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Email không hợp lệ. Vui lòng nhập email hợp lệ với tên miền @gmail.com.", QtWidgets.QMessageBox.StandardButton.Ok)
            return

        # Mã hóa mật khẩu
        hashed_password = self.hash_password(password)

        # Kiểm tra xem tên đăng nhập đã tồn tại trong cơ sở dữ liệu chưa
        connection = database.create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            QtWidgets.QMessageBox.warning(None, "Thông báo", "Tên đăng nhập đã tồn tại. Vui lòng chọn tên đăng nhập khác.", QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            # Thêm người dùng mới vào cơ sở dữ liệu
            #print(f"hashed_password: {hashed_password}")
            insert_query = "INSERT INTO users (username, password, Name, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (username, hashed_password, ho_va_ten, email))
            connection.commit()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Đăng ký thành công!", QtWidgets.QMessageBox.StandardButton.Ok)
            self.closeDialogAndShowLogin(Dialog)

        # Đóng kết nối
        cursor.close()
        connection.close()

    def closeDialogAndShowLogin(self, Dialog):
        # Đóng form đăng ký
        Dialog.close()

        # Hiển thị form đăng nhập (MainWindow)
        self.showLoginWindow()
    def showLoginWindow(self):
        # Tạo và hiển thị form đăng nhập
        from Login import Ui_MainWindow
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_MainWindow()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())