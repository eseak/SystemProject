#-*- coding: utf-8 -*-
__author__ = 'Ese'
import sys
from PyQt5.QtWidgets import *
from formLayout2 import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.setWindowTitle("Dosya Gezgini")
window.show()
sys.exit(app.exec_())