from icons import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/hangman.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/gameicon0.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonA = QtWidgets.QPushButton(self.frame_4)
        self.buttonA.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonA.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonA.setFont(font)
        self.buttonA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonA.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonA.setObjectName("buttonA")
        self.horizontalLayout.addWidget(self.buttonA)
        self.buttonB = QtWidgets.QPushButton(self.frame_4)
        self.buttonB.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonB.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonB.setFont(font)
        self.buttonB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonB.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonB.setObjectName("buttonB")
        self.horizontalLayout.addWidget(self.buttonB)
        self.buttonC = QtWidgets.QPushButton(self.frame_4)
        self.buttonC.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonC.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonC.setFont(font)
        self.buttonC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonC.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonC.setObjectName("buttonC")
        self.horizontalLayout.addWidget(self.buttonC)
        self.buttonD = QtWidgets.QPushButton(self.frame_4)
        self.buttonD.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonD.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonD.setFont(font)
        self.buttonD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonD.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonD.setObjectName("buttonD")
        self.horizontalLayout.addWidget(self.buttonD)
        self.buttonE = QtWidgets.QPushButton(self.frame_4)
        self.buttonE.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonE.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonE.setFont(font)
        self.buttonE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonE.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonE.setObjectName("buttonE")
        self.horizontalLayout.addWidget(self.buttonE)
        self.buttonF = QtWidgets.QPushButton(self.frame_4)
        self.buttonF.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonF.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonF.setFont(font)
        self.buttonF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonF.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonF.setObjectName("buttonF")
        self.horizontalLayout.addWidget(self.buttonF)
        self.buttonG = QtWidgets.QPushButton(self.frame_4)
        self.buttonG.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonG.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonG.setFont(font)
        self.buttonG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonG.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonG.setObjectName("buttonG")
        self.horizontalLayout.addWidget(self.buttonG)
        self.buttonH = QtWidgets.QPushButton(self.frame_4)
        self.buttonH.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonH.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonH.setFont(font)
        self.buttonH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonH.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonH.setObjectName("buttonH")
        self.horizontalLayout.addWidget(self.buttonH)
        self.buttonI = QtWidgets.QPushButton(self.frame_4)
        self.buttonI.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonI.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonI.setFont(font)
        self.buttonI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonI.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonI.setObjectName("buttonI")
        self.horizontalLayout.addWidget(self.buttonI)
        self.buttonJ = QtWidgets.QPushButton(self.frame_4)
        self.buttonJ.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonJ.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonJ.setFont(font)
        self.buttonJ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonJ.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonJ.setObjectName("buttonJ")
        self.horizontalLayout.addWidget(self.buttonJ)
        self.buttonK = QtWidgets.QPushButton(self.frame_4)
        self.buttonK.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonK.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonK.setFont(font)
        self.buttonK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonK.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonK.setObjectName("buttonK")
        self.horizontalLayout.addWidget(self.buttonK)
        self.buttonL = QtWidgets.QPushButton(self.frame_4)
        self.buttonL.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonL.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonL.setFont(font)
        self.buttonL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonL.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonL.setObjectName("buttonL")
        self.horizontalLayout.addWidget(self.buttonL)
        self.buttonM = QtWidgets.QPushButton(self.frame_4)
        self.buttonM.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonM.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonM.setFont(font)
        self.buttonM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonM.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonM.setObjectName("buttonM")
        self.horizontalLayout.addWidget(self.buttonM)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonN = QtWidgets.QPushButton(self.frame_4)
        self.buttonN.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonN.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonN.setFont(font)
        self.buttonN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonN.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonN.setObjectName("buttonN")
        self.horizontalLayout_2.addWidget(self.buttonN)
        self.buttonO = QtWidgets.QPushButton(self.frame_4)
        self.buttonO.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonO.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonO.setFont(font)
        self.buttonO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonO.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonO.setObjectName("buttonO")
        self.horizontalLayout_2.addWidget(self.buttonO)
        self.buttonP = QtWidgets.QPushButton(self.frame_4)
        self.buttonP.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonP.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonP.setFont(font)
        self.buttonP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonP.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonP.setObjectName("buttonP")
        self.horizontalLayout_2.addWidget(self.buttonP)
        self.buttonQ = QtWidgets.QPushButton(self.frame_4)
        self.buttonQ.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonQ.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonQ.setFont(font)
        self.buttonQ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonQ.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonQ.setObjectName("buttonQ")
        self.horizontalLayout_2.addWidget(self.buttonQ)
        self.buttonR = QtWidgets.QPushButton(self.frame_4)
        self.buttonR.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonR.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonR.setFont(font)
        self.buttonR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonR.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonR.setObjectName("buttonR")
        self.horizontalLayout_2.addWidget(self.buttonR)
        self.buttonS = QtWidgets.QPushButton(self.frame_4)
        self.buttonS.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonS.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonS.setFont(font)
        self.buttonS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonS.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonS.setObjectName("buttonS")
        self.horizontalLayout_2.addWidget(self.buttonS)
        self.buttonT = QtWidgets.QPushButton(self.frame_4)
        self.buttonT.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonT.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonT.setFont(font)
        self.buttonT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonT.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonT.setObjectName("buttonT")
        self.horizontalLayout_2.addWidget(self.buttonT)
        self.buttonU = QtWidgets.QPushButton(self.frame_4)
        self.buttonU.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonU.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonU.setFont(font)
        self.buttonU.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonU.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonU.setObjectName("buttonU")
        self.horizontalLayout_2.addWidget(self.buttonU)
        self.buttonV = QtWidgets.QPushButton(self.frame_4)
        self.buttonV.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonV.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonV.setFont(font)
        self.buttonV.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonV.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonV.setObjectName("buttonV")
        self.horizontalLayout_2.addWidget(self.buttonV)
        self.buttonW = QtWidgets.QPushButton(self.frame_4)
        self.buttonW.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonW.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonW.setFont(font)
        self.buttonW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonW.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonW.setObjectName("buttonW")
        self.horizontalLayout_2.addWidget(self.buttonW)
        self.buttonX = QtWidgets.QPushButton(self.frame_4)
        self.buttonX.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonX.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonX.setFont(font)
        self.buttonX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonX.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonX.setObjectName("buttonX")
        self.horizontalLayout_2.addWidget(self.buttonX)
        self.buttonY = QtWidgets.QPushButton(self.frame_4)
        self.buttonY.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonY.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonY.setFont(font)
        self.buttonY.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonY.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonY.setObjectName("buttonY")
        self.horizontalLayout_2.addWidget(self.buttonY)
        self.buttonZ = QtWidgets.QPushButton(self.frame_4)
        self.buttonZ.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonZ.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.buttonZ.setFont(font)
        self.buttonZ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonZ.setStyleSheet("background-color: white;\n"
                                   "color: black;\n"
                                   "border: 2px solid #000000;\n"
                                   "text-align: center;\n"
                                   "text-decoration: none;\n"
                                   "display: inline-block;\n"
                                   "font-size: 16px;\n"
                                   "border-radius: 30px;\n"
                                   "\n"
                                   "")
        self.buttonZ.setObjectName("buttonZ")
        self.horizontalLayout_2.addWidget(self.buttonZ)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "----------"))
        self.buttonA.setText(_translate("MainWindow", "A"))
        self.buttonB.setText(_translate("MainWindow", "B"))
        self.buttonC.setText(_translate("MainWindow", "C"))
        self.buttonD.setText(_translate("MainWindow", "D"))
        self.buttonE.setText(_translate("MainWindow", "E"))
        self.buttonF.setText(_translate("MainWindow", "F"))
        self.buttonG.setText(_translate("MainWindow", "G"))
        self.buttonH.setText(_translate("MainWindow", "H"))
        self.buttonI.setText(_translate("MainWindow", "I"))
        self.buttonJ.setText(_translate("MainWindow", "J"))
        self.buttonK.setText(_translate("MainWindow", "K"))
        self.buttonL.setText(_translate("MainWindow", "L"))
        self.buttonM.setText(_translate("MainWindow", "M"))
        self.buttonN.setText(_translate("MainWindow", "N"))
        self.buttonO.setText(_translate("MainWindow", "O"))
        self.buttonP.setText(_translate("MainWindow", "P"))
        self.buttonQ.setText(_translate("MainWindow", "Q"))
        self.buttonR.setText(_translate("MainWindow", "R"))
        self.buttonS.setText(_translate("MainWindow", "S"))
        self.buttonT.setText(_translate("MainWindow", "T"))
        self.buttonU.setText(_translate("MainWindow", "U"))
        self.buttonV.setText(_translate("MainWindow", "V"))
        self.buttonW.setText(_translate("MainWindow", "W"))
        self.buttonX.setText(_translate("MainWindow", "X"))
        self.buttonY.setText(_translate("MainWindow", "Y"))
        self.buttonZ.setText(_translate("MainWindow", "Z"))
