# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialportform.ui'
#
# Created: Fri Apr 03 13:18:26 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import serialportedittext
import json
from serialport import registry
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

X_START = 10
COMBO_WIDTH = 130
COMBO_START = 100
LABLE_WIDTH = 80

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial

class Ui_SerialPortWindow(object):
    def setupUi(self, SerialPortWindow):
        self.reg = registry.Registry()
        SerialPortWindow.setObjectName(_fromUtf8("SerialPortWindow"))
        SerialPortWindow.resize(850, 700)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SerialPortWindow.sizePolicy().hasHeightForWidth())
        SerialPortWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(SerialPortWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(X_START, 10, 240, 350))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.label_email = QtGui.QLabel(self.groupBox)
        self.label_email.setGeometry(QtCore.QRect(X_START, 30, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_email.setObjectName(_fromUtf8("label_email"))

        self.textEditEmail = QtGui.QTextEdit(self.groupBox)
        self.textEditEmail.setGeometry(QtCore.QRect(COMBO_START, 30, COMBO_WIDTH, 21))
        self.textEditEmail.setObjectName(_fromUtf8("textEditUsername"))

        self.label_username = QtGui.QLabel(self.groupBox)
        self.label_username.setGeometry(QtCore.QRect(X_START, 60, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName(_fromUtf8("label_username"))

        self.textEditUsername = QtGui.QTextEdit(self.groupBox)
        self.textEditUsername.setGeometry(QtCore.QRect(COMBO_START, 60, COMBO_WIDTH, 21))
        self.textEditUsername.setObjectName(_fromUtf8("textEditUsername"))

        self.label_password = QtGui.QLabel(self.groupBox)
        self.label_password.setGeometry(QtCore.QRect(X_START, 90, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName(_fromUtf8("label_password"))

        self.textEditPassword = QtGui.QLineEdit(self.groupBox)
        self.textEditPassword.setGeometry(QtCore.QRect(COMBO_START, 90, COMBO_WIDTH, 21))
        self.textEditPassword.setObjectName(_fromUtf8("textEditPassword"))
        self.textEditPassword.setEchoMode(QtGui.QLineEdit.Password)

        self.comboBoxPort = QtGui.QComboBox(self.groupBox)
        self.comboBoxPort.setGeometry(QtCore.QRect(COMBO_START, 120, COMBO_WIDTH, 21))
        self.comboBoxPort.setObjectName(_fromUtf8("comboBoxPort"))

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(X_START, 120, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))


        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(X_START, 150, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.comboBoxBaud = QtGui.QComboBox(self.groupBox)
        self.comboBoxBaud.setGeometry(QtCore.QRect(COMBO_START, 150, COMBO_WIDTH, 21))
        self.comboBoxBaud.setObjectName(_fromUtf8("comboBoxBaud"))

        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(X_START, 180, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.comboBoxCheckSum = QtGui.QComboBox(self.groupBox)
        self.comboBoxCheckSum.setGeometry(QtCore.QRect(COMBO_START, 180, COMBO_WIDTH, 21))

        self.comboBoxCheckSum.setObjectName(_fromUtf8("comboBoxCheckSum"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(X_START, 210, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBoxBits = QtGui.QComboBox(self.groupBox)
        self.comboBoxBits.setGeometry(QtCore.QRect(COMBO_START, 210, COMBO_WIDTH, 21))
        self.comboBoxBits.setObjectName(_fromUtf8("comboBoxBits"))

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(X_START, 240, LABLE_WIDTH, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.comboBoxStopBits = QtGui.QComboBox(self.groupBox)
        self.comboBoxStopBits.setGeometry(QtCore.QRect(COMBO_START, 240, COMBO_WIDTH, 21))
        self.comboBoxStopBits.setObjectName(_fromUtf8("comboBoxStopBits"))

        self.pushButtonOpenSerial = QtGui.QPushButton(self.groupBox)
        self.pushButtonOpenSerial.setGeometry(QtCore.QRect(X_START, 320, 220, 21))
        self.pushButtonOpenSerial.setObjectName(_fromUtf8("pushButtonOpenSerial"))
        self.textEditReceived = QtGui.QTextEdit(self.centralwidget)

        self.textEditReceived.setGeometry(QtCore.QRect(260, 50, 551, 271))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditReceived.sizePolicy().hasHeightForWidth())
        self.textEditReceived.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditReceived.setFont(font)
        self.textEditReceived.setReadOnly(True)
        self.textEditReceived.setObjectName(_fromUtf8("textEditReceived"))

        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(X_START, 370, 240, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.checkBoxSaveAsFile = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxSaveAsFile.setGeometry(QtCore.QRect(X_START, 20, 91, 17))
        self.checkBoxSaveAsFile.setObjectName(_fromUtf8("checkBoxSaveAsFile"))
        self.checkBoxNewLine = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxNewLine.setGeometry(QtCore.QRect(X_START, 40, 101, 17))
        self.checkBoxNewLine.setObjectName(_fromUtf8("checkBoxNewLine"))
        self.checkBoxDisplayHex = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxDisplayHex.setGeometry(QtCore.QRect(X_START, 60, 101, 17))
        self.checkBoxDisplayHex.setObjectName(_fromUtf8("checkBoxDisplayHex"))
        self.checkBoxStopReceive = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxStopReceive.setGeometry(QtCore.QRect(X_START, 80, 101, 17))
        self.checkBoxStopReceive.setObjectName(_fromUtf8("checkBoxStopReceive"))
        self.pushButtonOpenRecvFile = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonOpenRecvFile.setGeometry(QtCore.QRect(130, 20, 100, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButtonOpenRecvFile.setFont(font)
        self.pushButtonOpenRecvFile.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonOpenRecvFile.setFlat(True)
        self.pushButtonOpenRecvFile.setObjectName(_fromUtf8("pushButtonOpenRecvFile"))
        self.pushButtonClearRecvArea = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonClearRecvArea.setGeometry(QtCore.QRect(130, 50, 100, 23))
        self.pushButtonClearRecvArea.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonClearRecvArea.setFlat(True)
        self.pushButtonClearRecvArea.setObjectName(_fromUtf8("pushButtonClearRecvArea"))

        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(X_START, 490, 240, 130))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.checkBoxSendFile = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxSendFile.setGeometry(QtCore.QRect(X_START, 20, 91, 17))
        self.checkBoxSendFile.setObjectName(_fromUtf8("checkBoxSendFile"))
        self.checkBoxEmptyAfterSent = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxEmptyAfterSent.setGeometry(QtCore.QRect(X_START, 40, 91, 17))
        self.checkBoxEmptyAfterSent.setObjectName(_fromUtf8("checkBoxEmptyAfterSent"))
        self.checkBoxSendHex = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxSendHex.setGeometry(QtCore.QRect(X_START, 60, 101, 17))
        self.checkBoxSendHex.setObjectName(_fromUtf8("checkBoxSendHex"))

        self.checkBoxSendLooping = QtGui.QCheckBox(self.groupBox_3)
        self.checkBoxSendLooping.setGeometry(QtCore.QRect(X_START, 80, 101, 17))
        self.checkBoxSendLooping.setObjectName(_fromUtf8("checkBoxSendLooping"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(121, 80, 41, 22))
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(X_START, 100, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        #self.horizontalLayout_2.addWidget(self.label_9)

        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(160, 80, 46, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButtonOpenSendFile = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonOpenSendFile.setGeometry(QtCore.QRect(120, 20, 100, 23))
        self.pushButtonOpenSendFile.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonOpenSendFile.setFlat(True)
        self.pushButtonOpenSendFile.setObjectName(_fromUtf8("pushButtonOpenSendFile"))
        self.pushButtonClearSendArea = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonClearSendArea.setGeometry(QtCore.QRect(120, 50, 100, 23))
        self.pushButtonClearSendArea.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonClearSendArea.setFlat(True)
        self.pushButtonClearSendArea.setObjectName(_fromUtf8("pushButtonClearSendArea"))
        self.textEditSent = serialportedittext.SerialPortInput(self.centralwidget)#QtGui.QTextEdit(self.centralwidget)
        self.textEditSent.setGeometry(QtCore.QRect(260, 330, 481, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEditSent.setFont(font)
        self.textEditSent.setObjectName(_fromUtf8("textEditSent"))
        self.pushButtonSendData = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSendData.setGeometry(QtCore.QRect(750, 330, 61, 221))
        self.pushButtonSendData.setObjectName(_fromUtf8("pushButtonSendData"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 20, 551, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBoxCD = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxCD.setFont(font)
        self.checkBoxCD.setObjectName(_fromUtf8("checkBoxCD"))
        self.horizontalLayout.addWidget(self.checkBoxCD)
        self.checkBoxRXD = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxRXD.setFont(font)
        self.checkBoxRXD.setObjectName(_fromUtf8("checkBoxRXD"))
        self.horizontalLayout.addWidget(self.checkBoxRXD)
        self.checkBoxTXD = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxTXD.setFont(font)
        self.checkBoxTXD.setObjectName(_fromUtf8("checkBoxTXD"))
        self.horizontalLayout.addWidget(self.checkBoxTXD)
        self.checkBoxDTR = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxDTR.setFont(font)
        self.checkBoxDTR.setObjectName(_fromUtf8("checkBoxDTR"))
        self.horizontalLayout.addWidget(self.checkBoxDTR)
        self.checkBoxGND = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxGND.setFont(font)
        self.checkBoxGND.setObjectName(_fromUtf8("checkBoxGND"))
        self.horizontalLayout.addWidget(self.checkBoxGND)
        self.checkBoxDSR = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxDSR.setFont(font)
        self.checkBoxDSR.setObjectName(_fromUtf8("checkBoxDSR"))
        self.horizontalLayout.addWidget(self.checkBoxDSR)
        self.checkBoxRTS = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxRTS.setFont(font)
        self.checkBoxRTS.setObjectName(_fromUtf8("checkBoxRTS"))
        self.horizontalLayout.addWidget(self.checkBoxRTS)
        self.checkBoxCTS = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxCTS.setFont(font)
        self.checkBoxCTS.setObjectName(_fromUtf8("checkBoxCTS"))
        self.horizontalLayout.addWidget(self.checkBoxCTS)
        self.checkBoxRI = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxRI.setFont(font)
        self.checkBoxRI.setObjectName(_fromUtf8("checkBoxRI"))
        self.horizontalLayout.addWidget(self.checkBoxRI)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 570, 548, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonClearAllCounts = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonClearAllCounts.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonClearAllCounts.setFlat(True)
        self.pushButtonClearAllCounts.setObjectName(_fromUtf8("pushButtonClearAllCounts"))
        self.horizontalLayout_2.addWidget(self.pushButtonClearAllCounts)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEditReceivedCounts = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditReceivedCounts.setReadOnly(True)
        self.lineEditReceivedCounts.setObjectName(_fromUtf8("lineEditReceivedCounts"))
        self.horizontalLayout_2.addWidget(self.lineEditReceivedCounts)
        self.pushButtonClearRecvCounts = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonClearRecvCounts.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonClearRecvCounts.setFlat(True)
        self.pushButtonClearRecvCounts.setObjectName(_fromUtf8("pushButtonClearRecvCounts"))
        self.horizontalLayout_2.addWidget(self.pushButtonClearRecvCounts)

        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEditSentCounts = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditSentCounts.setReadOnly(True)
        self.lineEditSentCounts.setObjectName(_fromUtf8("lineEditSentCounts"))
        self.horizontalLayout_2.addWidget(self.lineEditSentCounts)
        self.pushButtonClearSentCounts = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonClearSentCounts.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:blue;"))
        self.pushButtonClearSentCounts.setFlat(True)
        self.pushButtonClearSentCounts.setObjectName(_fromUtf8("pushButtonClearSentCounts"))
        self.horizontalLayout_2.addWidget(self.pushButtonClearSentCounts)
        SerialPortWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SerialPortWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SerialPortWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SerialPortWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SerialPortWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SerialPortWindow)
        QtCore.QMetaObject.connectSlotsByName(SerialPortWindow)

    def retranslateUi(self, SerialPortWindow):
        reg = registry.Registry()
        reg.readDB()
        #print "ddd" + reg.getPassword();

        SerialPortWindow.setWindowTitle(_translate("SerialPortWindow", "POS Transceiver ID: " + " " + getserial(), None))
        self.groupBox.setTitle(_translate("SerialPortWindow", "POS COM Port -> Pi's WiFi -> Cloud", None))
        self.label_email.setText(_translate("SerialPortWindow", "Email:", None))
        self.label_username.setText(_translate("SerialPortWindow", "Username:", None))
        self.label_password.setText(_translate("SerialPortWindow", "Password:", None))
        self.label_2.setText(_translate("SerialPortWindow", "Port:", None))
        self.label.setText(_translate("SerialPortWindow", "Baud:", None))
        self.label_3.setText(_translate("SerialPortWindow", "Check:", None))
        self.label_4.setText(_translate("SerialPortWindow", "Paraty:", None))
        self.label_5.setText(_translate("SerialPortWindow", "Stop:", None))

        self.textEditUsername.setText(reg.getUsername())
        self.textEditPassword.setText(reg.getPassword())
        #self.textEditPassword.setEchoMode(QLineEdit.Password)
        self.textEditEmail.setText(reg.getEmail())

        self.pushButtonOpenSerial.setText(_translate("SerialPortWindow", "Open", None))
        self.groupBox_2.setTitle(_translate("SerialPortWindow", "Receiving (POS -> Pi)", None))
        self.checkBoxSaveAsFile.setText(_translate("SerialPortWindow", "Save as", None))
        self.checkBoxNewLine.setText(_translate("SerialPortWindow", "Auto CR/LF", None))
        self.checkBoxDisplayHex.setText(_translate("SerialPortWindow", "Hex display", None))
        self.checkBoxStopReceive.setText(_translate("SerialPortWindow", "Pause", None))
        self.pushButtonOpenRecvFile.setText(_translate("SerialPortWindow", "New file", None))
        self.pushButtonClearRecvArea.setText(_translate("SerialPortWindow", "Clear buffer", None))
        self.groupBox_3.setTitle(_translate("SerialPortWindow", "Android POS -> Pi's WiFi -> Printer ", None))
        self.checkBoxSendFile.setText(_translate("SerialPortWindow", "Send doc", None))
        self.checkBoxEmptyAfterSent.setText(_translate("SerialPortWindow", "Clear after sent", None))
        self.checkBoxSendHex.setText(_translate("SerialPortWindow", "Hex input", None))
        self.checkBoxSendLooping.setText(_translate("SerialPortWindow", "Auto resent", None))
        self.label_6.setText(_translate("SerialPortWindow", "*100ms", None))
        self.pushButtonOpenSendFile.setText(_translate("SerialPortWindow", "Open file", None))
        self.pushButtonClearSendArea.setText(_translate("SerialPortWindow", "Clear buffer", None))
        self.pushButtonSendData.setText(_translate("SerialPortWindow", "Send", None))
        self.checkBoxCD.setText(_translate("SerialPortWindow", "1.CD", None))
        self.checkBoxRXD.setText(_translate("SerialPortWindow", "2.RXD", None))
        self.checkBoxTXD.setText(_translate("SerialPortWindow", "3.TXD", None))
        self.checkBoxDTR.setText(_translate("SerialPortWindow", "4.DTR", None))
        self.checkBoxGND.setText(_translate("SerialPortWindow", "5.GND", None))
        self.checkBoxDSR.setText(_translate("SerialPortWindow", "6.DSR", None))
        self.checkBoxRTS.setText(_translate("SerialPortWindow", "7.RTS", None))
        self.checkBoxCTS.setText(_translate("SerialPortWindow", "8.CTS", None))
        self.checkBoxRI.setText(_translate("SerialPortWindow", "9.RI", None))
        self.pushButtonClearAllCounts.setText(_translate("SerialPortWindow", "Reset counter", None))
        self.label_7.setText(_translate("SerialPortWindow", "Receive:", None))
        self.pushButtonClearRecvCounts.setText(_translate("SerialPortWindow", "Reset receiving", None))
        self.label_8.setText(_translate("SerialPortWindow", "Send:", None))
        self.pushButtonClearSentCounts.setText(_translate("SerialPortWindow", "Reset sending", None))
        self.label_9.setText(_translate("SerialPortWindow", "Serial #: " + getserial(), None))

