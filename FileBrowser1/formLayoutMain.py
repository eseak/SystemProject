#-*- coding: utf-8 -*-
__author__ = 'Ese'
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from formLayout import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.setWindowTitle("Layout...")
window.show()
sys.exit(app.exec_())