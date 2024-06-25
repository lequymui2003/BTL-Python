from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QTreeWidget, QTreeWidgetItem, QLineEdit, QPushButton
from Database import database  # Import từ module database

class Ui_Dialog(object):
    def __init__(self, session):
        self.session = session

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1249, 582)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(980, 10, 131, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 1251, 531))
        self.tabWidget.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
                                     "color: black; /* Màu chữ đen */\n"
                                     "border: 1px solid #cccccc; /* Viền màu xám */")
        self.tabWidget.setObjectName("tabWidget")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.btnAddPH = QtWidgets.QPushButton(self.tab_3)
        self.btnAddPH.setGeometry(QtCore.QRect(1040, 180, 121, 41))
        self.btnAddPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                     "color: rgb(255, 255, 255);")
        self.btnAddPH.setObjectName("btnAddPH")

        self.btnUpdatePH = QtWidgets.QPushButton(self.tab_3)
        self.btnUpdatePH.setGeometry(QtCore.QRect(1040, 260, 121, 41))
        self.btnUpdatePH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.btnUpdatePH.setObjectName("btnUpdatePH")

        self.btnDeletePH = QtWidgets.QPushButton(self.tab_3)
        self.btnDeletePH.setGeometry(QtCore.QRect(1040, 340, 121, 41))
        self.btnDeletePH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.btnDeletePH.setObjectName("btnDeletePH")

        self.txtSearchPH = QtWidgets.QLineEdit(self.tab_3)
        self.txtSearchPH.setGeometry(QtCore.QRect(1020, 20, 171, 31))
        self.txtSearchPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
                                       "color: black; /* Màu chữ đen */\n"
                                       "border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtSearchPH.setObjectName("txtSearchPH")

        self.btSearchPH = QtWidgets.QPushButton(self.tab_3)
        self.btSearchPH.setGeometry(QtCore.QRect(1040, 70, 121, 41))
        self.btSearchPH.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                      "color: rgb(255, 255, 255);")
        self.btSearchPH.setObjectName("btSearchPH")

        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.txtIDPhong = QtWidgets.QLineEdit(self.tab_3)
        self.txtIDPhong.setGeometry(QtCore.QRect(100, 10, 181, 31))
        self.txtIDPhong.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtIDPhong.setAutoFillBackground(False)
        self.txtIDPhong.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
                                      "color: black; /* Màu chữ đen */\n"
                                      "border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtIDPhong.setObjectName("txtIDPhong")

        self.txtTenPhong = QtWidgets.QLineEdit(self.tab_3)
        self.txtTenPhong.setGeometry(QtCore.QRect(100, 60, 181, 31))
        self.txtTenPhong.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
                                       "color: black; /* Màu chữ đen */\n"
                                       "border: 1px solid #cccccc; /* Viền màu xám */")
        self.txtTenPhong.setObjectName("txtTenPhong")

        self.treeWidgetPH = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidgetPH.setGeometry(QtCore.QRect(0, 180, 981, 311))
        self.treeWidgetPH.setStyleSheet("background-color: #f0f0f0; /* Màu nền xám nhạt */\n"
                                         "color: black; /* Màu chữ đen */\n"
                                         "border: 1px solid #cccccc; /* Viền màu xám */")
        self.treeWidgetPH.setHeaderLabels(["ID Phòng", "Tên Phòng"])
        self.treeWidgetPH.setAllColumnsShowFocus(True)
        self.treeWidgetPH.setObjectName("treeWidgetPH")

        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Load dữ liệu từ MySQL vào treeWidgetPH
        self.loadDataToTreeWidget()

        # Kết nối sự kiện click nút Thêm
        self.btnAddPH.clicked.connect(self.handleAddPH)

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Phòng học"))

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