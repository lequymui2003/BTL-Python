
# -*- coding: utf-8 -*-
import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QTreeWidget, QTreeWidgetItem, QLineEdit, QPushButton
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Database import database

class Ui_Dialog(object):
    def __init__(self, session):
        self.session = session
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 500)
        self.label_30 = QtWidgets.QLabel(parent=Dialog)
        self.label_30.setGeometry(QtCore.QRect(20, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(230, 0, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtIDDKPH = QtWidgets.QLineEdit(parent=Dialog)
        self.txtIDDKPH.setGeometry(QtCore.QRect(130, 90, 181, 31))
        self.txtIDDKPH.setObjectName("txtIDDKPH")
        self.label_22 = QtWidgets.QLabel(parent=Dialog)
        self.label_22.setGeometry(QtCore.QRect(20, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.cbBoxTenKhoa_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTenKhoa_DKPH.setGeometry(QtCore.QRect(130, 140, 181, 31))
        self.cbBoxTenKhoa_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenKhoa_DKPH.setObjectName("cbBoxTenKhoa_DKPH")
        self.label_23 = QtWidgets.QLabel(parent=Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.cbBoxTenLop_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTenLop_DKPH.setGeometry(QtCore.QRect(130, 190, 181, 31))
        self.cbBoxTenLop_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenLop_DKPH.setObjectName("cbBoxTenLop_DKPH")
        self.label_24 = QtWidgets.QLabel(parent=Dialog)
        self.label_24.setGeometry(QtCore.QRect(20, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.cbBoxTenGV_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTenGV_DKPH.setGeometry(QtCore.QRect(130, 240, 181, 31))
        self.cbBoxTenGV_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenGV_DKPH.setObjectName("cbBoxTenGV_DKPH")
        self.label_25 = QtWidgets.QLabel(parent=Dialog)
        self.label_25.setGeometry(QtCore.QRect(20, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.cbBoxtenMon_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxtenMon_DKPH.setGeometry(QtCore.QRect(130, 290, 181, 31))
        self.cbBoxtenMon_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxtenMon_DKPH.setObjectName("cbBoxtenMon_DKPH")
        self.label_26 = QtWidgets.QLabel(parent=Dialog)
        self.label_26.setGeometry(QtCore.QRect(20, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.cbBoxTenPhong_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTenPhong_DKPH.setGeometry(QtCore.QRect(130, 340, 181, 31))
        self.cbBoxTenPhong_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenPhong_DKPH.setObjectName("cbBoxTenPhong_DKPH")
        self.label_27 = QtWidgets.QLabel(parent=Dialog)
        self.label_27.setGeometry(QtCore.QRect(390, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.txtNgay_DKPH = QtWidgets.QLineEdit(parent=Dialog)
        self.txtNgay_DKPH.setGeometry(QtCore.QRect(470, 90, 181, 31))
        self.txtNgay_DKPH.setObjectName("txtNgay_DKPH")
        self.label_28 = QtWidgets.QLabel(parent=Dialog)
        self.label_28.setGeometry(QtCore.QRect(390, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.cbBoxTG_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTG_DKPH.setGeometry(QtCore.QRect(470, 140, 181, 31))
        self.cbBoxTG_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTG_DKPH.setObjectName("cbBoxTG_DKPH")
        self.cbBoxTG_DKPH.addItem("")
        self.cbBoxTG_DKPH.addItem("")
        self.cbBoxTG_DKPH.addItem("")
        self.cbBoxTG_DKPH.addItem("")
        self.label_29 = QtWidgets.QLabel(parent=Dialog)
        self.label_29.setGeometry(QtCore.QRect(390, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.cbBoxTinhTrang_DKPH = QtWidgets.QComboBox(parent=Dialog)
        self.cbBoxTinhTrang_DKPH.setGeometry(QtCore.QRect(470, 190, 181, 31))
        self.cbBoxTinhTrang_DKPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTinhTrang_DKPH.setObjectName("cbBoxTinhTrang_DKPH")
        self.cbBoxTinhTrang_DKPH.addItem("")
        self.btnDKPH = QtWidgets.QPushButton(parent=Dialog)
        self.btnDKPH.setGeometry(QtCore.QRect(260, 410, 151, 51))
        self.btnDKPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDKPH.setObjectName("btnDKPH")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.checkSession(Dialog)
        self.btnDKPH.clicked.connect(self.handleAddDKLH)

        self.load_name_Khoa()
        self.load_name_GV()
        self.load_name_Lop()
        self.load_name_Mon()
        self.load_name_Phong()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_30.setText(_translate("Dialog", "ID:"))
        self.label.setText(_translate("Dialog", "Đăng ký phòng học"))
        self.label_22.setText(_translate("Dialog", "Tên khoa:"))
        self.label_23.setText(_translate("Dialog", "Tên Lớp:"))
        self.label_24.setText(_translate("Dialog", "Tên giảng viên:"))
        self.label_25.setText(_translate("Dialog", "Tên môn:"))
        self.label_26.setText(_translate("Dialog", "Tên phòng:"))
        self.label_27.setText(_translate("Dialog", "Ngày:"))
        self.label_28.setText(_translate("Dialog", "Thời gian:"))
        self.cbBoxTG_DKPH.setItemText(0, _translate("Dialog", "Ca 1 "))
        self.cbBoxTG_DKPH.setItemText(1, _translate("Dialog", "Ca 2"))
        self.cbBoxTG_DKPH.setItemText(2, _translate("Dialog", "Ca 3"))
        self.cbBoxTG_DKPH.setItemText(3, _translate("Dialog", "Ca 4"))
        self.label_29.setText(_translate("Dialog", "Tình trạng:"))
        self.cbBoxTinhTrang_DKPH.setItemText(0, _translate("Dialog", "Đã đăng ký"))
        self.btnDKPH.setText(_translate("Dialog", "Đăng ký phòng học"))

    def load_name_Khoa(self):
        name_khoa_list = database.get_all_name_khoa()
        self.cbBoxTenKhoa_DKPH.addItems(name_khoa_list)
    def load_name_Lop(self):
        name_lop_list = database.get_all_name_lop()
        self.cbBoxTenLop_DKPH.addItems(name_lop_list)
    def load_name_Phong(self):
        name_Phong_list = database.get_all_name_Phong()
        self.cbBoxTenPhong_DKPH.addItems(name_Phong_list)
    def load_name_GV(self):
        name_GV_list = database.get_all_name_GV()
        self.cbBoxTenGV_DKPH.addItems(name_GV_list)
    def load_name_Mon(self):
        name_Mon_list = database.get_all_name_Mon()
        self.cbBoxtenMon_DKPH.addItems(name_Mon_list)

    def handleAddDKLH(self):
        id = self.txtIDDKPH.text().strip()
        ten_Phong = self.cbBoxTenPhong_DKPH.currentText().strip()
        ten_Khoa = self.cbBoxTenKhoa_DKPH.currentText().strip()
        ten_Mon = self.cbBoxtenMon_DKPH.currentText().strip()
        ten_GV = self.cbBoxTenGV_DKPH.currentText().strip()
        ten_Lop = self.cbBoxTenLop_DKPH.currentText().strip()
        ngay = self.txtNgay_DKPH.text().strip()
        thoigian = self.cbBoxTG_DKPH.currentText().strip()
        tinhTrang = self.cbBoxTinhTrang_DKPH.currentText().strip()

    # Kiểm tra điều kiện trước khi thêm vào cơ sở dữ liệu
        if not ngay:
                QMessageBox.warning(self.txtIDDKPH,"Thông báo", "Vui lòng nhập đầy đủ thông tin!")
                return

    # Kiểm tra phòng học đã được đăng ký vào thời gian đó chưa
        if database.check_Phong_Gio(ten_Phong, ngay, thoigian):
                QMessageBox.warning(self.txtIDDKPH,"Thông báo", "Phòng học đã được đăng ký vào thời gian này!")
                return

    # Kiểm tra giảng viên có dạy vào thời gian đó chưa
        if database.check_GV_Gio(ten_GV, ngay, thoigian):
                QMessageBox.warning(self.txtIDDKPH,"Thông báo", "Giảng viên đã có lịch dạy vào thời gian này!")
                return

    # Kiểm tra lớp học đã có lịch vào thời gian đó chưa
        if database.check_Lop_Gio(ten_Lop, ngay, thoigian):
                QMessageBox.warning(self.txtIDDKPH,"Thông báo", "Lớp học đã có lịch vào thời gian này!")
                return

    # Thực hiện thêm đăng ký phòng học vào cơ sở dữ liệu
        if not database.add_Xeplich(ten_Phong, ten_Khoa, ten_Mon, ten_GV, ten_Lop, ngay, thoigian, tinhTrang):
                QMessageBox.warning(self.txtIDDKPH,"Thông báo", "ID lớp hoặc Tên lớp đã tồn tại!")
                self.txtIDLop.clear()
                self.txtIDTenLop.clear()
                return

    # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.txtIDDKPH,"Thông báo", "Đăng ký phòng học thành công!")

    def checkSession(self, Dialog):
        if 'username' not in self.session:
            QMessageBox.warning(Dialog, "Thông báo", "Vui lòng đăng nhập trước khi truy cập trang này!")
            Dialog.close() 
            self.openLoginWindow()
        else:
            Dialog.show() 

    def openLoginWindow(self):
        from Login import Ui_MainWindow
        self.loginWindow = QtWidgets.QMainWindow()
        self.ui_login = Ui_MainWindow()
        self.ui_login.setupUi(self.loginWindow)
        self.loginWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    session = {}  # Tạo một session rỗng
    ui = Ui_Dialog(session)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
