import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import random
import string
import hashlib  # Import thư viện để sử dụng băm
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Database import database

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(791, 591)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(190, 110, 391, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.txtEmail.setGeometry(QtCore.QRect(10, 90, 361, 31))
        self.txtEmail.setObjectName("txtEmail")
        self.txtNewMK = QtWidgets.QLabel(self.groupBox)
        self.txtNewMK.setGeometry(QtCore.QRect(10, 140, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txtNewMK.setFont(font)
        self.txtNewMK.setObjectName("txtNewMK")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect the button to the function that handles its click event
        self.pushButton.clicked.connect(self.generate_random_password)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Quên mật khẩu"))
        self.label.setText(_translate("Dialog", "Email:"))
        self.pushButton.setText(_translate("Dialog", "Xác nhận"))

    def generate_random_password(self):
        email = self.txtEmail.text().strip()
        if email:
            # Generate a random password of 5 characters including letters and digits
            random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            self.txtNewMK.setText(random_password)
            
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(random_password.encode()).hexdigest()
            
            # Update password in MySQL database
            connection = database.create_connection()
            if connection:
                try:
                    cursor = connection.cursor()
                    # Update the password in the database for the given email
                    update_query = "UPDATE users SET password = %s WHERE email = %s"
                    cursor.execute(update_query, (hashed_password, email))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    print("Password updated successfully in database.")
                except database.Error as error:
                    print(f"Error updating password: {error}")
            else:
                print("Failed to connect to database.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
