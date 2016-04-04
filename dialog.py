# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(278, 181)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelEn = QtWidgets.QLabel(Dialog)
        self.labelEn.setObjectName("labelEn")
        self.horizontalLayout.addWidget(self.labelEn)
        self.lineEn = QtWidgets.QLineEdit(Dialog)
        self.lineEn.setObjectName("lineEn")
        self.horizontalLayout.addWidget(self.lineEn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelFr = QtWidgets.QLabel(Dialog)
        self.labelFr.setObjectName("labelFr")
        self.horizontalLayout_2.addWidget(self.labelFr)
        self.lineFr = QtWidgets.QLineEdit(Dialog)
        self.lineFr.setObjectName("lineFr")
        self.horizontalLayout_2.addWidget(self.lineFr)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelEs = QtWidgets.QLabel(Dialog)
        self.labelEs.setObjectName("labelEs")
        self.horizontalLayout_3.addWidget(self.labelEs)
        self.lineEs = QtWidgets.QLineEdit(Dialog)
        self.lineEs.setObjectName("lineEs")
        self.horizontalLayout_3.addWidget(self.lineEs)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelGer = QtWidgets.QLabel(Dialog)
        self.labelGer.setObjectName("labelGer")
        self.horizontalLayout_4.addWidget(self.labelGer)
        self.lineGer = QtWidgets.QLineEdit(Dialog)
        self.lineGer.setObjectName("lineGer")
        self.horizontalLayout_4.addWidget(self.lineGer)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelJap = QtWidgets.QLabel(Dialog)
        self.labelJap.setObjectName("labelJap")
        self.horizontalLayout_5.addWidget(self.labelJap)
        self.lineJap = QtWidgets.QLineEdit(Dialog)
        self.lineJap.setObjectName("lineJap")
        self.horizontalLayout_5.addWidget(self.lineJap)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelEn.setText(_translate("Dialog", "   English : "))
        self.labelFr.setText(_translate("Dialog", "   French : "))
        self.labelEs.setText(_translate("Dialog", "  Spanish : "))
        self.labelGer.setText(_translate("Dialog", "  German : "))
        self.labelJap.setText(_translate("Dialog", "Japanese :"))


