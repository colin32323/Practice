import sys
import random
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.tries = 6
        self.movie, self.movieLabel = movieSelect()
        self.label_2.setText(self.movieLabel)
        self.buttonA.clicked.connect(lambda: self.guess('A', self.buttonA))
        self.buttonB.clicked.connect(lambda: self.guess('B', self.buttonB))
        self.buttonC.clicked.connect(lambda: self.guess('C', self.buttonC))
        self.buttonD.clicked.connect(lambda: self.guess('D', self.buttonD))
        self.buttonE.clicked.connect(lambda: self.guess('E', self.buttonE))
        self.buttonF.clicked.connect(lambda: self.guess('F', self.buttonF))
        self.buttonG.clicked.connect(lambda: self.guess('G', self.buttonG))
        self.buttonH.clicked.connect(lambda: self.guess('H', self.buttonH))
        self.buttonI.clicked.connect(lambda: self.guess('I', self.buttonI))
        self.buttonJ.clicked.connect(lambda: self.guess('J', self.buttonJ))
        self.buttonK.clicked.connect(lambda: self.guess('K', self.buttonK))
        self.buttonL.clicked.connect(lambda: self.guess('L', self.buttonL))
        self.buttonM.clicked.connect(lambda: self.guess('M', self.buttonM))
        self.buttonN.clicked.connect(lambda: self.guess('N', self.buttonN))
        self.buttonO.clicked.connect(lambda: self.guess('O', self.buttonO))
        self.buttonP.clicked.connect(lambda: self.guess('P', self.buttonP))
        self.buttonQ.clicked.connect(lambda: self.guess('Q', self.buttonQ))
        self.buttonR.clicked.connect(lambda: self.guess('R', self.buttonR))
        self.buttonS.clicked.connect(lambda: self.guess('S', self.buttonS))
        self.buttonT.clicked.connect(lambda: self.guess('T', self.buttonT))
        self.buttonU.clicked.connect(lambda: self.guess('U', self.buttonU))
        self.buttonV.clicked.connect(lambda: self.guess('V', self.buttonV))
        self.buttonW.clicked.connect(lambda: self.guess('W', self.buttonW))
        self.buttonX.clicked.connect(lambda: self.guess('X', self.buttonX))
        self.buttonY.clicked.connect(lambda: self.guess('Y', self.buttonY))
        self.buttonZ.clicked.connect(lambda: self.guess('Z', self.buttonZ))

    def guess(self, letter, button):
        if letter in self.movie:
            for i in range(len(self.movie)):
                if self.movie[i] == letter:
                    self.movieLabel = self.movieLabel[:i] + \
                        letter + self.movieLabel[i+1:]
            self.label_2.setText(self.movieLabel)
            if self.movie == self.movieLabel:
                self.label_2.setText(self.movieLabel + '\nYOU WON!!')

        else:
            self.tries -= 1
            if self.tries == 5:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon1.png'))
            elif self.tries == 4:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon2.png'))
            elif self.tries == 3:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon3.png'))
            elif self.tries == 2:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon4.png'))
            elif self.tries == 1:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon5.png'))
            else:
                self.label.setPixmap(QtGui.QPixmap('./icons/gameicon6.png'))
                self.label_2.setText(f'YOU LOST!!\n A: {self.movie}')

        button.setStyleSheet(
            "background-color: white;\n"
            "color: white;\n"
            "border: none;\n"
            "\n"
            ""
        )
        button.setEnabled(False)
        button.setCursor(QCursor(QtCore.Qt.ArrowCursor))


def movieSelect():
    movies = []
    with open('movies.txt') as file:
        for line in file:
            movies.extend(line.strip().split('\n'))
    movie = random.choice(movies).upper()
    temp = movie
    for i in range(len(movie)):
        if movie[i].isalpha():
            movie = movie[:i] + '-' + movie[i+1:]
    return temp, movie


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
