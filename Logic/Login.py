import sys
import os
import hashlib
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
# Thêm thư mục gốc (chứa thư mục Database) vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# Import module database từ thư mục Database
from Database import database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 592)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 70, 361, 441))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnDangnhap = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDangnhap.setGeometry(QtCore.QRect(20, 300, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnDangnhap.setFont(font)
        self.btnDangnhap.setObjectName("btnDangnhap")
        self.btnDangky = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDangky.setGeometry(QtCore.QRect(20, 370, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnDangky.setFont(font)
        self.btnDangky.setObjectName("btnDangky")
        self.txtUsername = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtUsername.setGeometry(QtCore.QRect(20, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtPassword.setGeometry(QtCore.QRect(20, 200, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.LinkQuenMatKhau = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.LinkQuenMatKhau.setGeometry(QtCore.QRect(20, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LinkQuenMatKhau.setFont(font)
        self.LinkQuenMatKhau.setObjectName("LinkQuenMatKhau")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnDangnhap.clicked.connect(self.handleLogin)
        self.btnDangky.clicked.connect(self.openRegisterWindow)
        self.LinkQuenMatKhau.clicked.connect(self.openForgetPasswordWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Đăng nhập"))
        self.label.setText(_translate("MainWindow", "Tên đăng nhập:"))
        self.label_2.setText(_translate("MainWindow", "Mật khẩu:"))
        self.btnDangnhap.setText(_translate("MainWindow", "Đăng nhập"))
        self.btnDangky.setText(_translate("MainWindow", "Đăng ký"))
        self.LinkQuenMatKhau.setText(_translate("MainWindow", "Quên mật khẩu?"))
        self.txtUsername.setPlaceholderText(_translate("MainWindow", "Nhập tên đăng nhập"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Nhập mật khẩu"))


    def handleLogin(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()

        # Kiểm tra xem người dùng đã nhập tên đăng nhập và mật khẩu chưa
        if not username or not password:
            QMessageBox.warning(None, "Thông báo", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!")
            return

        # Mã hóa mật khẩu nhập vào để so sánh với mật khẩu đã lưu trong cơ sở dữ liệu
        hashed_password = self.hash_password(password)

        # Kết nối đến cơ sở dữ liệu
        connection = database.create_connection()
        cursor = connection.cursor()

        # Kiểm tra thông tin đăng nhập
        query = "SELECT password, role FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            password = user[0]
            role = user[1]
            #print(f"hashed_password: {hashed_password}")
            #print(f"password: {password}")
            if hashed_password == password:
                if role == 'admin':
                    QMessageBox.information(None, "Thông báo", "Đăng nhập thành công! Bạn là admin.")
                else:
                    QMessageBox.information(None, "Thông báo", "Đăng nhập thành công! Bạn là user.")
            else:
                QMessageBox.warning(None, "Thông báo", "Tên đăng nhập hoặc mật khẩu không đúng!")
        else:
            QMessageBox.warning(None, "Thông báo", "Tên đăng nhập hoặc mật khẩu không đúng!")

        # Đóng kết nối
        cursor.close()
        connection.close()


    # Hàm mã hóa mật khẩu
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def openRegisterWindow(self):
        from Register import Ui_Dialog
        self.secondWindow = QtWidgets.QMainWindow()
        self.ui_second = Ui_Dialog()
        self.ui_second.setupUi(self.secondWindow)
        self.secondWindow.show()
    def openForgetPasswordWindow(self):
        from Forgetpassword import Ui_Dialog
        self.ForgetpasswordWindow = QtWidgets.QMainWindow()
        self.ui_second = Ui_Dialog()
        self.ui_second.setupUi(self.ForgetpasswordWindow)
        self.ForgetpasswordWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
