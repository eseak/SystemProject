# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psutil,os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setMaximumWidth(150)
        self.listWidget.setMaximumHeight(120)
        self.fillDiskList()
        self.verticalLayout.addWidget(self.listWidget)
        self.listWidget.currentItemChanged.connect(self.diskFileList)





        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 150, 150))



        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.setMaximumWidth(150)
        self.verticalLayout.addWidget(self.treeWidget)



        self.horizontalLayout.addLayout(self.verticalLayout)


        '''
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        '''
        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget2.setObjectName("listWidget2")
        #self.listWidget2.setMaximumWidth(150)
        self.horizontalLayout.addWidget(self.listWidget2)




        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def getDiskList(self):
        self.diskListesi=[]
        partitions=psutil.disk_partitions(all=False)
        for part in partitions:
            S=""+str(part)
            Start=S.find('mountpoint')+12
            End=S.find('\'',Start,len(S))
            diskname=S[Start:End]
            self.diskListesi.append(diskname)
        return self.diskListesi
    def fillDiskList(self):
        dl=self.getDiskList()
        for diskname in dl:
            self.listWidget.addItem(diskname)

    #Diske tıklandığında çalışan metod
    def diskFileList(self):
        self.treeWidget.clear()
        self.selectedDiskName=self.listWidget.currentItem().text()
        self.rootNameOfFileTreeWidget=self.selectedDiskName
        self.fillFolderTreeWidgetRootName=self.selectedDiskName
        self.fillFolderTreeWidget()#Disk listesine tıklandığında Klasör listesini de güncelle
        print(os.listdir(self.selectedDiskName))

    def fillFolderTreeWidget(self):

        header=QtWidgets.QTreeWidgetItem(["Klasörler"])
        self.treeWidget.setHeaderItem(header)
        root = QtWidgets.QTreeWidgetItem(self.treeWidget, [self.fillFolderTreeWidgetRootName])
        self.activeFolderContent=os.listdir(self.selectedDiskName)
        for folName in self.activeFolderContent:
            QtWidgets.QTreeWidgetItem(root, [folName])



        #A = QtWidgets.QTreeWidgetItem(root, ["A"])
        #barA = QtWidgets.QTreeWidgetItem(A, ["bar"])
        #bazA = QtWidgets.QTreeWidgetItem(A, ["baz"])


