# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Face.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(978, 657)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/pukontu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(444, 486, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Start.sizePolicy().hasHeightForWidth())
        self.pushButton_Start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setTabletTracking(True)
        self.pushButton_Start.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Start.setAcceptDrops(False)
        self.pushButton_Start.setCheckable(False)
        self.pushButton_Start.setChecked(False)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.label_connected = QtWidgets.QLabel(self.centralwidget)
        self.label_connected.setGeometry(QtCore.QRect(214, 496, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_connected.sizePolicy().hasHeightForWidth())
        self.label_connected.setSizePolicy(sizePolicy)
        self.label_connected.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_connected.setFont(font)
        self.label_connected.setText("")
        self.label_connected.setObjectName("label_connected")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(278, 88, 341, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_hardness = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_hardness.setFont(font)
        self.label_hardness.setObjectName("label_hardness")
        self.gridLayout.addWidget(self.label_hardness, 5, 0, 1, 1)
        self.lineEdit_hardness = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hardness.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_hardness.setFont(font)
        self.lineEdit_hardness.setText("")
        self.lineEdit_hardness.setCursorPosition(0)
        self.lineEdit_hardness.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_hardness.setDragEnabled(False)
        self.lineEdit_hardness.setReadOnly(False)
        self.lineEdit_hardness.setClearButtonEnabled(False)
        self.lineEdit_hardness.setObjectName("lineEdit_hardness")
        self.gridLayout.addWidget(self.lineEdit_hardness, 5, 1, 1, 1)
        self.lineEdit_gluten = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_gluten.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_gluten.setFont(font)
        self.lineEdit_gluten.setText("")
        self.lineEdit_gluten.setCursorPosition(0)
        self.lineEdit_gluten.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_gluten.setDragEnabled(False)
        self.lineEdit_gluten.setReadOnly(False)
        self.lineEdit_gluten.setClearButtonEnabled(False)
        self.lineEdit_gluten.setObjectName("lineEdit_gluten")
        self.gridLayout.addWidget(self.lineEdit_gluten, 4, 1, 1, 1)
        self.lineEdit_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_number.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setText("")
        self.lineEdit_number.setCursorPosition(0)
        self.lineEdit_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number.setDragEnabled(False)
        self.lineEdit_number.setReadOnly(False)
        self.lineEdit_number.setClearButtonEnabled(False)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.gridLayout.addWidget(self.lineEdit_number, 6, 1, 1, 1)
        self.label_protein = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_protein.setFont(font)
        self.label_protein.setObjectName("label_protein")
        self.gridLayout.addWidget(self.label_protein, 3, 0, 1, 1)
        self.lineEdit_Statue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Statue.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Statue.setFont(font)
        self.lineEdit_Statue.setText("")
        self.lineEdit_Statue.setCursorPosition(0)
        self.lineEdit_Statue.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Statue.setDragEnabled(False)
        self.lineEdit_Statue.setReadOnly(False)
        self.lineEdit_Statue.setClearButtonEnabled(False)
        self.lineEdit_Statue.setObjectName("lineEdit_Statue")
        self.gridLayout.addWidget(self.lineEdit_Statue, 2, 1, 1, 1)
        self.label_density = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_density.setFont(font)
        self.label_density.setObjectName("label_density")
        self.gridLayout.addWidget(self.label_density, 1, 0, 1, 1)
        self.label_water = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_water.setFont(font)
        self.label_water.setObjectName("label_water")
        self.gridLayout.addWidget(self.label_water, 0, 0, 1, 1)
        self.label_gluten = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_gluten.setFont(font)
        self.label_gluten.setObjectName("label_gluten")
        self.gridLayout.addWidget(self.label_gluten, 4, 0, 1, 1)
        self.lineEdit_Water = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Water.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Water.setFont(font)
        self.lineEdit_Water.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_Water.setText("")
        self.lineEdit_Water.setCursorPosition(0)
        self.lineEdit_Water.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Water.setDragEnabled(False)
        self.lineEdit_Water.setReadOnly(False)
        self.lineEdit_Water.setClearButtonEnabled(False)
        self.lineEdit_Water.setObjectName("lineEdit_Water")
        self.gridLayout.addWidget(self.lineEdit_Water, 0, 1, 1, 1)
        self.label_starch = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_starch.setFont(font)
        self.label_starch.setObjectName("label_starch")
        self.gridLayout.addWidget(self.label_starch, 2, 0, 1, 1)
        self.label_number = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")
        self.gridLayout.addWidget(self.label_number, 6, 0, 1, 1)
        self.lineEdit_protein = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_protein.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_protein.setFont(font)
        self.lineEdit_protein.setText("")
        self.lineEdit_protein.setCursorPosition(0)
        self.lineEdit_protein.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_protein.setDragEnabled(False)
        self.lineEdit_protein.setReadOnly(False)
        self.lineEdit_protein.setClearButtonEnabled(False)
        self.lineEdit_protein.setObjectName("lineEdit_protein")
        self.gridLayout.addWidget(self.lineEdit_protein, 3, 1, 1, 1)
        self.lineEdit_density = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_density.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_density.setFont(font)
        self.lineEdit_density.setText("")
        self.lineEdit_density.setCursorPosition(0)
        self.lineEdit_density.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_density.setDragEnabled(False)
        self.lineEdit_density.setReadOnly(False)
        self.lineEdit_density.setClearButtonEnabled(False)
        self.lineEdit_density.setObjectName("lineEdit_density")
        self.gridLayout.addWidget(self.lineEdit_density, 1, 1, 1, 1)
        self.pushButton_updata = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_updata.setGeometry(QtCore.QRect(638, 288, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_updata.sizePolicy().hasHeightForWidth())
        self.pushButton_updata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_updata.setFont(font)
        self.pushButton_updata.setTabletTracking(True)
        self.pushButton_updata.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_updata.setAcceptDrops(False)
        self.pushButton_updata.setCheckable(False)
        self.pushButton_updata.setChecked(False)
        self.pushButton_updata.setObjectName("pushButton_updata")
        self.pushButton_press = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_press.setGeometry(QtCore.QRect(638, 358, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_press.sizePolicy().hasHeightForWidth())
        self.pushButton_press.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_press.setFont(font)
        self.pushButton_press.setTabletTracking(True)
        self.pushButton_press.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_press.setAcceptDrops(False)
        self.pushButton_press.setCheckable(False)
        self.pushButton_press.setChecked(False)
        self.pushButton_press.setObjectName("pushButton_press")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(638, 428, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setTabletTracking(True)
        self.pushButton_back.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_back.setAcceptDrops(False)
        self.pushButton_back.setCheckable(False)
        self.pushButton_back.setChecked(False)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_config = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_config.setGeometry(QtCore.QRect(640, 96, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_config.sizePolicy().hasHeightForWidth())
        self.pushButton_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_config.setFont(font)
        self.pushButton_config.setTabletTracking(True)
        self.pushButton_config.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_config.setAcceptDrops(False)
        self.pushButton_config.setCheckable(False)
        self.pushButton_config.setChecked(False)
        self.pushButton_config.setObjectName("pushButton_config")
        self.label_COM2_connected = QtWidgets.QLabel(self.centralwidget)
        self.label_COM2_connected.setGeometry(QtCore.QRect(617, 51, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_COM2_connected.sizePolicy().hasHeightForWidth())
        self.label_COM2_connected.setSizePolicy(sizePolicy)
        self.label_COM2_connected.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_COM2_connected.setFont(font)
        self.label_COM2_connected.setObjectName("label_COM2_connected")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(337, 46, 281, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_23.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.comboBox_Moto_COM = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Moto_COM.setFont(font)
        self.comboBox_Moto_COM.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox_Moto_COM.setCurrentText("COM2")
        self.comboBox_Moto_COM.setMaxVisibleItems(11)
        self.comboBox_Moto_COM.setObjectName("comboBox_Moto_COM")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(0, "COM2")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(2, "COM3")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(3, "COM4")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(4, "COM5")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(5, "COM6")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.setItemText(6, "COM7")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.comboBox_Moto_COM.addItem("")
        self.gridLayout_23.addWidget(self.comboBox_Moto_COM, 0, 1, 1, 1)
        self.label_COM_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_COM_3.setFont(font)
        self.label_COM_3.setObjectName("label_COM_3")
        self.gridLayout_23.addWidget(self.label_COM_3, 0, 0, 1, 1)
        self.pushButton_Start_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start_2.setGeometry(QtCore.QRect(277, 486, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Start_2.sizePolicy().hasHeightForWidth())
        self.pushButton_Start_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Start_2.setFont(font)
        self.pushButton_Start_2.setTabletTracking(True)
        self.pushButton_Start_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Start_2.setAcceptDrops(False)
        self.pushButton_Start_2.setCheckable(False)
        self.pushButton_Start_2.setChecked(False)
        self.pushButton_Start_2.setObjectName("pushButton_Start_2")
        self.label_density_com = QtWidgets.QLabel(self.centralwidget)
        self.label_density_com.setGeometry(QtCore.QRect(667, 156, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_density_com.setFont(font)
        self.label_density_com.setObjectName("label_density_com")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(627, 140, 72, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(610, 486, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Stop.sizePolicy().hasHeightForWidth())
        self.pushButton_Stop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.pushButton_breakdown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_breakdown.setGeometry(QtCore.QRect(640, 220, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_breakdown.sizePolicy().hasHeightForWidth())
        self.pushButton_breakdown.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_breakdown.setFont(font)
        self.pushButton_breakdown.setTabletTracking(True)
        self.pushButton_breakdown.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_breakdown.setAcceptDrops(False)
        self.pushButton_breakdown.setCheckable(False)
        self.pushButton_breakdown.setChecked(False)
        self.pushButton_breakdown.setObjectName("pushButton_breakdown")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Start.setText(_translate("MainWindow", "开始"))
        self.label_hardness.setText(_translate("MainWindow", "       硬   度 "))
        self.label_protein.setText(_translate("MainWindow", "       蛋   白"))
        self.label_density.setText(_translate("MainWindow", "       容   重"))
        self.label_water.setText(_translate("MainWindow", "       水    分"))
        self.label_gluten.setText(_translate("MainWindow", "    湿   面   筋"))
        self.label_starch.setText(_translate("MainWindow", "       淀   粉"))
        self.label_number.setText(_translate("MainWindow", "   样 品 编 号  "))
        self.pushButton_updata.setText(_translate("MainWindow", "上传"))
        self.pushButton_press.setText(_translate("MainWindow", "打印"))
        self.pushButton_back.setText(_translate("MainWindow", "返回"))
        self.pushButton_config.setText(_translate("MainWindow", "设置"))
        self.label_COM2_connected.setText(_translate("MainWindow", "    串口打开失败！"))
        self.comboBox_Moto_COM.setItemText(1, _translate("MainWindow", "COM1"))
        self.comboBox_Moto_COM.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_Moto_COM.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_Moto_COM.setItemText(9, _translate("MainWindow", "COM10"))
        self.comboBox_Moto_COM.setItemText(10, _translate("MainWindow", "COM11"))
        self.comboBox_Moto_COM.setItemText(11, _translate("MainWindow", "COM12"))
        self.comboBox_Moto_COM.setItemText(12, _translate("MainWindow", "COM13"))
        self.comboBox_Moto_COM.setItemText(13, _translate("MainWindow", "COM14"))
        self.comboBox_Moto_COM.setItemText(14, _translate("MainWindow", "COM15"))
        self.comboBox_Moto_COM.setItemText(15, _translate("MainWindow", "COM16"))
        self.comboBox_Moto_COM.setItemText(16, _translate("MainWindow", "COM17"))
        self.comboBox_Moto_COM.setItemText(17, _translate("MainWindow", "COM18"))
        self.comboBox_Moto_COM.setItemText(18, _translate("MainWindow", "COM19"))
        self.comboBox_Moto_COM.setItemText(19, _translate("MainWindow", "COM20"))
        self.comboBox_Moto_COM.setItemText(20, _translate("MainWindow", "COM21"))
        self.comboBox_Moto_COM.setItemText(21, _translate("MainWindow", "COM22"))
        self.comboBox_Moto_COM.setItemText(22, _translate("MainWindow", "COM23"))
        self.comboBox_Moto_COM.setItemText(23, _translate("MainWindow", "COM24"))
        self.comboBox_Moto_COM.setItemText(24, _translate("MainWindow", "COM25"))
        self.label_COM_3.setText(_translate("MainWindow", "电机串口选择"))
        self.pushButton_Start_2.setText(_translate("MainWindow", "背景"))
        self.label_density_com.setText(_translate("MainWindow", "未连接"))
        self.label.setText(_translate("MainWindow", "g"))
        self.pushButton_Stop.setText(_translate("MainWindow", "结束"))
        self.pushButton_breakdown.setText(_translate("MainWindow", "故障"))
        self.pushButton_breakdown.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
import Picture_rc