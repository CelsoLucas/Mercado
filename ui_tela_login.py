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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
from imgs import icons_rc

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
        TelaLogin.setMinimumSize(QSize(0, 0))
        TelaLogin.setStyleSheet(u"QMainWindow {\n"
"background-color: rgb(76,81,191);\n"
"background-color: linear-gradient(155deg, rgba(76,81,191,1) 0%, rgba(0,0,0,1) 100%);}\n"
"\n"
"#layout,  #layout_2{\n"
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
"    font-size: 20px;\n"
"    color: #2D3748;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4C51BF;\n"
"}\n"
"")
        self.centralwidget = QWidget(TelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout = QFrame(self.page1)
        self.layout.setObjectName(u"layout")
        self.layout.setMinimumSize(QSize(550, 600))
        self.layout.setStyleSheet(u"")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.layout)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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


        self.verticalLayout_6.addWidget(self.layout_img_login)

        self.txt_login = QLabel(self.layout)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setStyleSheet(u"font-size: 40px;\n"
"font-weight: bold;")
        self.txt_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.txt_login)

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


        self.verticalLayout_6.addWidget(self.layout_user)

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

        self.btn_esqueci_senha = QPushButton(self.layout_senha)
        self.btn_esqueci_senha.setObjectName(u"btn_esqueci_senha")
        self.btn_esqueci_senha.setMaximumSize(QSize(170, 37))
        self.btn_esqueci_senha.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_esqueci_senha.setStyleSheet(u"QPushButton {\n"
"    background-color: none;\n"
"    color: rgb(0, 13, 255);\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(170, 153, 255);\n"
"}")

        self.verticalLayout.addWidget(self.btn_esqueci_senha, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_6.addWidget(self.layout_senha)

        self.btn_login = QPushButton(self.layout)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(130, 40))
        self.btn_login.setMaximumSize(QSize(153, 53))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_login.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.txt_login.raise_()
        self.layout_user.raise_()
        self.layout_senha.raise_()
        self.layout_img_login.raise_()
        self.btn_login.raise_()

        self.verticalLayout_3.addWidget(self.layout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.layout_2 = QFrame(self.page_2)
        self.layout_2.setObjectName(u"layout_2")
        self.layout_2.setMinimumSize(QSize(550, 600))
        self.layout_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.layout_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.layout_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"font-weight: 600;")

        self.verticalLayout_8.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame = QFrame(self.layout_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_email = QLineEdit(self.frame_2)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setMinimumSize(QSize(375, 0))

        self.horizontalLayout.addWidget(self.input_email)

        self.btn_enviar_codigo = QPushButton(self.frame_2)
        self.btn_enviar_codigo.setObjectName(u"btn_enviar_codigo")
        self.btn_enviar_codigo.setStyleSheet(u"background-color: none;\n"
"border: 1px solid #E2E8F0;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/mail-send.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_enviar_codigo.setIcon(icon)
        self.btn_enviar_codigo.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_enviar_codigo)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.input_cod = QLineEdit(self.frame_3)
        self.input_cod.setObjectName(u"input_cod")
        self.input_cod.setMinimumSize(QSize(375, 0))

        self.verticalLayout_10.addWidget(self.input_cod)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.input_nova_senha = QLineEdit(self.frame_4)
        self.input_nova_senha.setObjectName(u"input_nova_senha")
        self.input_nova_senha.setMinimumSize(QSize(375, 0))
        self.input_nova_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_11.addWidget(self.input_nova_senha)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.input_confirmar_senha = QLineEdit(self.frame_5)
        self.input_confirmar_senha.setObjectName(u"input_confirmar_senha")
        self.input_confirmar_senha.setMinimumSize(QSize(375, 0))
        self.input_confirmar_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_12.addWidget(self.input_confirmar_senha)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_voltar = QPushButton(self.frame_6)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.horizontalLayout_2.addWidget(self.btn_voltar)

        self.btn_redefinir_senha = QPushButton(self.frame_6)
        self.btn_redefinir_senha.setObjectName(u"btn_redefinir_senha")

        self.horizontalLayout_2.addWidget(self.btn_redefinir_senha)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_8.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.layout_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stackedWidget)

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
        self.btn_esqueci_senha.setText(QCoreApplication.translate("TelaLogin", u"Esqueci minha senha", None))
        self.btn_login.setText(QCoreApplication.translate("TelaLogin", u"Login", None))
        self.label.setText(QCoreApplication.translate("TelaLogin", u"Recuperar Senha", None))
        self.input_email.setText("")
        self.input_email.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"Digite seu Email para recuperar a senha", None))
        self.btn_enviar_codigo.setText("")
        self.input_cod.setText("")
        self.input_cod.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"C\u00f3digo de 6 digitos", None))
        self.input_nova_senha.setText("")
        self.input_nova_senha.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"Digite a nova senha", None))
        self.input_confirmar_senha.setPlaceholderText(QCoreApplication.translate("TelaLogin", u"Confirmar nova senha", None))
        self.btn_voltar.setText(QCoreApplication.translate("TelaLogin", u"Voltar", None))
        self.btn_redefinir_senha.setText(QCoreApplication.translate("TelaLogin", u"Redefinir Senha", None))
    # retranslateUi

