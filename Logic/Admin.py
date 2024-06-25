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
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1251, 531))
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
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(390, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtIDKhoa = QtWidgets.QLineEdit(parent=self.tab_4)
        self.txtIDKhoa.setGeometry(QtCore.QRect(90, 20, 181, 31))
        self.txtIDKhoa.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDKhoa.setAutoFillBackground(False)
        self.txtIDKhoa.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDKhoa.setObjectName("txtIDKhoa")
        self.txtTenKhoa = QtWidgets.QLineEdit(parent=self.tab_4)
        self.txtTenKhoa.setGeometry(QtCore.QRect(480, 20, 181, 31))
        self.txtTenKhoa.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtTenKhoa.setAutoFillBackground(False)
        self.txtTenKhoa.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenKhoa.setObjectName("txtTenKhoa")
        self.treeWidgetKhoa = QtWidgets.QTreeWidget(parent=self.tab_4)
        self.treeWidgetKhoa.setGeometry(QtCore.QRect(0, 170, 1021, 321))
        self.treeWidgetKhoa.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetKhoa.setObjectName("treeWidgetKhoa")
        self.txtSearchKhoa = QtWidgets.QLineEdit(parent=self.tab_4)
        self.txtSearchKhoa.setGeometry(QtCore.QRect(1050, 20, 171, 31))
        self.txtSearchKhoa.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchKhoa.setObjectName("txtSearchKhoa")
        self.btSearchKhoa = QtWidgets.QPushButton(parent=self.tab_4)
        self.btSearchKhoa.setGeometry(QtCore.QRect(1080, 70, 121, 41))
        self.btSearchKhoa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchKhoa.setObjectName("btSearchKhoa")
        self.btnAddKhoa = QtWidgets.QPushButton(parent=self.tab_4)
        self.btnAddKhoa.setGeometry(QtCore.QRect(1080, 170, 121, 41))
        self.btnAddKhoa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddKhoa.setObjectName("btnAddKhoa")
        self.btnUpdateKhoa = QtWidgets.QPushButton(parent=self.tab_4)
        self.btnUpdateKhoa.setGeometry(QtCore.QRect(1080, 250, 121, 41))
        self.btnUpdateKhoa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdateKhoa.setObjectName("btnUpdateKhoa")
        self.btnDeleteKhoa = QtWidgets.QPushButton(parent=self.tab_4)
        self.btnDeleteKhoa.setGeometry(QtCore.QRect(1080, 330, 121, 41))
        self.btnDeleteKhoa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteKhoa.setObjectName("btnDeleteKhoa")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(450, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(450, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.treeWidgetGV = QtWidgets.QTreeWidget(parent=self.tab_5)
        self.treeWidgetGV.setGeometry(QtCore.QRect(0, 170, 1021, 321))
        self.treeWidgetGV.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetGV.setObjectName("treeWidgetGV")
        self.txtIDGiangvien = QtWidgets.QLineEdit(parent=self.tab_5)
        self.txtIDGiangvien.setGeometry(QtCore.QRect(140, 20, 181, 31))
        self.txtIDGiangvien.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDGiangvien.setAutoFillBackground(False)
        self.txtIDGiangvien.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDGiangvien.setObjectName("txtIDGiangvien")
        self.txtTenGiangvien = QtWidgets.QLineEdit(parent=self.tab_5)
        self.txtTenGiangvien.setGeometry(QtCore.QRect(140, 70, 181, 31))
        self.txtTenGiangvien.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtTenGiangvien.setAutoFillBackground(False)
        self.txtTenGiangvien.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenGiangvien.setObjectName("txtTenGiangvien")
        self.txtSDT = QtWidgets.QLineEdit(parent=self.tab_5)
        self.txtSDT.setGeometry(QtCore.QRect(580, 20, 181, 31))
        self.txtSDT.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSDT.setAutoFillBackground(False)
        self.txtSDT.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSDT.setObjectName("txtSDT")
        self.cbBoxIDKhoa_Giangvien = QtWidgets.QComboBox(parent=self.tab_5)
        self.cbBoxIDKhoa_Giangvien.setGeometry(QtCore.QRect(580, 70, 181, 31))
        self.cbBoxIDKhoa_Giangvien.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxIDKhoa_Giangvien.setObjectName("cbBoxIDKhoa_Giangvien")
        self.txtSearchKhoa_2 = QtWidgets.QLineEdit(parent=self.tab_5)
        self.txtSearchKhoa_2.setGeometry(QtCore.QRect(1050, 20, 171, 31))
        self.txtSearchKhoa_2.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchKhoa_2.setObjectName("txtSearchKhoa_2")
        self.btSearchGV = QtWidgets.QPushButton(parent=self.tab_5)
        self.btSearchGV.setGeometry(QtCore.QRect(1080, 70, 121, 41))
        self.btSearchGV.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchGV.setObjectName("btSearchGV")
        self.btnAddGV = QtWidgets.QPushButton(parent=self.tab_5)
        self.btnAddGV.setGeometry(QtCore.QRect(1080, 170, 121, 41))
        self.btnAddGV.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddGV.setObjectName("btnAddGV")
        self.btnUpdateGV = QtWidgets.QPushButton(parent=self.tab_5)
        self.btnUpdateGV.setGeometry(QtCore.QRect(1080, 240, 121, 41))
        self.btnUpdateGV.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdateGV.setObjectName("btnUpdateGV")
        self.btnDeleteGV = QtWidgets.QPushButton(parent=self.tab_5)
        self.btnDeleteGV.setGeometry(QtCore.QRect(1080, 310, 121, 41))
        self.btnDeleteGV.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteGV.setObjectName("btnDeleteGV")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.treeWidgetCSVC = QtWidgets.QTreeWidget(parent=self.tab_6)
        self.treeWidgetCSVC.setGeometry(QtCore.QRect(0, 180, 1021, 321))
        self.treeWidgetCSVC.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetCSVC.setObjectName("treeWidgetCSVC")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(370, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(370, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_20.setGeometry(QtCore.QRect(680, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.tab_6)
        self.label_21.setGeometry(QtCore.QRect(680, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.cbBoxIDcosovatchat = QtWidgets.QComboBox(parent=self.tab_6)
        self.cbBoxIDcosovatchat.setGeometry(QtCore.QRect(160, 20, 181, 31))
        self.cbBoxIDcosovatchat.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxIDcosovatchat.setObjectName("cbBoxIDcosovatchat")
        self.txtTenCosovatchat = QtWidgets.QLineEdit(parent=self.tab_6)
        self.txtTenCosovatchat.setGeometry(QtCore.QRect(160, 70, 181, 31))
        self.txtTenCosovatchat.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtTenCosovatchat.setAutoFillBackground(False)
        self.txtTenCosovatchat.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenCosovatchat.setObjectName("txtTenCosovatchat")
        self.cbBoxIDPhong_csvc = QtWidgets.QComboBox(parent=self.tab_6)
        self.cbBoxIDPhong_csvc.setGeometry(QtCore.QRect(470, 20, 181, 31))
        self.cbBoxIDPhong_csvc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxIDPhong_csvc.setObjectName("cbBoxIDPhong_csvc")
        self.txtTenPhong_csvc = QtWidgets.QLineEdit(parent=self.tab_6)
        self.txtTenPhong_csvc.setGeometry(QtCore.QRect(470, 70, 181, 31))
        self.txtTenPhong_csvc.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtTenPhong_csvc.setAutoFillBackground(False)
        self.txtTenPhong_csvc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenPhong_csvc.setObjectName("txtTenPhong_csvc")
        self.txtSoLuongTot = QtWidgets.QLineEdit(parent=self.tab_6)
        self.txtSoLuongTot.setGeometry(QtCore.QRect(790, 20, 171, 31))
        self.txtSoLuongTot.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSoLuongTot.setAutoFillBackground(False)
        self.txtSoLuongTot.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSoLuongTot.setObjectName("txtSoLuongTot")
        self.txtSoLuongXau = QtWidgets.QLineEdit(parent=self.tab_6)
        self.txtSoLuongXau.setGeometry(QtCore.QRect(790, 70, 171, 31))
        self.txtSoLuongXau.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSoLuongXau.setAutoFillBackground(False)
        self.txtSoLuongXau.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSoLuongXau.setObjectName("txtSoLuongXau")
        self.txtSearchCsvc = QtWidgets.QLineEdit(parent=self.tab_6)
        self.txtSearchCsvc.setGeometry(QtCore.QRect(1050, 20, 171, 31))
        self.txtSearchCsvc.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchCsvc.setObjectName("txtSearchCsvc")
        self.btSearchCSVC = QtWidgets.QPushButton(parent=self.tab_6)
        self.btSearchCSVC.setGeometry(QtCore.QRect(1080, 70, 121, 41))
        self.btSearchCSVC.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchCSVC.setObjectName("btSearchCSVC")
        self.btnAddCSVC = QtWidgets.QPushButton(parent=self.tab_6)
        self.btnAddCSVC.setGeometry(QtCore.QRect(1080, 180, 121, 41))
        self.btnAddCSVC.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddCSVC.setObjectName("btnAddCSVC")
        self.btnUpdateCSVC = QtWidgets.QPushButton(parent=self.tab_6)
        self.btnUpdateCSVC.setGeometry(QtCore.QRect(1080, 260, 121, 41))
        self.btnUpdateCSVC.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdateCSVC.setObjectName("btnUpdateCSVC")
        self.btnDeleteCSVC = QtWidgets.QPushButton(parent=self.tab_6)
        self.btnDeleteCSVC.setGeometry(QtCore.QRect(1080, 340, 121, 41))
        self.btnDeleteCSVC.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteCSVC.setObjectName("btnDeleteCSVC")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.treeWidgetCSVC_2 = QtWidgets.QTreeWidget(parent=self.tab_7)
        self.treeWidgetCSVC_2.setGeometry(QtCore.QRect(0, 170, 1021, 321))
        self.treeWidgetCSVC_2.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetCSVC_2.setObjectName("treeWidgetCSVC_2")
        self.label_22 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_22.setGeometry(QtCore.QRect(10, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_24.setGeometry(QtCore.QRect(320, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_25.setGeometry(QtCore.QRect(320, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_26.setGeometry(QtCore.QRect(320, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_27.setGeometry(QtCore.QRect(650, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_28.setGeometry(QtCore.QRect(650, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_29.setGeometry(QtCore.QRect(650, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.cbBoxTenKhoa_xeplich = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTenKhoa_xeplich.setGeometry(QtCore.QRect(100, 80, 181, 31))
        self.cbBoxTenKhoa_xeplich.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenKhoa_xeplich.setObjectName("cbBoxTenKhoa_xeplich")
        self.cbBoxTenLop_xeplich = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTenLop_xeplich.setGeometry(QtCore.QRect(100, 130, 181, 31))
        self.cbBoxTenLop_xeplich.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenLop_xeplich.setObjectName("cbBoxTenLop_xeplich")
        self.cbBoxTenPhong_xeplich = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTenPhong_xeplich.setGeometry(QtCore.QRect(450, 130, 181, 31))
        self.cbBoxTenPhong_xeplich.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenPhong_xeplich.setObjectName("cbBoxTenPhong_xeplich")
        self.cbBoxTenGV_xeplich = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTenGV_xeplich.setGeometry(QtCore.QRect(450, 20, 181, 31))
        self.cbBoxTenGV_xeplich.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTenGV_xeplich.setObjectName("cbBoxTenGV_xeplich")
        self.cbBoxtenMon_xeplich = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxtenMon_xeplich.setGeometry(QtCore.QRect(450, 80, 181, 31))
        self.cbBoxtenMon_xeplich.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxtenMon_xeplich.setObjectName("cbBoxtenMon_xeplich")
        self.cbBoxTinhTrang = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTinhTrang.setGeometry(QtCore.QRect(740, 130, 181, 31))
        self.cbBoxTinhTrang.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTinhTrang.setObjectName("cbBoxTinhTrang")
        self.cbBoxTinhTrang.addItem("")
        self.cbBoxTinhTrang.addItem("")
        self.txtSearchCsvc_2 = QtWidgets.QLineEdit(parent=self.tab_7)
        self.txtSearchCsvc_2.setGeometry(QtCore.QRect(1050, 20, 171, 31))
        self.txtSearchCsvc_2.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchCsvc_2.setObjectName("txtSearchCsvc_2")
        self.btSearchxeplich = QtWidgets.QPushButton(parent=self.tab_7)
        self.btSearchxeplich.setGeometry(QtCore.QRect(1080, 70, 121, 41))
        self.btSearchxeplich.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btSearchxeplich.setObjectName("btSearchxeplich")
        self.btnAddxeplich = QtWidgets.QPushButton(parent=self.tab_7)
        self.btnAddxeplich.setGeometry(QtCore.QRect(1080, 170, 121, 41))
        self.btnAddxeplich.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnAddxeplich.setObjectName("btnAddxeplich")
        self.btnUpdatexeplich = QtWidgets.QPushButton(parent=self.tab_7)
        self.btnUpdatexeplich.setGeometry(QtCore.QRect(1080, 260, 121, 41))
        self.btnUpdatexeplich.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnUpdatexeplich.setObjectName("btnUpdatexeplich")
        self.btnDeleteXeplich = QtWidgets.QPushButton(parent=self.tab_7)
        self.btnDeleteXeplich.setGeometry(QtCore.QRect(1080, 340, 121, 41))
        self.btnDeleteXeplich.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteXeplich.setObjectName("btnDeleteXeplich")
        self.cbBoxTG = QtWidgets.QComboBox(parent=self.tab_7)
        self.cbBoxTG.setGeometry(QtCore.QRect(740, 80, 181, 31))
        self.cbBoxTG.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
"color: black; /* Màu chữ đen */\n"
"border: 1px solid #cccccc; /* Viền màu xám */")
        self.cbBoxTG.setObjectName("cbBoxTG")
        self.cbBoxTG.addItem("")
        self.cbBoxTG.addItem("")
        self.cbBoxTG.addItem("")
        self.cbBoxTG.addItem("")
        self.txtNgay = QtWidgets.QLineEdit(parent=self.tab_7)
        self.txtNgay.setGeometry(QtCore.QRect(730, 20, 191, 31))
        self.txtNgay.setObjectName("txtNgay")
        self.label_30 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_30.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.txtIDXeplich = QtWidgets.QLineEdit(parent=self.tab_7)
        self.txtIDXeplich.setGeometry(QtCore.QRect(100, 20, 181, 31))
        self.txtIDXeplich.setObjectName("txtIDXeplich")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.checkSession(Dialog)
        self.commandLinkButton.clicked.connect(self.confirm_logout)


        # Load dữ liệu từ MySQL vào treeWidgetPH
        self.loadDataToTreeWidget()
        self.loadDataToTreeWidgetMH()
        self.loadDataToTreeWidgetLH()
        self.loadDataToTreeWidgetKhoa()
        self.loadDataToTreeWidgetGV()
        self.loadDataToTreeWidgetCSVC()
        self.loadDataToTreeWidgetXeplich()
        self.load_id_khoa()
        self.load_id_csvc()
        self.load_id_Phonghoc()
        self.load_name_Khoa()
        self.load_name_GV()
        self.load_name_Lop()
        self.load_name_Mon()
        self.load_name_Phong()
        self.loadDataToTreeWidgetXeplich()

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
        self.txtSearchLophoc.textChanged.connect(self.handleInputChangedLH)
        self.btSearchLophoc.clicked.connect(self.handleSearchLH)
        self.treeWidgetLH.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng khoa
        self.btnAddKhoa.clicked.connect(self.handleAddKhoa)
        self.btnUpdateKhoa.clicked.connect(self.handleUpdateKhoa)
        self.btnDeleteKhoa.clicked.connect(self.handleDeleteKhoa)
        self.txtSearchKhoa.textChanged.connect(self.handleInputChangedKhoa)
        self.btSearchKhoa.clicked.connect(self.handleSearchKhoa)
        self.treeWidgetKhoa.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng khoa
        self.btnAddKhoa.clicked.connect(self.handleAddKhoa)
        self.btnUpdateKhoa.clicked.connect(self.handleUpdateKhoa)
        self.btnDeleteKhoa.clicked.connect(self.handleDeleteKhoa)
        self.txtSearchKhoa.textChanged.connect(self.handleInputChangedKhoa)
        self.btSearchKhoa.clicked.connect(self.handleSearchKhoa)
        self.treeWidgetKhoa.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng khoa
        self.btnAddGV.clicked.connect(self.handleAddGV)
        self.btnUpdateGV.clicked.connect(self.handleUpdateGV)
        self.btnDeleteGV.clicked.connect(self.handleDeleteGV)
        self.txtSearchKhoa_2.textChanged.connect(self.handleInputChangedGV)
        self.btSearchGV.clicked.connect(self.handleSearchGV)
        self.treeWidgetGV.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng cơ sở vật chất
        self.cbBoxIDcosovatchat.currentIndexChanged.connect(self.update_csv_name)
        self.cbBoxIDPhong_csvc.currentIndexChanged.connect(self.update_phong_name)
        self.btnAddCSVC.clicked.connect(self.handleAddCSVC)
        self.btnUpdateCSVC.clicked.connect(self.handleUpdateCSVC)
        self.btnDeleteCSVC.clicked.connect(self.handleDeleteCSVC)
        self.txtSearchCsvc.textChanged.connect(self.handleInputChangedCSVC)
        self.btSearchCSVC.clicked.connect(self.handleSearchCSVC)
        self.treeWidgetCSVC.itemSelectionChanged.connect(self.handleSelectionChanged)

        #gán sự kiện cho bảng xếp lịch
        self.btnAddxeplich.clicked.connect(self.handleAddXeplich)
        self.btnUpdatexeplich.clicked.connect(self.handleUpdateXeplich)
        self.btnDeleteXeplich.clicked.connect(self.handleDeleteXeplich)
        self.txtSearchCsvc_2.textChanged.connect(self.handleInputChangedXeplich)
        self.btSearchxeplich.clicked.connect(self.handleSearchXeplich)
        self.treeWidgetCSVC_2.itemSelectionChanged.connect(self.handleSelectionChanged)


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
        self.label_10.setText(_translate("Dialog", "ID Khoa:"))
        self.label_11.setText(_translate("Dialog", "Tên Khoa:"))
        self.treeWidgetKhoa.headerItem().setText(0, _translate("Dialog", "ID Khoa"))
        self.treeWidgetKhoa.headerItem().setText(1, _translate("Dialog", "Tên Khoa"))
        self.btSearchKhoa.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddKhoa.setText(_translate("Dialog", "Thêm"))
        self.btnUpdateKhoa.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteKhoa.setText(_translate("Dialog", "Xóa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Khoa"))
        self.label_12.setText(_translate("Dialog", "ID Giảng viên:"))
        self.label_13.setText(_translate("Dialog", "Tên giảng viên:"))
        self.label_14.setText(_translate("Dialog", "Số điện thoại:"))
        self.label_15.setText(_translate("Dialog", "ID Khoa:"))
        self.treeWidgetGV.headerItem().setText(0, _translate("Dialog", "ID Giảng viên"))
        self.treeWidgetGV.headerItem().setText(1, _translate("Dialog", "Tên giảng viên"))
        self.treeWidgetGV.headerItem().setText(2, _translate("Dialog", "Số điện thoại"))
        self.treeWidgetGV.headerItem().setText(3, _translate("Dialog", "ID Khoa"))
        self.btSearchGV.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddGV.setText(_translate("Dialog", "Thêm"))
        self.btnUpdateGV.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteGV.setText(_translate("Dialog", "Xóa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Giảng viên"))
        self.treeWidgetCSVC.headerItem().setText(0, _translate("Dialog", "STT"))
        self.treeWidgetCSVC.headerItem().setText(1, _translate("Dialog", "ID cơ sở vật chất"))
        self.treeWidgetCSVC.headerItem().setText(2, _translate("Dialog", "Tên cơ sở vật chất"))
        self.treeWidgetCSVC.headerItem().setText(3, _translate("Dialog", "ID phòng"))
        self.treeWidgetCSVC.headerItem().setText(4, _translate("Dialog", "Tên phòng"))
        self.treeWidgetCSVC.headerItem().setText(5, _translate("Dialog", "Số lượng tốt"))
        self.treeWidgetCSVC.headerItem().setText(6, _translate("Dialog", "Số lượng xấu"))
        self.label_16.setText(_translate("Dialog", "ID cơ sở vật chất:"))
        self.label_17.setText(_translate("Dialog", "Tên cơ sở vật chất:"))
        self.label_18.setText(_translate("Dialog", "ID phòng:"))
        self.label_19.setText(_translate("Dialog", "Tên phòng:"))
        self.label_20.setText(_translate("Dialog", "Số lượng tốt:"))
        self.label_21.setText(_translate("Dialog", "Số lượng xấu:"))
        self.btSearchCSVC.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddCSVC.setText(_translate("Dialog", "Thêm"))
        self.btnUpdateCSVC.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteCSVC.setText(_translate("Dialog", "Xóa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Cơ sở vật chất"))
        self.treeWidgetCSVC_2.headerItem().setText(0, _translate("Dialog", "ID"))
        self.treeWidgetCSVC_2.headerItem().setText(1, _translate("Dialog", "Tên khoa"))
        self.treeWidgetCSVC_2.headerItem().setText(2, _translate("Dialog", "Tên lớp"))
        self.treeWidgetCSVC_2.headerItem().setText(3, _translate("Dialog", "Tên giảng viên"))
        self.treeWidgetCSVC_2.headerItem().setText(4, _translate("Dialog", "Tên môn"))
        self.treeWidgetCSVC_2.headerItem().setText(5, _translate("Dialog", "Tên phòng"))
        self.treeWidgetCSVC_2.headerItem().setText(6, _translate("Dialog", "Ngày"))
        self.treeWidgetCSVC_2.headerItem().setText(7, _translate("Dialog", "Thời gian "))
        self.treeWidgetCSVC_2.headerItem().setText(8, _translate("Dialog", "Tình trạng"))
        self.label_22.setText(_translate("Dialog", "Tên khoa:"))
        self.label_23.setText(_translate("Dialog", "Tên Lớp:"))
        self.label_24.setText(_translate("Dialog", "Tên giảng viên:"))
        self.label_25.setText(_translate("Dialog", "Tên môn:"))
        self.label_26.setText(_translate("Dialog", "Tên phòng:"))
        self.label_27.setText(_translate("Dialog", "Ngày:"))
        self.label_28.setText(_translate("Dialog", "Thời gian:"))
        self.label_29.setText(_translate("Dialog", "Tình trạng:"))
        self.cbBoxTinhTrang.setItemText(0, _translate("Dialog", "Đã đăng ký"))
        self.cbBoxTinhTrang.setItemText(1, _translate("Dialog", "Trống"))
        self.btSearchxeplich.setText(_translate("Dialog", "Tìm kiếm"))
        self.btnAddxeplich.setText(_translate("Dialog", "Thêm"))
        self.btnUpdatexeplich.setText(_translate("Dialog", "Sửa"))
        self.btnDeleteXeplich.setText(_translate("Dialog", "Xóa"))
        self.cbBoxTG.setItemText(0, _translate("Dialog", "Ca 1 "))
        self.cbBoxTG.setItemText(1, _translate("Dialog", "Ca 2"))
        self.cbBoxTG.setItemText(2, _translate("Dialog", "Ca 3"))
        self.cbBoxTG.setItemText(3, _translate("Dialog", "Ca 4"))
        self.label_30.setText(_translate("Dialog", "ID:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Xếp lịch"))
    

    def load_id_khoa(self):
        id_khoa_list = database.get_all_id_khoa()
        self.cbBoxIDKhoa_Monhoc.addItems(id_khoa_list)
        self.cbBoxIDKhoa_Lophoc.addItems(id_khoa_list)
        self.cbBoxIDKhoa_Giangvien.addItems(id_khoa_list)
    def load_id_csvc(self):
        id_csvc_list = database.get_all_csvc()
        self.cbBoxIDcosovatchat.clear()  # Xóa các mục cũ
        for id, ten in id_csvc_list:
            self.cbBoxIDcosovatchat.addItem(id, ten)  # Thêm ID làm dữ liệu và tên làm hiển thị
    def update_csv_name(self):
        ten_csvc = self.cbBoxIDcosovatchat.currentData()
        self.txtTenCosovatchat.setText(ten_csvc)
    def load_id_Phonghoc(self):
        id_Phong_list = database.get_all_phonghoc()
        self.cbBoxIDPhong_csvc.clear()  # Xóa các mục cũ
        for idPhong, tenPhong in id_Phong_list:
            self.cbBoxIDPhong_csvc.addItem(idPhong, tenPhong)  # Thêm ID làm dữ liệu và tên làm hiển thị
    def update_phong_name(self):
        ten_phong = self.cbBoxIDPhong_csvc.currentData()
        self.txtTenPhong_csvc.setText(ten_phong)
    def load_name_Khoa(self):
        name_khoa_list = database.get_all_name_khoa()
        self.cbBoxTenKhoa_xeplich.addItems(name_khoa_list)
    def load_name_Lop(self):
        name_lop_list = database.get_all_name_lop()
        self.cbBoxTenLop_xeplich.addItems(name_lop_list)
    def load_name_Phong(self):
        name_Phong_list = database.get_all_name_Phong()
        self.cbBoxTenPhong_xeplich.addItems(name_Phong_list)
    def load_name_GV(self):
        name_GV_list = database.get_all_name_GV()
        self.cbBoxTenGV_xeplich.addItems(name_GV_list)
    def load_name_Mon(self):
        name_Mon_list = database.get_all_name_Mon()
        self.cbBoxtenMon_xeplich.addItems(name_Mon_list)
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
        selected_itemsKhoa = self.treeWidgetKhoa.selectedItems()
        selected_itemsGV = self.treeWidgetGV.selectedItems()
        selected_itemsCSVC = self.treeWidgetCSVC.selectedItems()
        selected_itemsXeplich = self.treeWidgetCSVC_2.selectedItems()
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
        if selected_itemsKhoa:
             item = selected_itemsKhoa[0]
             id_Khoa = item.text(0)
             ten_khoa = item.text(1)
             self.txtIDKhoa.setText(id_Khoa)
             self.txtTenKhoa.setText(ten_khoa)
        if selected_itemsGV:
             item = selected_itemsGV[0]
             id_GV = item.text(0)
             ten_GV = item.text(1)
             sdt = item.text(2)
             id_Khoa = item.text(3)
             self.txtIDGiangvien.setText(id_GV)
             self.txtTenGiangvien.setText(ten_GV)
             self.txtSDT.setText(sdt)
             self.cbBoxIDKhoa_Giangvien.setCurrentText(id_Khoa)
        if selected_itemsCSVC:
              item = selected_itemsCSVC[0]
              id_csvc = item.text(1)
              id_tencsvc = item.text(2)
              id_idphong = item.text(3)
              id_tenphong = item.text(4)
              id_slt = item.text(5)
              id_slx = item.text(6)
              self.cbBoxIDcosovatchat.setCurrentText(id_csvc)
              self.txtTenCosovatchat.setText(id_tencsvc)
              self.cbBoxIDPhong_csvc.setCurrentText(id_idphong)
              self.txtTenPhong_csvc.setText(id_tenphong)
              self.txtSoLuongTot.setText(id_slt)
              self.txtSoLuongXau.setText(id_slx)
        if selected_itemsXeplich:
              item = selected_itemsXeplich[0]
              id = item.text(0)
              id_Khoa = item.text(1)
              id_lop = item.text(2)
              id_GV = item.text(3)
              id_mon = item.text(4)
              id_phong = item.text(5)
              date = item.text(6)
              thoigian = item.text(7)
              tinhTrang = item.text(8)
              self.txtIDXeplich.setText(id)
              self.cbBoxTenKhoa_xeplich.setCurrentText(id_Khoa)
              self.cbBoxTenLop_xeplich.setCurrentText(id_lop)
              self.cbBoxTenGV_xeplich.setCurrentText(id_GV)
              self.cbBoxtenMon_xeplich.setCurrentText(id_mon)
              self.cbBoxTenPhong_xeplich.setCurrentText(id_phong)
              self.txtNgay.setText(date)
              self.cbBoxTG.setCurrentText(thoigian)
              self.cbBoxTinhTrang.setCurrentText(tinhTrang)
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
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên môn học để tìm kiếm!")
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
                f'Bạn có chắc chắn muốn xóa lớp có ID {id_Lop}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_LH(id_Lop):
           
                        self.loadDataToTreeWidgetLH()
                        QMessageBox.information(self.treeWidgetLH, 'Thông báo', 'Xóa lớp học thành công!')
        else:
            QMessageBox.critical(self.treeWidgetLH, 'Lỗi', 'Không thể xóa lớp học này!')
    def handleSearchLH(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_lop = self.txtSearchLophoc.text().strip()

        if ten_lop:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                lop_list = database.search_LH(ten_lop)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetLH.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for lop in lop_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetLH)
                        item.setText(0, str(lop[0]))  
                        item.setText(1, str(lop[1]))  
                        item.setText(2, lop[2]) 

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên lớp học để tìm kiếm!")
    def handleInputChangedLH(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetLH()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng khoa
    def loadDataToTreeWidgetKhoa(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_dataKhoa()

        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetKhoa.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  
            parent_item.setText(1, row[1])      

            self.treeWidgetKhoa.addTopLevelItem(parent_item)
    def handleAddKhoa(self):
        id_khoa = self.txtIDKhoa.text().strip()
        ten_Khoa = self.txtTenKhoa.text().strip()
        

        if not id_khoa or not ten_Khoa:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_Khoa(id_khoa, ten_Khoa):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID Khoa hoặc Tên khoa đã tồn tại!")
            self.txtIDKhoa.clear()
            self.txtTenKhoa.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm lớp học thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeWidgetKhoa()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtIDKhoa.clear()
        self.txtTenKhoa.clear()
    def handleUpdateKhoa(self):
        id_khoa = self.txtIDKhoa.text().strip()
        ten_khoa = self.txtTenKhoa.text().strip()


        if not ten_khoa or not id_khoa:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn khoa để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_Khoa(id_khoa, ten_khoa):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật khoa thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetKhoa()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtIDKhoa.clear()
                self.txtTenKhoa.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật khoa thất bại!")
    def handleDeleteKhoa(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetKhoa.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id_Khoa = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetKhoa, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa khoa có ID {id_Khoa}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_Khoa(id_Khoa):
           
                        self.loadDataToTreeWidgetKhoa()
                        QMessageBox.information(self.treeWidgetKhoa, 'Thông báo', 'Xóa khoa thành công!')
        else:
            QMessageBox.critical(self.treeWidgetKhoa, 'Lỗi', 'Không thể xóa lớp học này!')
    def handleSearchKhoa(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_Khoa = self.txtSearchKhoa.text().strip()

        if ten_Khoa:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                khoa_list = database.search_Khoa(ten_Khoa)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetKhoa.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for khoa in khoa_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetKhoa)
                        item.setText(0, str(khoa[0]))  
                        item.setText(1, khoa[1])  

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên khoa để tìm kiếm!")
    def handleInputChangedKhoa(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetKhoa()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng giảng viên
    def loadDataToTreeWidgetGV(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_dataGV()

        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetGV.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  
            parent_item.setText(1, str(row[1]))      
            parent_item.setText(2, str(row[2]))      
            parent_item.setText(3, row[3])      

            self.treeWidgetGV.addTopLevelItem(parent_item)
    def handleAddGV(self):
        id_GV = self.txtIDGiangvien.text().strip()
        ten_GV = self.txtTenGiangvien.text().strip()
        sdt = self.txtSDT.text().strip()
        id_Khoa = self.cbBoxIDKhoa_Giangvien.currentText().strip()
        

        if not id_GV or not ten_GV or not sdt or not id_Khoa:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_GV(id_GV, ten_GV, sdt, id_Khoa):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID Giảng viên hoặc Tên giảng viên đã tồn tại!")
            self.txtIDGiangvien.clear()
            self.txtTenGiangvien.clear()
            self.txtSDT.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm giảng viên thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeWidgetGV()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtIDGiangvien.clear()
        self.txtTenGiangvien.clear()
        self.txtSDT.clear()
    def handleUpdateGV(self):
        id_GV = self.txtIDGiangvien.text().strip()
        ten_GV = self.txtTenGiangvien.text().strip()
        sdt = self.txtSDT.text().strip()
        id_Khoa = self.cbBoxIDKhoa_Giangvien.currentText().strip()
        


        if not id_GV or not ten_GV or not sdt or not id_Khoa:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn giảng viên để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_GV(id_GV, ten_GV, sdt, id_Khoa):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật thông tin giảng viên thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetGV()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtIDGiangvien.clear()
                self.txtTenGiangvien.clear()
                self.txtSDT.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật khoa thất bại!")
    def handleDeleteGV(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetGV.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id_GV = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetGV, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa giảng viên có ID {id_GV}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_GV(id_GV):
           
                        self.loadDataToTreeWidgetGV()
                        QMessageBox.information(self.treeWidgetGV, 'Thông báo', 'Xóa giảng viên thành công!')
        else:
            QMessageBox.critical(self.treeWidgetGV, 'Lỗi', 'Không thể xóa giảng viên này!')
    def handleSearchGV(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_GV= self.txtSearchKhoa_2.text().strip()

        if ten_GV:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                giangvien_list = database.search_GV(ten_GV)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetGV.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for giangvien in giangvien_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetGV)
                        item.setText(0, str(giangvien[0]))  
                        item.setText(1, str(giangvien[1]))  
                        item.setText(2, str(giangvien[2]))  
                        item.setText(3, giangvien[3])  

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên giảng viên để tìm kiếm!")
    def handleInputChangedGV(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetGV()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng cơ sở vật chất
    def loadDataToTreeWidgetCSVC(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_dataCSVC()
        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetCSVC.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  
            parent_item.setText(1, str(row[1]))      
            parent_item.setText(2, str(row[2]))      
            parent_item.setText(3, str(row[3]))      
            parent_item.setText(4, str(row[4]))      
            parent_item.setText(5, str(row[5]))      
            parent_item.setText(6, str(row[6]))      

            self.treeWidgetCSVC.addTopLevelItem(parent_item)
    def handleAddCSVC(self):
        id_CSVC = self.cbBoxIDcosovatchat.currentText().strip()
        ten_CSVC = self.txtTenCosovatchat.text().strip()
        id_Phong = self.cbBoxIDPhong_csvc.currentText().strip()
        ten_Phong = self.txtTenPhong_csvc.text().strip()
        SoLuongTot = self.txtSoLuongTot.text().strip()
        SoLuongXau = self.txtSoLuongXau.text().strip()

        if not id_CSVC or not ten_CSVC or not id_Phong or not ten_Phong or not SoLuongTot or not SoLuongXau:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Thực hiện kiểm tra trước khi thêm phòng học vào cơ sở dữ liệu
        if not database.add_CSVC(id_CSVC, id_Phong, SoLuongTot, SoLuongXau):
            QMessageBox.warning(self.tab_3, "Thông báo", "ID cơ sở vật chất hoặc Tên cơ sở vật chất đã tồn tại!")
            self.txtTenCosovatchat.clear()
            self.txtTenPhong_csvc.clear()
            self.txtSoLuongTot.clear()
            self.txtSoLuongXau.clear()
            return
       
                # Nếu không có lỗi, hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm cơ sở vật chất thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
        self.loadDataToTreeWidgetCSVC()

            # Sau khi thêm thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
        self.txtTenCosovatchat.clear()
        self.txtTenPhong_csvc.clear()
        self.txtSoLuongTot.clear()
        self.txtSoLuongXau.clear()
    def handleUpdateCSVC(self):
        id_CSVC = self.cbBoxIDcosovatchat.currentText().strip()
        ten_CSVC = self.txtTenCosovatchat.text().strip()
        id_Phong = self.cbBoxIDPhong_csvc.currentText().strip()
        ten_Phong = self.txtTenPhong_csvc.text().strip()
        SoLuongTot = self.txtSoLuongTot.text().strip()
        SoLuongXau = self.txtSoLuongXau.text().strip()
        


        if not id_CSVC or not ten_CSVC or not id_Phong or not ten_Phong or not SoLuongTot or not SoLuongXau:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn cơ sở vật chất để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_CSVC(id_CSVC, id_Phong, SoLuongTot, SoLuongXau):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật thông tin cơ sở vật chất thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetCSVC()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtTenCosovatchat.clear()
                self.txtTenPhong_csvc.clear()
                self.txtSoLuongTot.clear()
                self.txtSoLuongXau.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật cơ sở vật chất thất bại!")
    def handleDeleteCSVC(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetCSVC.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        stt = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetCSVC, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa cơ sở vật chất có ID {stt}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_CSVC(stt):
           
                        self.loadDataToTreeWidgetCSVC()
                        QMessageBox.information(self.treeWidgetGV, 'Thông báo', 'Xóa cơ sở vật chất thành công!')
        else:
            QMessageBox.critical(self.treeWidgetGV, 'Lỗi', 'Không thể xóa cơ sở vật chất này!')
    def handleSearchCSVC(self):
        # Lấy nội dung từ ô input tìm kiếm
        ten_Phong= self.txtSearchCsvc.text().strip()

        if ten_Phong:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                ten_Phong_list = database.search_CSVC(ten_Phong)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetCSVC.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for tenphong in ten_Phong_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetCSVC)
                        item.setText(0, str(tenphong[0]))  
                        item.setText(1, str(tenphong[1]))  
                        item.setText(2, str(tenphong[2]))  
                        item.setText(3, str(tenphong[3]))  
                        item.setText(4, str(tenphong[4]))  
                        item.setText(5, str(tenphong[5]))  

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên giảng viên để tìm kiếm!")
    def handleInputChangedCSVC(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetCSVC()

# thêm, sửa, xóa, tìm kiếm hiển thị bảng xếp lịch
    def loadDataToTreeWidgetXeplich(self):
        # Lấy dữ liệu từ cơ sở dữ liệu
        data = database.load_dataXeplich()
        # Xóa dữ liệu cũ trong treeWidgetPH trước khi load lại
        self.treeWidgetCSVC_2.clear()

        for row in data:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, str(row[0]))  
            parent_item.setText(1, str(row[1]))      
            parent_item.setText(2, str(row[2]))      
            parent_item.setText(3, str(row[3]))      
            parent_item.setText(4, str(row[4]))      
            parent_item.setText(5, str(row[5]))      
            parent_item.setText(6, str(row[6]))      
            parent_item.setText(7, str(row[7]))         
            parent_item.setText(8, str(row[8]))         

            self.treeWidgetCSVC_2.addTopLevelItem(parent_item)
    def handleAddXeplich(self):
        # Lấy thông tin từ các widget
        ten_Phong = self.cbBoxTenPhong_xeplich.currentText().strip()
        ten_GV = self.cbBoxTenGV_xeplich.currentText().strip()
        ten_Khoa = self.cbBoxTenKhoa_xeplich.currentText().strip()
        ten_Mon = self.cbBoxtenMon_xeplich.currentText().strip()
        ten_Lop = self.cbBoxTenLop_xeplich.currentText().strip()
        ngay = self.txtNgay.text().strip()
        thoigian = self.cbBoxTG.currentText().strip()
        tinhTrang = self.cbBoxTinhTrang.currentText().strip()

        # Kiểm tra xem các thông tin cần thiết đã được nhập đủ hay chưa
        if not ten_Phong or not ten_GV or not ten_Lop or not ngay or not thoigian or not ten_Khoa or not ten_Mon or not tinhTrang:
            QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Nếu không có lỗi, thực hiện thêm lịch vào cơ sở dữ liệu
        database.add_Xeplich(ten_Phong, ten_Khoa, ten_Mon, ten_GV, ten_Lop, ngay, thoigian, tinhTrang)

        # Hiển thị thông báo thành công
        QMessageBox.information(self.tab_3, "Thông báo", "Thêm lịch thành công!")

        # Load lại dữ liệu trên treeViewPH
        self.loadDataToTreeWidgetXeplich()
    def handleUpdateXeplich(self):
        id = self.txtIDXeplich.text().strip()
        ten_Phong = self.cbBoxTenPhong_xeplich.currentText().strip()
        ten_GV = self.cbBoxTenGV_xeplich.currentText().strip()
        ten_Khoa = self.cbBoxTenKhoa_xeplich.currentText().strip()
        ten_Mon = self.cbBoxtenMon_xeplich.currentText().strip()
        ten_Lop = self.cbBoxTenLop_xeplich.currentText().strip()
        ngay = self.txtNgay.text().strip()
        thoigian = self.cbBoxTG.currentText().strip()
        tinhTrang = self.cbBoxTinhTrang.currentText().strip()
        


        if not ten_Phong or not ten_GV or not ten_Lop or not ngay or not thoigian or not ten_Khoa or not ten_Mon or not tinhTrang:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn cơ sở vật chất để sửa!")
                return

        # Thực hiện cập nhật phòng học vào cơ sở dữ liệu
        if database.update_Xeplich( id, ten_Phong, ten_Khoa, ten_Mon, ten_GV, ten_Lop, ngay, thoigian, tinhTrang):
                QMessageBox.information(self.tab_3, "Thông báo", "Cập nhật thông tin cơ sở vật chất thành công!")

                # Xóa dữ liệu cũ trên treeViewPH và load lại dữ liệu mới từ cơ sở dữ liệu
                self.loadDataToTreeWidgetXeplich()

                # Sau khi cập nhật thành công, clear các ô input để chuẩn bị nhập dữ liệu mới
                self.txtNgay.clear()
        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Cập nhật cơ sở vật chất thất bại!")
    def handleDeleteXeplich(self):
        # Lấy dòng được chọn trong treeWidgetPH
        selected_items = self.treeWidgetCSVC_2.selectedItems()

        if not selected_items:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng chọn dòng cần xóa!")
                return

    # Lấy ID Phòng từ dòng đầu tiên được chọn (giả sử chỉ chọn một dòng)
        id = selected_items[0].text(0)

    # Hiển thị hộp thoại xác nhận xóa
        reply = QMessageBox.question(self.treeWidgetCSVC, 'Xác nhận xóa', 
                f'Bạn có chắc chắn muốn xóa lịch học có ID {id}?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

                if database.delete_Xeplich(id):
           
                        self.loadDataToTreeWidgetXeplich()
                        QMessageBox.information(self.treeWidgetCSVC_2, 'Thông báo', 'Xóa lịch học thành công!')
        else:
            QMessageBox.critical(self.treeWidgetCSVC_2, 'Lỗi', 'Không thể xóa lịch học này này!')   
    def handleSearchXeplich(self):
        # Lấy nội dung từ ô input tìm kiếm
        tinhTrang= self.txtSearchCsvc_2.text().strip()

        if tinhTrang:
                # Gọi hàm search_phong từ module database để tìm kiếm phòng học theo tên
                tinhTrang_list = database.search_Xeplich(tinhTrang)

        # Xóa dữ liệu cũ trên treeViewPH
                self.treeWidgetCSVC_2.clear()

        # Thêm dữ liệu mới vào treeViewPH
                for tinhtrang in tinhTrang_list:
                        item = QtWidgets.QTreeWidgetItem(self.treeWidgetCSVC_2)
                        item.setText(0, str(tinhtrang[0]))  
                        item.setText(1, str(tinhtrang[1]))  
                        item.setText(2, str(tinhtrang[2]))  
                        item.setText(3, str(tinhtrang[3]))  
                        item.setText(4, str(tinhtrang[4]))  
                        item.setText(5, str(tinhtrang[5]))  
                        item.setText(6, str(tinhtrang[6]))  
                        item.setText(7, str(tinhtrang[7]))  
                        item.setText(8, str(tinhtrang[8]))  

        else:
                QMessageBox.warning(self.tab_3, "Thông báo", "Vui lòng nhập tên giảng viên để tìm kiếm!")
    def handleInputChangedXeplich(self, text):
        if not text:
        # Nếu ô input rỗng, load lại dữ liệu ban đầu
                self.loadDataToTreeWidgetXeplich()













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

    def confirm_logout(self):
        reply = QMessageBox.question(None, 'Xác nhận đăng xuất', 
                                     'Bạn có chắc chắn muốn đăng xuất?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.logout()

    def logout(self):
        # Xóa thông tin phiên đăng nhập
        self.session.clear()
        # Lưu trạng thái của cửa sổ hiện tại
        Dialog = QtWidgets.QApplication.activeWindow()
        if Dialog is not None:
            Dialog.close()
        # Mở cửa sổ đăng nhập
        self.openLoginWindow()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    session = {}  # Tạo một session rỗng
    ui = Ui_Dialog(session)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())