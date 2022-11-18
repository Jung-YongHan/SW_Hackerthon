import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from gensim.models.word2vec import Word2Vec
from method import get_words

form_secondwindow = uic.loadUiType("./ui_files/secondwindow.ui")[0]

class secondwindow(QDialog, QWidget, form_secondwindow):
    def __init__(self, words, top15):
        super(secondwindow, self).__init__()
        self.words = words
        self.top15 = top15
        self.model = Word2Vec.load('./datasets/ko.bin')
        self.initUI()
        self.show()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def initUI(self):
        self.setupUi(self)
        self.second_text.setText((self.words[-1]))
        self.pushButton_1.setText(self.top15[0][0]+ "\n" + str('{:.4f}'.format(self.top15[0][1])))
        self.pushButton_2.setText(self.top15[1][0]+ "\n" + str('{:.4f}'.format(self.top15[1][1])))
        self.pushButton_3.setText(self.top15[2][0]+ "\n" + str('{:.4f}'.format(self.top15[2][1])))
        self.pushButton_4.setText(self.top15[3][0]+ "\n" + str('{:.4f}'.format(self.top15[3][1])))
        self.pushButton_5.setText(self.top15[4][0]+ "\n" + str('{:.4f}'.format(self.top15[4][1])))
        self.pushButton_6.setText(self.top15[5][0]+ "\n" + str('{:.4f}'.format(self.top15[5][1])))
        self.pushButton_7.setText(self.top15[6][0]+ "\n" + str('{:.4f}'.format(self.top15[6][1])))
        self.pushButton_8.setText(self.top15[7][0]+ "\n" + str('{:.4f}'.format(self.top15[7][1])))
        self.pushButton_9.setText(self.top15[8][0]+ "\n" + str('{:.4f}'.format(self.top15[8][1])))
        self.pushButton_10.setText(self.top15[9][0]+ "\n" + str('{:.4f}'.format(self.top15[9][1])))
        self.pushButton_11.setText(self.top15[10][0] + "\n" + str('{:.4f}'.format(self.top15[10][1])))
        self.pushButton_12.setText(self.top15[11][0] + "\n" + str('{:.4f}'.format(self.top15[11][1])))
        self.pushButton_13.setText(self.top15[12][0] + "\n" + str('{:.4f}'.format(self.top15[12][1])))
        self.pushButton_14.setText(self.top15[13][0] + "\n" + str('{:.4f}'.format(self.top15[13][1])))
        self.pushButton_15.setText(self.top15[14][0] + "\n" + str('{:.4f}'.format(self.top15[14][1])))

        self.exitButton.clicked.connect(self.exit)

        self.pushButton_1.clicked.connect(lambda: self.change('1'))
        self.pushButton_2.clicked.connect(lambda: self.change('2'))
        self.pushButton_3.clicked.connect(lambda: self.change('3'))
        self.pushButton_4.clicked.connect(lambda: self.change('4'))
        self.pushButton_5.clicked.connect(lambda: self.change('5'))
        self.pushButton_6.clicked.connect(lambda: self.change('6'))
        self.pushButton_7.clicked.connect(lambda: self.change('7'))
        self.pushButton_8.clicked.connect(lambda: self.change('8'))
        self.pushButton_9.clicked.connect(lambda: self.change('9'))
        self.pushButton_10.clicked.connect(lambda: self.change('10'))
        self.pushButton_11.clicked.connect(lambda: self.change('11'))
        self.pushButton_12.clicked.connect(lambda: self.change('12'))
        self.pushButton_13.clicked.connect(lambda: self.change('13'))
        self.pushButton_14.clicked.connect(lambda: self.change('14'))
        self.pushButton_15.clicked.connect(lambda: self.change('15'))



    def exit(self):
        sys.exit()


    def change(self, get):
        if get == '1':
            word = self.pushButton_1.text()
        elif get == '2':
            word = self.pushButton_2.text()
        elif get == '3':
            word = self.pushButton_3.text()
        elif get == '4':
            word = self.pushButton_4.text()
        elif get == '5':
            word = self.pushButton_5.text()
        elif get == '6':
            word = self.pushButton_6.text()
        elif get == '7':
            word = self.pushButton_7.text()
        elif get == '8':
            word = self.pushButton_8.text()
        elif get == '9':
            word = self.pushButton_9.text()
        elif get == '10':
            word = self.pushButton_10.text()
        elif get == '11':
            word = self.pushButton_11.text()
        elif get == '12':
            word = self.pushButton_12.text()
        elif get == '13':
            word = self.pushButton_13.text()
        elif get == '14':
            word = self.pushButton_14.text()
        else:
            word = self.pushButton_15.text()
        word = word.split('\n')[0]
        self.words.append(word)
        self.top15 = get_words(self.words, self.model)
        self.close()
        self.second = secondwindow(self.words, self.top15)
        self.second.exec()
        self.show()


