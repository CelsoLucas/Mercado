# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        if not TelaLogin.objectName():
            TelaLogin.setObjectName(u"TelaLogin")
        TelaLogin.resize(942, 1051)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaLogin.sizePolicy().hasHeightForWidth())
        TelaLogin.setSizePolicy(sizePolicy)
        TelaLogin.setStyleSheet(u"QMainWindow {\n"
"    background-color: #F5F6FA;\n"
"}\n"
"\n"
"#layout{\n"
"	\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4C51BF;\n"
"    color: #FFFFFF;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding: 10px 20px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5A67D8;\n"
"    transition: background-color 0.2s ease;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #434190;\n"
"}\n"
"\n"
"/* Inputs */\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E2E8F0;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4C51BF;\n"
"    box-shadow: 0 0 5px rgba(76, 81, 191, 0.3);\n"
"}")
        self.centralwidget = QWidget(TelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layout = QFrame(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.layout.setMinimumSize(QSize(550, 600))
        self.layout.setStyleSheet(u"")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_img_login = QFrame(self.layout)
        self.layout_img_login.setObjectName(u"layout_img_login")
        self.layout_img_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_img_login.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.layout_img_login)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.icon_login = QLabel(self.layout_img_login)
        self.icon_login.setObjectName(u"icon_login")
        self.icon_login.setMaximumSize(QSize(150, 150))
        self.icon_login.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.icon_login, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.layout_img_login)

        self.txt_login = QLabel(self.layout)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setStyleSheet(u"font-size: 40px;\n"
"font-weight: bold;")
        self.txt_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_login)

        self.layout_user = QFrame(self.layout)
        self.layout_user.setObjectName(u"layout_user")
        self.layout_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_user.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout_user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_user = QLineEdit(self.layout_user)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setStyleSheet(u"")
        self.input_user.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.input_user)


        self.verticalLayout_3.addWidget(self.layout_user)

        self.layout_senha = QFrame(self.layout)
        self.layout_senha.setObjectName(u"layout_senha")
        self.layout_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.layout_senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_senha = QLineEdit(self.layout_senha)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setStyleSheet(u"")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.input_senha)


        self.verticalLayout_3.addWidget(self.layout_senha)

        self.btn_login = QPushButton(self.layout)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(153, 53))
        self.btn_login.setMaximumSize(QSize(153, 53))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_login.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_login, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_login.raise_()
        self.txt_login.raise_()
        self.layout_user.raise_()
        self.layout_senha.raise_()
        self.layout_img_login.raise_()

        self.verticalLayout_4.addWidget(self.layout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)

        QMetaObject.connectSlotsByName(TelaLogin)
    # setupUi

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(QCoreApplication.translate("TelaLogin", u"MainWindow", None))
        self.icon_login.setText("")
        self.txt_login.setText(QCoreApplication.translate("TelaLogin", u"LOGIN", None))
        self.input_user.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"Usuario", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("TelaLogin", u"Login", None))
    # retranslateUi

