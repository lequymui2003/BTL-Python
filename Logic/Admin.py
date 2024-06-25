import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QTreeWidget, QTreeWidgetItem, QLineEdit, QPushButton
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Database import database  # Import từ module database


class Ui_Dialog(object):
    def __init__(self, session):
        self.session = session

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
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(360, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtIDLop = QtWidgets.QLineEdit(parent=self.tab_2)
        self.txtIDLop.setGeometry(QtCore.QRect(90, 20, 181, 31))
        self.txtIDLop.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDLop.setAutoFillBackground(False)
        self.txtIDLop.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDLop.setObjectName("txtIDLop")
        self.txtIDTenLop = QtWidgets.QLineEdit(parent=self.tab_2)
        self.txtIDTenLop.setGeometry(QtCore.QRect(90, 70, 181, 31))
        self.txtIDTenLop.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDTenLop.setAutoFillBackground(False)
        self.txtIDTenLop.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDTenLop.setObjectName("txtIDTenLop")
        self.cbBoxIDKhoa_Lophoc = QtWidgets.QComboBox(parent=self.tab_2)
        self.cbBoxIDKhoa_Lophoc.setGeometry(QtCore.QRect(440, 20, 181, 31))
        self.cbBoxIDKhoa_Lophoc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxIDKhoa_Lophoc.setObjectName("cbBoxIDKhoa_Lophoc")
        self.treeWidgetLH = QtWidgets.QTreeWidget(parent=self.tab_2)
        self.treeWidgetLH.setGeometry(QtCore.QRect(0, 170, 1021, 321))
        self.treeWidgetLH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetLH.setObjectName("treeWidgetLH")
        self.txtSearchLophoc = QtWidgets.QLineEdit(parent=self.tab_2)
        self.txtSearchLophoc.setGeometry(QtCore.QRect(1050, 20, 171, 31))
        self.txtSearchLophoc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchLophoc.setObjectName("txtSearchLophoc")
        self.btSearchLophoc = QtWidgets.QPushButton(parent=self.tab_2)
        self.btSearchLophoc.setGeometry(QtCore.QRect(1080, 70, 121, 41))
        self.btSearchLophoc.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchLophoc.setObjectName("btSearchLophoc")
        self.btnAddLophoc = QtWidgets.QPushButton(parent=self.tab_2)
        self.btnAddLophoc.setGeometry(QtCore.QRect(1080, 170, 121, 41))
        self.btnAddLophoc.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddLophoc.setObjectName("btnAddLophoc")
        self.btnUpdateLH = QtWidgets.QPushButton(parent=self.tab_2)
        self.btnUpdateLH.setGeometry(QtCore.QRect(1080, 250, 121, 41))
        self.btnUpdateLH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdateLH.setObjectName("btnUpdateLH")
        self.btnDeleteLH = QtWidgets.QPushButton(parent=self.tab_2)
        self.btnDeleteLH.setGeometry(QtCore.QRect(1080, 330, 121, 41))
        self.btnDeleteLH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteLH.setObjectName("btnDeleteLH")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Load dữ liệu từ MySQL vào treeWidgetPH
        self.loadDataToTreeWidget()
        self.loadDataToTreeWidgetMH()
        self.loadDataToTreeWidgetLH()
        self.load_id_khoa()

        # gán sự kiện click bảng phòng học
        self.btnAddPH.clicked.connect(self.handleAddPH)
        self.btnUpdatePH.clicked.connect(self.handleUpdatePH)
        self.btnDeletePH.clicked.connect(self.handleDeletePH)
        self.btSearchPH.clicked.connect(self.handleSearch)
        self.txtSearchPH.textChanged.connect(self.handleInputChanged)
        self.treeWidgetPH.itemSelectionChanged.connect(self.handleSelectionChanged)
        

        #gán sự kiện cho bảng môn học
        self.btnAddMH.clicked.connect(self.handleAddMH)
        self.btnUpdateMH.clicked.connect(self.handleUpdateMH)
        self.btnDeleteMH.clicked.connect(self.handleDeleteMH)
        self.txtSearchMonhoc.textChanged.connect(self.handleInputChangedMH)
        self.btSearchMH.clicked.connect(self.handleSearchMH)
        self.treeWidgetMH.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng môn học
        self.btnAddLophoc.clicked.connect(self.handleAddLH)
        self.btnUpdateLH.clicked.connect(self.handleUpdateLH)
        self.btnDeleteLH.clicked.connect(self.handleDeleteLH)
        #self.txtSearchLophoc.textChanged.connect(self.handleInputChangedLH)
        #self.btSearchLophoc.clicked.connect(self.handleSearchLH)
        self.treeWidgetLH.itemSelectionChanged.connect(self.handleSelectionChanged)


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
        self.label_7.setText(_translate("Dialog", "ID Lớp:"))
        self.label_8.setText(_translate("Dialog", "Tên lớp:"))
        self.label_9.setText(_translate("Dialog", "ID Khoa:"))
        self.treeWidgetLH.headerItem().setText(0, _translate("Dialog", "ID Lớp"))
        self.treeWidgetLH.headerItem().setText(1, _translate("Dialog", "Tên Lớp"))
        self.treeWidgetLH.headerItem().setText(2, _translate("Dialog", "ID Khoa"))
        self.btSearchLophoc.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddLophoc.setText(_translate("Dialog", "Thêm"))
        self.btnUpdateLH.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteLH.setText(_translate("Dialog", "Xóa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Lớp học"))
# hàm load id khoa cho vào comboBox
    def load_id_khoa(self):
        id_khoa_list = database.get_all_id_khoa()

        self.cbBoxIDKhoa_Monhoc.addItems(id_khoa_list)
        self.cbBoxIDKhoa_Lophoc.addItems(id_khoa_list)
# thêm, sửa, xóa, tìm kiếm hiển thị bảng Phòng học
    def loadDataToTreeWidget(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_data()

        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetPH.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  # Cột 0 là ID Phòng
            parent_item.setText(1, row[1])       # Cột 1 là Tên Phòng

            self.treeWidgetPH.addTopLevelItem(parent_item)
    def handleAddPH(self):
        id_phong = self.txtIDPhong.text().strip()
        ten_phong = self.txtTenPhong.text().strip()

        if not id_phong or not ten_phong:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_phong(id_phong, ten_phong):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID phòng hoặc Tên phòng đã tồn tại!")
            self.txtIDPhong.clear()
            self.txtTenPhong.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm phòng học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeView()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtIDPhong.clear()
        self.txtTenPhong.clear()
        

        # Hàm xử lý khi chọn dòng trong treeViewPH
    def handleSelectionChanged(self):
        selected_items = self.treeWidgetPH.selectedItems()
        selected_itemsMH = self.treeWidgetMH.selectedItems()
        selected_itemsLH = self.treeWidgetLH.selectedItems()
        if selected_items:
                item = selected_items[0]
                id_phong = item.text(0)  # Lấy ID Phòng từ cột 0
                ten_phong = item.text(1)  # Lấy Tên Phòng từ cột 1

                # Hiển thị dữ liệu lên các ô input
                self.txtIDPhong.setText(id_phong)
                self.txtTenPhong.setText(ten_phong)
        if selected_itemsMH:
             item = selected_itemsMH[0]
             id_mon = item.text(0)
             ten_mon = item.text(1)
             so_tin_chi = item.text(2)
             id_Khoa = item.text(3)
             self.txtIDMon.setText(id_mon)
             self.txtTenMon.setText(ten_mon)
             self.txtSoTinChi.setText(so_tin_chi)
             self.cbBoxIDKhoa_Monhoc.setCurrentText(id_Khoa)
        if selected_itemsLH:
             item = selected_itemsLH[0]
             id_lop = item.text(0)
             ten_lop = item.text(1)
             id_Khoa = item.text(2)
             self.txtIDLop.setText(id_lop)
             self.txtIDTenLop.setText(ten_lop)
             self.cbBoxIDKhoa_Lophoc.setCurrentText(id_Khoa)
        # Hàm xử lý khi nhấn nút Sửa
    def handleUpdatePH(self):
        id_phong = self.txtIDPhong.text().strip()
        ten_phong = self.txtTenPhong.text().strip()

        if not id_phong or not ten_phong:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn phòng học để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_phong(id_phong, ten_phong):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật phòng học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidget()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtIDPhong.clear()
                self.txtTenPhong.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật phòng học thất bại!")
    def handleDeletePH(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetPH.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id_phong = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetPH, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa phòng có ID {id_phong}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
        # Gọi hàm xóa dữ liệu từ cơ sở dữ liệu
                if database.delete_phong(id_phong):
            # Xóa thành công, cập nhật lại treeWidgetPH
                        self.loadDataToTreeWidget()
                        QMessageBox.information(self.treeWidgetPH, 'Thông báo', 'Xóa phòng thành công!')
        else:
            QMessageBox.critical(self.treeWidgetPH, 'Lỗi', 'Không thể xóa phòng này!')
    def handleSearch(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_phong = self.txtSearchPH.text().strip()

        if ten_phong:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                phong_list = database.search_phong(ten_phong)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetPH.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for phong in phong_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetPH)
                        item.setText(0, str(phong[0]))  # Giả sử cột 0 là ID_Phong
                        item.setText(1, phong[1])  # Giả sử cột 1 là Ten_Phong

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên phòng học để tìm kiếm!")
    def handleInputChanged(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidget()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng môn học
    def loadDataToTreeWidgetMH(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_data_monhoc()

       
        self.treeWidgetMH.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))
            parent_item.setText(1, str(row[1]))  
            parent_item.setText(2, str(row[2])) 
            parent_item.setText(3, row[3]) 

            self.treeWidgetMH.addTopLevelItem(parent_item)
    def handleAddMH(self):
        id_mon = self.txtIDMon.text().strip()
        ten_mon = self.txtTenMon.text().strip()
        so_tin_chi = self.txtSoTinChi.text().strip()
        id_khoa = self.cbBoxIDKhoa_Monhoc.currentText().strip()

        if not id_mon or not ten_mon or not so_tin_chi or not id_khoa:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_monhoc(id_mon, ten_mon, so_tin_chi, id_khoa):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID môn hoặc Tên môn đã tồn tại!")
            self.txtIDMon.clear()
            self.txtTenMon.clear()
            self.txtSoTinChi.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm môn học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeWidgetMH()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtIDMon.clear()
        self.txtTenMon.clear()
        self.txtSoTinChi.clear()
    def handleUpdateMH(self):
        id_mon = self.txtIDMon.text().strip()
        ten_mon = self.txtTenMon.text().strip()
        so_tin_chi = self.txtSoTinChi.text().strip()
        id_khoa = self.cbBoxIDKhoa_Monhoc.currentText().strip()


        if not id_mon or not ten_mon or not so_tin_chi or not id_khoa:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn môn học để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_MH(id_mon, ten_mon, so_tin_chi, id_khoa):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật môn học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetMH()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtIDMon.clear()
                self.txtTenMon.clear()
                self.txtSoTinChi.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật môn học thất bại!")
    def handleDeleteMH(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetMH.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id_mon = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetMH, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa môn học có ID {id_mon}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
        # Gọi hàm xóa dữ liệu từ cơ sở dữ liệu
                if database.delete_MH(id_mon):
            # Xóa thành công, cập nhật lại treeWidgetPH
                        self.loadDataToTreeWidgetMH()
                        QMessageBox.information(self.treeWidgetMH, 'Thông báo', 'Xóa môn học thành công!')
        else:
            QMessageBox.critical(self.treeWidgetMH, 'Lỗi', 'Không thể xóa môn học này!')
    def handleSearchMH(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_MH = self.txtSearchMonhoc.text().strip()

        if ten_MH:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                mon_list = database.search_MH(ten_MH)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetMH.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for mon in mon_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetMH)
                        item.setText(0, str(mon[0]))  
                        item.setText(1, str(mon[1]))  
                        item.setText(2, str(mon[2])) 
                        item.setText(3, mon[3])  

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên phòng học để tìm kiếm!")
    def handleInputChangedMH(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetMH()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng lớp học
    def loadDataToTreeWidgetLH(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_dataLH()

        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetLH.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  
            parent_item.setText(1, str(row[1]))      
            parent_item.setText(2, row[2])          

            self.treeWidgetLH.addTopLevelItem(parent_item)
    def handleAddLH(self):
        id_lop = self.txtIDLop.text().strip()
        ten_lop = self.txtIDTenLop.text().strip()
        id_khoa = self.cbBoxIDKhoa_Lophoc.currentText().strip()

        if not id_lop or not ten_lop  or not id_khoa:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_LH(id_lop, ten_lop, id_khoa):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID lớp hoặc Tên lớp đã tồn tại!")
            self.txtIDLop.clear()
            self.txtIDTenLop.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm lớp học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeWidgetLH()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtIDLop.clear()
        self.txtIDTenLop.clear()
    def handleUpdateLH(self):
        id_lop = self.txtIDLop.text().strip()
        ten_lop = self.txtIDTenLop.text().strip()
        id_khoa = self.cbBoxIDKhoa_Lophoc.currentText().strip()


        if not id_lop or not ten_lop or not id_khoa:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn lớp học để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_LH(id_lop, ten_lop, id_khoa):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật lớp học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetLH()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtIDLop.clear()
                self.txtIDTenLop.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật phòng học thất bại!")
    def handleDeleteLH(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetLH.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id_Lop = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetLH, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa phòng có ID {id_Lop}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_LH(id_Lop):
           
                        self.loadDataToTreeWidgetLH()
                        QMessageBox.information(self.treeWidgetLH, 'Thông báo', 'Xóa lớp học thành công!')
        else:
            QMessageBox.critical(self.treeWidgetLH, 'Lỗi', 'Không thể xóa lớp học này!')



    def checkSession(self, Dialog):
        if 'username' not in self.session:
            QMessageBox.warning(Dialog, "Thông báo", "Vui lòng đăng nhập trước khi truy cập trang này!")
            Dialog.close()  # Đóng cửa sổ Admin
            self.openLoginWindow()
        else:
            Dialog.show()  # Hiển thị cửa sổ Admin nếu đã đăng nhập

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