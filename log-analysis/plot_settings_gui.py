# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_settings_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 330)
        Form.setMinimumSize(QtCore.QSize(450, 330))
        Form.setMaximumSize(QtCore.QSize(450, 330))
        Form.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 14, 1, 1, 5)
        self.checkBox_rationing = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_rationing.setFont(font)
        self.checkBox_rationing.setObjectName("checkBox_rationing")
        self.gridLayout_4.addWidget(self.checkBox_rationing, 5, 1, 1, 4)
        self.checkBox_faults = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_faults.setFont(font)
        self.checkBox_faults.setObjectName("checkBox_faults")
        self.gridLayout_4.addWidget(self.checkBox_faults, 6, 1, 1, 4)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 10, 1, 1, 4)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 8, 1, 1, 5)
        self.comboBox_um = QtWidgets.QComboBox(Form)
        self.comboBox_um.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox_um.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_um.setFont(font)
        self.comboBox_um.setObjectName("comboBox_um")
        self.gridLayout_4.addWidget(self.comboBox_um, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(130, 0))
        self.label_2.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 15, 1, 1, 1)
        self.checkBox_set_koefs = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_set_koefs.setFont(font)
        self.checkBox_set_koefs.setObjectName("checkBox_set_koefs")
        self.gridLayout_4.addWidget(self.checkBox_set_koefs, 7, 1, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 3, 1, 1)
        self.pushButton_um1 = QtWidgets.QPushButton(Form)
        self.pushButton_um1.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_um1.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_um1.setFont(font)
        self.pushButton_um1.setObjectName("pushButton_um1")
        self.gridLayout_4.addWidget(self.pushButton_um1, 16, 1, 1, 5, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(45, 20))
        self.label.setMaximumSize(QtCore.QSize(45, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(75, 0))
        self.label_5.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dateTimeEdit_finish = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_finish.setMinimumSize(QtCore.QSize(130, 0))
        self.dateTimeEdit_finish.setMaximumSize(QtCore.QSize(130, 16777215))
        self.dateTimeEdit_finish.setObjectName("dateTimeEdit_finish")
        self.horizontalLayout_5.addWidget(self.dateTimeEdit_finish)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 12, 1, 1, 5)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 5)
        self.comboBox_marker = QtWidgets.QComboBox(Form)
        self.comboBox_marker.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_marker.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_marker.setFont(font)
        self.comboBox_marker.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_marker.setEditable(False)
        self.comboBox_marker.setObjectName("comboBox_marker")
        self.gridLayout_4.addWidget(self.comboBox_marker, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(55, 20))
        self.label_6.setMaximumSize(QtCore.QSize(55, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 4, 1, 1)
        self.checkBox_one_um1 = QtWidgets.QCheckBox(Form)
        self.checkBox_one_um1.setMinimumSize(QtCore.QSize(10, 0))
        self.checkBox_one_um1.setMaximumSize(QtCore.QSize(1000000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_one_um1.setFont(font)
        self.checkBox_one_um1.setObjectName("checkBox_one_um1")
        self.gridLayout_4.addWidget(self.checkBox_one_um1, 4, 1, 1, 4)
        self.comboBox_markersize = QtWidgets.QComboBox(Form)
        self.comboBox_markersize.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_markersize.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_markersize.setFont(font)
        self.comboBox_markersize.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_markersize.setEditable(False)
        self.comboBox_markersize.setObjectName("comboBox_markersize")
        self.gridLayout_4.addWidget(self.comboBox_markersize, 2, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 3, 1, 1, 5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(75, 0))
        self.label_4.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_start.setMinimumSize(QtCore.QSize(130, 0))
        self.dateTimeEdit_start.setMaximumSize(QtCore.QSize(130, 16777215))
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.horizontalLayout_4.addWidget(self.dateTimeEdit_start)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 11, 1, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 17, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.groupBox_um1 = QtWidgets.QGroupBox(Form)
        self.groupBox_um1.setMinimumSize(QtCore.QSize(163, 290))
        self.groupBox_um1.setMaximumSize(QtCore.QSize(163, 290))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_um1.setFont(font)
        self.groupBox_um1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_um1.setFlat(False)
        self.groupBox_um1.setCheckable(False)
        self.groupBox_um1.setObjectName("groupBox_um1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_um1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_k_Uips2 = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Uips2.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Uips2.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Uips2.setFont(font)
        self.lineEdit_k_Uips2.setText("")
        self.lineEdit_k_Uips2.setObjectName("lineEdit_k_Uips2")
        self.gridLayout_3.addWidget(self.lineEdit_k_Uips2, 11, 2, 1, 1)
        self.checkBox_um1_Ia = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Ia.setObjectName("checkBox_um1_Ia")
        self.gridLayout_3.addWidget(self.checkBox_um1_Ia, 4, 0, 1, 1)
        self.checkBox_um1_Un = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Un.setObjectName("checkBox_um1_Un")
        self.gridLayout_3.addWidget(self.checkBox_um1_Un, 5, 0, 1, 1)
        self.checkBox_um1_all = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_all.setChecked(False)
        self.checkBox_um1_all.setAutoExclusive(False)
        self.checkBox_um1_all.setObjectName("checkBox_um1_all")
        self.gridLayout_3.addWidget(self.checkBox_um1_all, 1, 0, 1, 3)
        self.lineEdit_k_Ikol = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Ikol.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Ikol.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Ikol.setFont(font)
        self.lineEdit_k_Ikol.setText("")
        self.lineEdit_k_Ikol.setObjectName("lineEdit_k_Ikol")
        self.gridLayout_3.addWidget(self.lineEdit_k_Ikol, 3, 2, 1, 1)
        self.lineEdit_k_Ia = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Ia.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Ia.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Ia.setFont(font)
        self.lineEdit_k_Ia.setText("")
        self.lineEdit_k_Ia.setObjectName("lineEdit_k_Ia")
        self.gridLayout_3.addWidget(self.lineEdit_k_Ia, 4, 2, 1, 1)
        self.lineEdit_k_Uvak = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Uvak.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Uvak.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Uvak.setFont(font)
        self.lineEdit_k_Uvak.setText("")
        self.lineEdit_k_Uvak.setObjectName("lineEdit_k_Uvak")
        self.gridLayout_3.addWidget(self.lineEdit_k_Uvak, 7, 2, 1, 1)
        self.checkBox_um1_Ivak = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Ivak.setObjectName("checkBox_um1_Ivak")
        self.gridLayout_3.addWidget(self.checkBox_um1_Ivak, 8, 0, 1, 1)
        self.checkBox_um1_Potr = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Potr.setObjectName("checkBox_um1_Potr")
        self.gridLayout_3.addWidget(self.checkBox_um1_Potr, 13, 0, 1, 1)
        self.checkBox_um1_Uips1 = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Uips1.setObjectName("checkBox_um1_Uips1")
        self.gridLayout_3.addWidget(self.checkBox_um1_Uips1, 10, 0, 1, 1)
        self.lineEdit_k_Uk = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Uk.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Uk.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Uk.setFont(font)
        self.lineEdit_k_Uk.setText("")
        self.lineEdit_k_Uk.setObjectName("lineEdit_k_Uk")
        self.gridLayout_3.addWidget(self.lineEdit_k_Uk, 2, 2, 1, 1)
        self.checkBox_um1_Uvak = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Uvak.setObjectName("checkBox_um1_Uvak")
        self.gridLayout_3.addWidget(self.checkBox_um1_Uvak, 7, 0, 1, 1)
        self.lineEdit_k_In = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_In.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_In.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_In.setFont(font)
        self.lineEdit_k_In.setText("")
        self.lineEdit_k_In.setObjectName("lineEdit_k_In")
        self.gridLayout_3.addWidget(self.lineEdit_k_In, 6, 2, 1, 1)
        self.lineEdit_k_Pvyh = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Pvyh.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Pvyh.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Pvyh.setFont(font)
        self.lineEdit_k_Pvyh.setText("")
        self.lineEdit_k_Pvyh.setObjectName("lineEdit_k_Pvyh")
        self.gridLayout_3.addWidget(self.lineEdit_k_Pvyh, 12, 2, 1, 1)
        self.lineEdit_k_Uips1 = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Uips1.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Uips1.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Uips1.setFont(font)
        self.lineEdit_k_Uips1.setText("")
        self.lineEdit_k_Uips1.setObjectName("lineEdit_k_Uips1")
        self.gridLayout_3.addWidget(self.lineEdit_k_Uips1, 10, 2, 1, 1)
        self.checkBox_um1_Uips2 = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Uips2.setObjectName("checkBox_um1_Uips2")
        self.gridLayout_3.addWidget(self.checkBox_um1_Uips2, 11, 0, 1, 1)
        self.checkBox_um1_In = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_In.setObjectName("checkBox_um1_In")
        self.gridLayout_3.addWidget(self.checkBox_um1_In, 6, 0, 1, 1)
        self.lineEdit_k_Uipup = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Uipup.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Uipup.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Uipup.setFont(font)
        self.lineEdit_k_Uipup.setText("")
        self.lineEdit_k_Uipup.setObjectName("lineEdit_k_Uipup")
        self.gridLayout_3.addWidget(self.lineEdit_k_Uipup, 9, 2, 1, 1)
        self.lineEdit_k_Potr = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Potr.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Potr.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Potr.setFont(font)
        self.lineEdit_k_Potr.setText("")
        self.lineEdit_k_Potr.setObjectName("lineEdit_k_Potr")
        self.gridLayout_3.addWidget(self.lineEdit_k_Potr, 13, 2, 1, 1)
        self.checkBox_um1_Pvyh = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Pvyh.setObjectName("checkBox_um1_Pvyh")
        self.gridLayout_3.addWidget(self.checkBox_um1_Pvyh, 12, 0, 1, 1)
        self.checkBox_um1_Uk = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Uk.setObjectName("checkBox_um1_Uk")
        self.gridLayout_3.addWidget(self.checkBox_um1_Uk, 2, 0, 1, 1)
        self.checkBox_um1_Ikol = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Ikol.setObjectName("checkBox_um1_Ikol")
        self.gridLayout_3.addWidget(self.checkBox_um1_Ikol, 3, 0, 1, 1)
        self.checkBox_um1_Uipup = QtWidgets.QCheckBox(self.groupBox_um1)
        self.checkBox_um1_Uipup.setObjectName("checkBox_um1_Uipup")
        self.gridLayout_3.addWidget(self.checkBox_um1_Uipup, 9, 0, 1, 1)
        self.lineEdit_k_Un = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Un.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Un.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Un.setFont(font)
        self.lineEdit_k_Un.setText("")
        self.lineEdit_k_Un.setObjectName("lineEdit_k_Un")
        self.gridLayout_3.addWidget(self.lineEdit_k_Un, 5, 2, 1, 1)
        self.lineEdit_k_Ivak = QtWidgets.QLineEdit(self.groupBox_um1)
        self.lineEdit_k_Ivak.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_k_Ivak.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_k_Ivak.setFont(font)
        self.lineEdit_k_Ivak.setText("")
        self.lineEdit_k_Ivak.setObjectName("lineEdit_k_Ivak")
        self.gridLayout_3.addWidget(self.lineEdit_k_Ivak, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_7.setMinimumSize(QtCore.QSize(10, 0))
        self.label_7.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_8.setMinimumSize(QtCore.QSize(10, 0))
        self.label_8.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_9.setMinimumSize(QtCore.QSize(10, 0))
        self.label_9.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_10.setMinimumSize(QtCore.QSize(10, 0))
        self.label_10.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_11.setMinimumSize(QtCore.QSize(10, 0))
        self.label_11.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 6, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_12.setMinimumSize(QtCore.QSize(10, 0))
        self.label_12.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 7, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_13.setMinimumSize(QtCore.QSize(10, 0))
        self.label_13.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 8, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_14.setMinimumSize(QtCore.QSize(10, 0))
        self.label_14.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 9, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_15.setMinimumSize(QtCore.QSize(10, 0))
        self.label_15.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 10, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_16.setMinimumSize(QtCore.QSize(10, 0))
        self.label_16.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 11, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_17.setMinimumSize(QtCore.QSize(10, 0))
        self.label_17.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 12, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_um1)
        self.label_18.setMinimumSize(QtCore.QSize(10, 0))
        self.label_18.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 13, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_um1, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        self.retranslateUi(Form)
        self.comboBox_marker.setCurrentIndex(-1)
        self.comboBox_markersize.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "???????????????????? ????????????????"))
        self.checkBox_rationing.setText(_translate("Form", "???????????????????????? ???? ??????????????????"))
        self.checkBox_faults.setText(_translate("Form", "???????????????????? ????????????"))
        self.label_3.setText(_translate("Form", "?????????????????? ????????????????:"))
        self.label_2.setText(_translate("Form", "?????????????????? ????????????????"))
        self.checkBox_set_koefs.setText(_translate("Form", "?????????????????? ????????????????????????"))
        self.pushButton_um1.setText(_translate("Form", "??????????????????"))
        self.label.setText(_translate("Form", "????????????"))
        self.label_5.setText(_translate("Form", "??????????????????:"))
        self.dateTimeEdit_finish.setDisplayFormat(_translate("Form", "dd.MM.yyyy HH:mm:ss"))
        self.label_6.setText(_translate("Form", "??????????????"))
        self.checkBox_one_um1.setText(_translate("Form", "?????????????? ???? ?????????? ??????????????"))
        self.label_4.setText(_translate("Form", "????????????:"))
        self.dateTimeEdit_start.setDisplayFormat(_translate("Form", "dd.MM.yyyy HH:mm:ss"))
        self.groupBox_um1.setTitle(_translate("Form", "??????????????????"))
        self.checkBox_um1_Ia.setText(_translate("Form", "Ia"))
        self.checkBox_um1_Un.setText(_translate("Form", "U??"))
        self.checkBox_um1_all.setText(_translate("Form", "?????????????? ??????"))
        self.checkBox_um1_Ivak.setText(_translate("Form", "I??????"))
        self.checkBox_um1_Potr.setText(_translate("Form", "P??????"))
        self.checkBox_um1_Uips1.setText(_translate("Form", "U??????1"))
        self.checkBox_um1_Uvak.setText(_translate("Form", "U??????"))
        self.checkBox_um1_Uips2.setText(_translate("Form", "U??????2"))
        self.checkBox_um1_In.setText(_translate("Form", "I??"))
        self.checkBox_um1_Pvyh.setText(_translate("Form", "P??????"))
        self.checkBox_um1_Uk.setText(_translate("Form", "U??"))
        self.checkBox_um1_Ikol.setText(_translate("Form", "I??????"))
        self.checkBox_um1_Uipup.setText(_translate("Form", "U????????"))
        self.label_7.setText(_translate("Form", "x"))
        self.label_8.setText(_translate("Form", "x"))
        self.label_9.setText(_translate("Form", "x"))
        self.label_10.setText(_translate("Form", "x"))
        self.label_11.setText(_translate("Form", "x"))
        self.label_12.setText(_translate("Form", "x"))
        self.label_13.setText(_translate("Form", "x"))
        self.label_14.setText(_translate("Form", "x"))
        self.label_15.setText(_translate("Form", "x"))
        self.label_16.setText(_translate("Form", "x"))
        self.label_17.setText(_translate("Form", "x"))
        self.label_18.setText(_translate("Form", "x"))
import resources_rc
