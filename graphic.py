# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphic.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: black;\n"
"	background-color: #e1e8f0;\n"
"	font-size: 14pt;\n"
"}")
        MainWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.UpArrowCursor))
        self.label_m = QLabel(self.centralwidget)
        self.label_m.setObjectName(u"label_m")
        self.label_m.setGeometry(QRect(20, 390, 21, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_m.sizePolicy().hasHeightForWidth())
        self.label_m.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_m.setFont(font)
        self.lineEdit_m = QLineEdit(self.centralwidget)
        self.lineEdit_m.setObjectName(u"lineEdit_m")
        self.lineEdit_m.setGeometry(QRect(40, 390, 531, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.lineEdit_m.setFont(font1)
        self.lineEdit_m.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_m_top = QLabel(self.centralwidget)
        self.label_m_top.setObjectName(u"label_m_top")
        self.label_m_top.setGeometry(QRect(60, 360, 521, 21))
        self.label_m_top.setFont(font)
        self.label_S_top = QLabel(self.centralwidget)
        self.label_S_top.setObjectName(u"label_S_top")
        self.label_S_top.setGeometry(QRect(180, 290, 391, 21))
        self.label_S_top.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 220, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.lineEdit_p = QLineEdit(self.centralwidget)
        self.lineEdit_p.setObjectName(u"lineEdit_p")
        self.lineEdit_p.setGeometry(QRect(30, 40, 551, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.lineEdit_p.setFont(font3)
        self.lineEdit_p.setStyleSheet(u"font-size: 18pt;")
        self.lineEdit_p.setMaxLength(1000)
        self.lineEdit_p.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_p.setReadOnly(True)
        self.lineEdit_p.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_p_2 = QLineEdit(self.centralwidget)
        self.lineEdit_p_2.setObjectName(u"lineEdit_p_2")
        self.lineEdit_p_2.setGeometry(QRect(30, 120, 551, 41))
        self.lineEdit_p_2.setFont(font3)
        self.lineEdit_p_2.setStyleSheet(u"font-size: 18pt;")
        self.lineEdit_p_2.setMaxLength(30)
        self.lineEdit_p_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_p_2.setReadOnly(True)
        self.label_S = QLabel(self.centralwidget)
        self.label_S.setObjectName(u"label_S")
        self.label_S.setGeometry(QRect(20, 320, 16, 31))
        sizePolicy.setHeightForWidth(self.label_S.sizePolicy().hasHeightForWidth())
        self.label_S.setSizePolicy(sizePolicy)
        self.label_S.setFont(font)
        self.lineEdit_S = QLineEdit(self.centralwidget)
        self.lineEdit_S.setObjectName(u"lineEdit_S")
        self.lineEdit_S.setGeometry(QRect(40, 320, 531, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_S.sizePolicy().hasHeightForWidth())
        self.lineEdit_S.setSizePolicy(sizePolicy1)
        self.lineEdit_S.setFont(font1)
        self.lineEdit_S.setMaxLength(100)
        self.lineEdit_S.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_S_top_2 = QLabel(self.centralwidget)
        self.label_S_top_2.setObjectName(u"label_S_top_2")
        self.label_S_top_2.setGeometry(QRect(240, 90, 341, 21))
        self.label_S_top_2.setFont(font)
        self.label_S_top_3 = QLabel(self.centralwidget)
        self.label_S_top_3.setObjectName(u"label_S_top_3")
        self.label_S_top_3.setGeometry(QRect(330, 10, 251, 21))
        self.label_S_top_3.setFont(font)
        self.lineEdit_m_2 = QLineEdit(self.centralwidget)
        self.lineEdit_m_2.setObjectName(u"lineEdit_m_2")
        self.lineEdit_m_2.setGeometry(QRect(40, 460, 531, 31))
        self.lineEdit_m_2.setFont(font1)
        self.lineEdit_m_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_m_top_2 = QLabel(self.centralwidget)
        self.label_m_top_2.setObjectName(u"label_m_top_2")
        self.label_m_top_2.setGeometry(QRect(310, 430, 261, 21))
        self.label_m_top_2.setFont(font)
        self.label_m_2 = QLabel(self.centralwidget)
        self.label_m_2.setObjectName(u"label_m_2")
        self.label_m_2.setGeometry(QRect(20, 460, 21, 31))
        sizePolicy.setHeightForWidth(self.label_m_2.sizePolicy().hasHeightForWidth())
        self.label_m_2.setSizePolicy(sizePolicy)
        self.label_m_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Effectiveness", None))
        self.label_m.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.lineEdit_m.setText(QCoreApplication.translate("MainWindow", u"2, 2, 1", None))
        self.label_m_top.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043f\u0430\u0434\u0430\u043d\u0438\u0439 \u0432 \u043a\u0430\u0436\u0434\u044b\u0439 \u043e\u0442\u0441\u0435\u043a", None))
        self.label_S_top.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u043f\u043b\u043e\u0449\u0430\u0434\u044c \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0446\u0435\u043b\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0421\u0421\u0427\u0418\u0422\u0410\u0422\u042c", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_p.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_p_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.lineEdit_S.setText(QCoreApplication.translate("MainWindow", u"0.3, 0.3, 0.4", None))
        self.label_S_top_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u043f\u043e\u043f\u0430\u0434\u0430\u043d\u0438\u0439", None))
        self.label_S_top_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0446\u0435\u043b\u0438", None))
        self.lineEdit_m_2.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_m_top_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0441\u0442\u0440\u0435\u043b\u043e\u0432", None))
        self.label_m_2.setText(QCoreApplication.translate("MainWindow", u"n", None))
    # retranslateUi

