# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'C:\Users\yalda_soft\desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1 
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setToolTip("")
        self.tableWidget.setAccessibleName("")
        self.tableWidget.setAccessibleDescription("")
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        conn = sqlite3.connect("db.db")
        cur = conn.cursor()
        cur.execute("Select count(*) from adam")
        for row in cur:
            pass
        conn.close()
        doogh=row[0]
        if doogh > 100:
            doogh=100
        self.tableWidget.setRowCount(doogh)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ball_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        conn = sqlite3.connect("db.db")
        cur = conn.cursor()
        cur.execute("Select id from adam ORDER BY id DESC LIMIT 100")
        rows = cur.fetchall()
        xx = 0
        for row in rows:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(xx, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(xx, 1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(xx, 2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(xx, 3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(xx, 4, item)
            xx += 1
        conn.close()
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 410, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        self.lineEdit.textChanged['QString'].connect(self.aliu)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "جستجو"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ردیف"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "کد عاملیت"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "نام و نام خانوادگی"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "جنسیت"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "کد ملی"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        conn = sqlite3.connect("db.db")
        cur = conn.cursor()
        cur.execute("Select * from adam ORDER BY id DESC LIMIT 100")
        rows = cur.fetchall()
        xx = 0
        n=0
        for row in rows:
            n += 1
            item = self.tableWidget.item(xx, 0)
            item.setText(_translate("MainWindow", str(n)))
            bir = row[1]
            item = self.tableWidget.item(xx, 1)
            item.setText(_translate("MainWindow", bir))
            bir2 = row[2]
            bir = bir2 + ' ' + row[3]
            item = self.tableWidget.item(xx, 2)
            item.setText(_translate("MainWindow", bir))
            bir = row[4]
            item = self.tableWidget.item(xx, 3)
            item.setText(_translate("MainWindow", bir))
            bir = row[5]
            item = self.tableWidget.item(xx, 4)
            item.setText(_translate("MainWindow", bir))
            xx += 1
        conn.close()
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setToolTip(_translate("MainWindow", "مقدار درخواستی را جستجو کنید"))

    def aliu(self):
        text = self.lineEdit.text()
        if len(text)>1 or text=='':
            self.tableWidget.clearContents()
            conn = sqlite3.connect("db.db")
            cur = conn.cursor()
            cur.execute("Select id from adam ORDER BY id DESC LIMIT 100")
            rows = cur.fetchall()
            xx = 0
            for row in rows:
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(xx, 0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(xx, 1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(xx, 2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(xx, 3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(xx, 4, item)
                xx += 1
            conn.close()
            text='%'+text+'%'
            conn = sqlite3.connect("db.db")
            cur = conn.cursor()
            cur.execute("Select * from adam where code like '%s' or name like '%s'"
                        " or family like '%s' or sex like '%s' or meli like '%s' ORDER BY id DESC LIMIT 100" % (text,text,text,text,text))
            rows = cur.fetchall()
            xx = 0
            n = 0
            _translate = QtCore.QCoreApplication.translate
            for row in rows:
                n += 1
                item = self.tableWidget.item(xx, 0)
                item.setText(_translate("MainWindow", str(n)))
                bir = row[1]
                item = self.tableWidget.item(xx, 1)
                item.setText(_translate("MainWindow", bir))
                bir2 = row[2]
                bir = bir2 + ' ' + row[3]
                item = self.tableWidget.item(xx, 2)
                item.setText(_translate("MainWindow", bir))
                bir = row[4]
                item = self.tableWidget.item(xx, 3)
                item.setText(_translate("MainWindow", bir))
                bir = row[5]
                item = self.tableWidget.item(xx, 4)
                item.setText(_translate("MainWindow", bir))
                xx += 1
            conn.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
