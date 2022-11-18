import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from secondwindow import secondwindow
from gensim.models.word2vec import Word2Vec
from method import get_words

form_main = uic.loadUiType("./ui_files/mainwindow.ui")[0]
class MainWindow(QMainWindow, QWidget, form_main):
    def __init__(self):
        super().__init__()
        self.words = []
        self.model = Word2Vec.load('./datasets/ko.bin')
        self.initUI()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.SecondWindow.clicked.connect(self.button_Second)

    def button_Second(self):
        word = self.keyword_input.toPlainText()
        self.words.append(word)
        top15 = get_words(word, self.model)
        self.close()
        self.second = secondwindow(self.words, top15)
        self.second.exec()
        self.show()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())