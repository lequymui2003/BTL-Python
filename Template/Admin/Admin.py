# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1249, 582)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(980, 10, 131, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 1251, 531))
        self.tabWidget.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btnAddPH = QtWidgets.QPushButton(parent=self.tab_3)
        self.btnAddPH.setGeometry(QtCore.QRect(1040, 180, 121, 41))
        self.btnAddPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddPH.setObjectName("btnAddPH")
        self.btnUpdatePH = QtWidgets.QPushButton(parent=self.tab_3)
        self.btnUpdatePH.setGeometry(QtCore.QRect(1040, 260, 121, 41))
        self.btnUpdatePH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdatePH.setObjectName("btnUpdatePH")
        self.btnDeletePH = QtWidgets.QPushButton(parent=self.tab_3)
        self.btnDeletePH.setGeometry(QtCore.QRect(1040, 340, 121, 41))
        self.btnDeletePH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeletePH.setObjectName("btnDeletePH")
        self.txtSearchPH = QtWidgets.QLineEdit(parent=self.tab_3)
        self.txtSearchPH.setGeometry(QtCore.QRect(1020, 20, 171, 31))
        self.txtSearchPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchPH.setObjectName("txtSearchPH")
        self.btSearchPH = QtWidgets.QPushButton(parent=self.tab_3)
        self.btSearchPH.setGeometry(QtCore.QRect(1040, 70, 121, 41))
        self.btSearchPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchPH.setObjectName("btSearchPH")
        self.label = QtWidgets.QLabel(parent=self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtIDPhong = QtWidgets.QLineEdit(parent=self.tab_3)
        self.txtIDPhong.setGeometry(QtCore.QRect(100, 10, 181, 31))
        self.txtIDPhong.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDPhong.setAutoFillBackground(False)
        self.txtIDPhong.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDPhong.setObjectName("txtIDPhong")
        self.txtTenPhong = QtWidgets.QLineEdit(parent=self.tab_3)
        self.txtTenPhong.setGeometry(QtCore.QRect(100, 60, 181, 31))
        self.txtTenPhong.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenPhong.setObjectName("txtTenPhong")
        self.treeWidgetPH = QtWidgets.QTreeWidget(parent=self.tab_3)
        self.treeWidgetPH.setGeometry(QtCore.QRect(0, 180, 991, 321))
        self.treeWidgetPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetPH.setObjectName("treeWidgetPH")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab)
        self.label_5.setGeometry(QtCore.QRect(380, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.tab)
        self.label_6.setGeometry(QtCore.QRect(380, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtIDMon = QtWidgets.QLineEdit(parent=self.tab)
        self.txtIDMon.setGeometry(QtCore.QRect(90, 20, 181, 31))
        self.txtIDMon.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDMon.setAutoFillBackground(False)
        self.txtIDMon.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDMon.setObjectName("txtIDMon")
        self.txtTenMon = QtWidgets.QLineEdit(parent=self.tab)
        self.txtTenMon.setGeometry(QtCore.QRect(90, 70, 181, 31))
        self.txtTenMon.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtTenMon.setAutoFillBackground(False)
        self.txtTenMon.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenMon.setObjectName("txtTenMon")
        self.txtSoTinChi = QtWidgets.QLineEdit(parent=self.tab)
        self.txtSoTinChi.setGeometry(QtCore.QRect(470, 20, 181, 31))
        self.txtSoTinChi.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSoTinChi.setAutoFillBackground(False)
        self.txtSoTinChi.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSoTinChi.setObjectName("txtSoTinChi")
        self.txtSearchMonhoc = QtWidgets.QLineEdit(parent=self.tab)
        self.txtSearchMonhoc.setGeometry(QtCore.QRect(1040, 20, 171, 31))
        self.txtSearchMonhoc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchMonhoc.setObjectName("txtSearchMonhoc")
        self.btSearchMH = QtWidgets.QPushButton(parent=self.tab)
        self.btSearchMH.setGeometry(QtCore.QRect(1070, 70, 121, 41))
        self.btSearchMH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchMH.setObjectName("btSearchMH")
        self.btnAddMH = QtWidgets.QPushButton(parent=self.tab)
        self.btnAddMH.setGeometry(QtCore.QRect(1070, 180, 121, 41))
        self.btnAddMH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddMH.setObjectName("btnAddMH")
        self.btnUpdateMH = QtWidgets.QPushButton(parent=self.tab)
        self.btnUpdateMH.setGeometry(QtCore.QRect(1070, 260, 121, 41))
        self.btnUpdateMH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdateMH.setObjectName("btnUpdateMH")
        self.btnDeleteMH = QtWidgets.QPushButton(parent=self.tab)
        self.btnDeleteMH.setGeometry(QtCore.QRect(1070, 340, 121, 41))
        self.btnDeleteMH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteMH.setObjectName("btnDeleteMH")
        self.cbBoxIDKhoa_Monhoc = QtWidgets.QComboBox(parent=self.tab)
        self.cbBoxIDKhoa_Monhoc.setGeometry(QtCore.QRect(470, 70, 181, 31))
        self.cbBoxIDKhoa_Monhoc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxIDKhoa_Monhoc.setObjectName("cbBoxIDKhoa_Monhoc")
        self.treeWidgetMH = QtWidgets.QTreeWidget(parent=self.tab)
        self.treeWidgetMH.setGeometry(QtCore.QRect(0, 180, 1021, 321))
        self.treeWidgetMH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetMH.setObjectName("treeWidgetMH")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.commandLinkButton.setText(_translate("Dialog", "Đăng xuất"))
        self.btnAddPH.setText(_translate("Dialog", "Thêm"))
        self.btnUpdatePH.setText(_translate("Dialog", "Sửa"))
        self.btnDeletePH.setText(_translate("Dialog", "Xóa"))
        self.btSearchPH.setText(_translate("Dialog", "Tìm kiếm"))
        self.label.setText(_translate("Dialog", "ID Phòng:"))
        self.label_2.setText(_translate("Dialog", "Tên Phòng:"))
        self.treeWidgetPH.headerItem().setText(0, _translate("Dialog", "ID Phòng"))
        self.treeWidgetPH.headerItem().setText(1, _translate("Dialog", "Tên Phòng"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Phòng học"))
        self.label_3.setText(_translate("Dialog", "ID Môn:"))
        self.label_4.setText(_translate("Dialog", "Tên môn:"))
        self.label_5.setText(_translate("Dialog", "Số tín chỉ:"))
        self.label_6.setText(_translate("Dialog", "ID Khoa:"))
        self.btSearchMH.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddMH.setText(_translate("Dialog", "Thêm"))
        self.btnUpdateMH.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteMH.setText(_translate("Dialog", "Xóa"))
        self.treeWidgetMH.headerItem().setText(0, _translate("Dialog", "ID Môn"))
        self.treeWidgetMH.headerItem().setText(1, _translate("Dialog", "Tên Môn"))
        self.treeWidgetMH.headerItem().setText(2, _translate("Dialog", "Số tín chỉ"))
        self.treeWidgetMH.headerItem().setText(3, _translate("Dialog", "ID Khoa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Môn học"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())