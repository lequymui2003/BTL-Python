# Form implementation generated from reading ui file 'DKPhongHoc.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.cbBoxTinhTrang_DKPH.addItem("")
        self.btnDKPH = QtWidgets.QPushButton(parent=Dialog)
        self.btnDKPH.setGeometry(QtCore.QRect(260, 410, 151, 51))
        self.btnDKPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDKPH.setObjectName("btnDKPH")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
        self.cbBoxTinhTrang_DKPH.setItemText(1, _translate("Dialog", "Trống"))
        self.btnDKPH.setText(_translate("Dialog", "Đăng ký phòng học"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())