# Form implementation generated from reading ui file 'Calendar.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(472, 302)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/dollar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Calendar.setWindowIcon(icon)
        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 30, 312, 183))
        self.calendarWidget.setSelectedDate(QtCore.QDate(1997, 1, 1))
        self.calendarWidget.setObjectName("calendarWidget")
        self.CalendarCheck = QtWidgets.QPushButton(Calendar)
        self.CalendarCheck.setGeometry(QtCore.QRect(190, 240, 101, 31))
        self.CalendarCheck.setObjectName("CalendarCheck")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Календарь"))
        self.CalendarCheck.setText(_translate("Calendar", "Подтвердить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calendar = QtWidgets.QWidget()
    ui = Ui_Calendar()
    ui.setupUi(Calendar)
    Calendar.show()
    sys.exit(app.exec())
