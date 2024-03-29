# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(620, 608)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSearch.setMinimumSize(QtCore.QSize(75, 20))
        self.lineSearch.setInputMask("")
        self.lineSearch.setText("")
        self.lineSearch.setFrame(True)
        self.lineSearch.setObjectName("lineSearch")
        self.horizontalLayout.addWidget(self.lineSearch)
        self.buttonNew = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNew.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNew.setIcon(icon)
        self.buttonNew.setIconSize(QtCore.QSize(32, 32))
        self.buttonNew.setObjectName("buttonNew")
        self.horizontalLayout.addWidget(self.buttonNew)
        self.buttonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEdit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEdit.setIcon(icon1)
        self.buttonEdit.setIconSize(QtCore.QSize(32, 32))
        self.buttonEdit.setObjectName("buttonEdit")
        self.horizontalLayout.addWidget(self.buttonEdit)
        self.buttonQuiz = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuiz.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/quizz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonQuiz.setIcon(icon2)
        self.buttonQuiz.setIconSize(QtCore.QSize(32, 32))
        self.buttonQuiz.setObjectName("buttonQuiz")
        self.horizontalLayout.addWidget(self.buttonQuiz)
        self.buttonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRefresh.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRefresh.setIcon(icon3)
        self.buttonRefresh.setIconSize(QtCore.QSize(32, 32))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.horizontalLayout.addWidget(self.buttonRefresh)
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAdd.setIcon(icon4)
        self.buttonAdd.setIconSize(QtCore.QSize(32, 32))
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelete.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDelete.setIcon(icon5)
        self.buttonDelete.setIconSize(QtCore.QSize(32, 32))
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout.addWidget(self.buttonDelete)
        self.buttonImport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImport.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonImport.setIcon(icon6)
        self.buttonImport.setIconSize(QtCore.QSize(32, 32))
        self.buttonImport.setObjectName("buttonImport")
        self.horizontalLayout.addWidget(self.buttonImport)
        self.buttonExport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExport.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonExport.setIcon(icon7)
        self.buttonExport.setIconSize(QtCore.QSize(32, 32))
        self.buttonExport.setObjectName("buttonExport")
        self.horizontalLayout.addWidget(self.buttonExport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/uk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon8)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/fra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon9)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/esp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon10)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/ger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon11)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/jap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon12)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "pyProject"))
        self.lineSearch.setToolTip(_translate("mainWindow", "Search..."))
        self.lineSearch.setStatusTip(_translate("mainWindow", "Type to search through directory."))
        self.lineSearch.setPlaceholderText(_translate("mainWindow", "Search..."))
        self.buttonNew.setToolTip(_translate("mainWindow", "New"))
        self.buttonNew.setStatusTip(_translate("mainWindow", "Click to create a new directory."))
        self.buttonEdit.setToolTip(_translate("mainWindow", "Edit"))
        self.buttonEdit.setStatusTip(_translate("mainWindow", "Click to edit a row."))
        self.buttonQuiz.setToolTip(_translate("mainWindow", "Quiz"))
        self.buttonQuiz.setStatusTip(_translate("mainWindow", "Click to test your knowledge."))
        self.buttonRefresh.setToolTip(_translate("mainWindow", "Refresh"))
        self.buttonRefresh.setStatusTip(_translate("mainWindow", "Click to refresh the of view current directory."))
        self.buttonAdd.setToolTip(_translate("mainWindow", "Add"))
        self.buttonAdd.setStatusTip(_translate("mainWindow", "Click to add a row."))
        self.buttonDelete.setToolTip(_translate("mainWindow", "Delete"))
        self.buttonDelete.setStatusTip(_translate("mainWindow", "Click to delete a row."))
        self.buttonImport.setToolTip(_translate("mainWindow", "Open"))
        self.buttonImport.setStatusTip(_translate("mainWindow", "Click to open a file."))
        self.buttonExport.setToolTip(_translate("mainWindow", "Save"))
        self.buttonExport.setStatusTip(_translate("mainWindow", "Click to save current file."))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "English"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "French"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Spanish"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "German"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Japanese"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

