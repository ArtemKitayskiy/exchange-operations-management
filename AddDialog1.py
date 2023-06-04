# Form implementation generated from reading ui file 'AddDialog1.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddDialog1(object):
    def setupUi(self, AddDialog1):
        AddDialog1.setObjectName("AddDialog1")
        AddDialog1.resize(653, 190)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/dollar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddDialog1.setWindowIcon(icon)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(AddDialog1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(240, 150, 160, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_2.addWidget(self.button_ok)
        self.button_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_2.addWidget(self.button_cancel)
        self.horizontalLayoutWidget = QtWidgets.QWidget(AddDialog1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 551, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_torg_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_torg_date.setFont(font)
        self.label_torg_date.setObjectName("label_torg_date")
        self.horizontalLayout.addWidget(self.label_torg_date)
        self.label_regnum = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_regnum.setFont(font)
        self.label_regnum.setObjectName("label_regnum")
        self.horizontalLayout.addWidget(self.label_regnum)
        self.label_price = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.horizontalLayout.addWidget(self.label_price)
        self.label_gain_end = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gain_end.setFont(font)
        self.label_gain_end.setObjectName("label_gain_end")
        self.horizontalLayout.addWidget(self.label_gain_end)
        self.line_price = QtWidgets.QLineEdit(AddDialog1)
        self.line_price.setGeometry(QtCore.QRect(330, 100, 121, 20))
        self.line_price.setObjectName("line_price")
        self.line_gain_end = QtWidgets.QLineEdit(AddDialog1)
        self.line_gain_end.setGeometry(QtCore.QRect(470, 100, 131, 20))
        self.line_gain_end.setObjectName("line_gain_end")
        self.comboBox_regnum = QtWidgets.QComboBox(AddDialog1)
        self.comboBox_regnum.setGeometry(QtCore.QRect(190, 100, 121, 20))
        self.comboBox_regnum.setObjectName("comboBox_regnum")
        self.textBrowser = QtWidgets.QTextBrowser(AddDialog1)
        self.textBrowser.setGeometry(QtCore.QRect(50, 10, 256, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.date_button = QtWidgets.QPushButton(AddDialog1)
        self.date_button.setGeometry(QtCore.QRect(50, 120, 121, 23))
        self.date_button.setObjectName("date_button")
        self.line_date = QtWidgets.QLineEdit(AddDialog1)
        self.line_date.setEnabled(False)
        self.line_date.setGeometry(QtCore.QRect(50, 100, 121, 20))
        self.line_date.setObjectName("line_date")

        self.retranslateUi(AddDialog1)
        QtCore.QMetaObject.connectSlotsByName(AddDialog1)

    def retranslateUi(self, AddDialog1):
        _translate = QtCore.QCoreApplication.translate
        AddDialog1.setWindowTitle(_translate("AddDialog1", "Добавление записи в Activ"))
        self.button_ok.setText(_translate("AddDialog1", "Ок"))
        self.button_cancel.setText(_translate("AddDialog1", "Отмена"))
        self.label_torg_date.setText(_translate("AddDialog1", "Дата торгов"))
        self.label_regnum.setText(_translate("AddDialog1", "Код бумаги"))
        self.label_price.setText(_translate("AddDialog1", "Текущая цена"))
        self.label_gain_end.setText(_translate("AddDialog1", "Текущая доходность"))
        self.date_button.setText(_translate("AddDialog1", "Выбрать дату"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDialog1 = QtWidgets.QWidget()
    ui = Ui_AddDialog1()
    ui.setupUi(AddDialog1)
    AddDialog1.show()
    sys.exit(app.exec())
