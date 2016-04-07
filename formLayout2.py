# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psutil,os
class Ui_MainWindow(object):
    def __init__(self):
        print('Başladı')


##*****************************************************************
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
        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setMaximumWidth(250)
        self.listWidget.setMaximumHeight(120)
        self.verticalLayout.addWidget(self.listWidget)


        #disk listesini, Aktif yol klasör listesini ve aktif yolun değerini dolduralım**********************************************************
        self.setDiskList()
        self.fillDiskListBox()
        self.activeWayFolderList=[]
        self.activeWayFolderList.append(self.diskList.__getitem__(0))
        self.activeWay=self.diskList.__getitem__(0)
        print('BAŞLANGIÇTA ATANAN YOL, EN KÜÇÜK İNDİSLİ DİSK:',self.activeWay)


        self.listWidget.currentItemChanged.connect(self.diskFileList)
        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.setMaximumWidth(250)
        self.verticalLayout.addWidget(self.treeWidget)
        self.treeWidget.itemSelectionChanged.connect(self.fillFileList)
       # self.treeWidget.doubleClicked.connect(self.treeDoubleClicked)
        self.treeWidget.itemDoubleClicked.connect(self.treeDoubleClicked)
       # QtCore.QMetaObject.connectSlotsByName(MainWindow)









        self.horizontalLayout.addLayout(self.verticalLayout)




        self.listWidget2.setObjectName("listWidget2")

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
#Bilgisayardaki disk adlarını(mouth) bir listede tutar
    def setDiskList(self):
        self.diskList=[]
        partitions=psutil.disk_partitions(all=False)
        for part in partitions:
            S=""+str(part)
            Start=S.find('mountpoint')+12
            End=S.find('\'',Start,len(S))
            diskname=S[Start:End]
            self.diskList.append(diskname)
            print('eklenen disk adı:',diskname)

    #Disklerin listesini bir dizin halinde verir
    def getDiskList(self):
        return self.diskList
    #


    def fillDiskListBox(self):
        dl=self.getDiskList()
        for diskname in dl:
            self.listWidget.addItem(diskname)
    #***************************************************************

    #Diske tıklandığında çalışan metod
    def diskFileList(self):
        #Sol taraftaki dizin ağacını temizle
        self.treeWidget.clear()
        #DiskLste kurtusunda seçilmiş disk aının değerin,i al
        self.selectedDiskName=self.listWidget.currentItem().text()
        #Aktif yolu da tıklanan disk olarak değiştirdik
        #self.activeWay=self.selectedDiskName.strip()
        self.activeWayFolderList.clear()#Aktif dizin silsilesini temizle
        #Seçilen dis adını yol dizinler listesine ekle
        self.activeWayFolderList.append(self.selectedDiskName)
        self.fillFolderTreeWidget()#Disk listesine tıklandığında Klasör listesini de güncelle
        self.treeWidget.expandAll()

    #Sol taraftak klasör ağacını dolduran metod: Diske tıklandığında veya Klasör ağcandan double click(hazır değil) yapıldığında çalışır
    def fillFolderTreeWidget(self):
        #Önce son tıklamaya göre aktif dizini güncelleyelim
        self.createActiveWay()
        print('İçeriği Listelenecek aktif yol:',self.activeWay)
        header=QtWidgets.QTreeWidgetItem(["Klasörler"])
        self.treeWidget.setHeaderItem(header)
        self.goUpTtreeWidget = QtWidgets.QTreeWidgetItem(self.treeWidget, ['^ Yukarı'])
        self.fillFolderTreeWidgetRootName=self.selectedDiskName
        self.rootTreeWidget = QtWidgets.QTreeWidgetItem(self.treeWidget, [self.fillFolderTreeWidgetRootName])
        self.activeFolderContent=os.listdir(self.activeWay)
        for folName in self.activeFolderContent:
            if os.path.isdir(self.activeWay+'/'+folName):
                QtWidgets.QTreeWidgetItem(self.rootTreeWidget, [folName])
                print('dizindir')
        print('DİZİN AĞACI DOLDURULDU: YENİ AKTİF YOL YAZILIYOR:',self.activeWay)


    #Klasör ağacından itemChanged olayı yapılınca
    def fillFileList(self):
        print('Klasör ağacından bir seçim yapıldı')
        ai=self.treeWidget.currentItem()#seçili item
        self.activeFolderContent=os.listdir(self.activeWay)#Aktif dizindeki dosyaları listele
        if ai==self.goUpTtreeWidget:
            print('^Yukarı itemi seçildi...........')
            '''
            if len(self.activeWayFolderList)<2:
                print('Köke ulaşıldığından bir şey yapılmadı...')
            else:#Dizin listesinde disten başka klasörler de var.

                self.activeWayFolderList.pop(len(self.activeWayFolderList)-1)#Son elemanı listeden çıkar
                print('Son klasör adı listeden çıkarıldı')
                self.treeWidget.clear()
                self.fillFolderTreeWidget()#Klasör listesini de güncelle
                self.treeWidget.expandAll() #ağacı genişlet
                '''
        elif ai==self.rootTreeWidget:
            print('Seçim ağaç köküne taşındı. Hiç bir işlem yapma')
        else:
            print('Tıklanan klasör actveWay listesine eklenebilir. Kontrol')
            self.activeFolderContent=os.listdir(self.activeWay+'/'+ai.text(0))#Aktif dizindeki dosyaları listele
            self.listWidget2.clear()
            for folName in self.activeFolderContent:
                if not (((self.treeWidget.currentItem()==self.goUpTtreeWidget)or(self.treeWidget.currentItem()==self.rootTreeWidget))):
                    self.listWidget2.addItem(folName)
                    print('sağ listeye eklendi')
            print('Ağaçtaki aktif index:',ai.text(0))
        '''

        activeDirectoryListLastElement=self.activeWayFolderList.__getitem__(len(self.activeWayFolderList)-1)
        print('SON ELEMAN:',activeDirectoryListLastElement)
        if self.activeWayFolderList.__contains__(self.treeWidget.currentItem()):
            print('Atif dizin listesinin son elemanı listenin sonunda yer alıyor. Öyleyse silinmeli')
            #self.activeWayFolderList
        else:
            self.activeWayFolderList.append(self.treeWidget.currentIndex())
            print('Atif dizin listesinin son elemanı içermiyor eklendi')

            '''

    #O anki aktif yolu oluşturu
    def createActiveWay(self):
        way=''#Kök dizin için ilk sembol eklendi
        for foldname in self.activeWayFolderList:
            way=way+foldname+'/'
            print('yol eklenen klasörler: ',foldname)
        way=way[0:(len(way)-1)]#En son eklenen / işaretini silmek için parçasını al
        self.activeWay=way
        print('Aktif yol güncellendi: ',way)


    def treeDoubleClicked(self):
        print('Ağaca çift tıklandı')
        ai=self.treeWidget.currentItem()# ağaçtan seçili item#Çi
        if (self.treeWidget.currentItem()==self.goUpTtreeWidget):#Çift tıklanan item Yukarı özelliği ise
            if len(self.activeWayFolderList)>1:
                self.activeWayFolderList.pop(len(self.activeWayFolderList)-1)#Son elemanı listeden çıkar
                print('Son klasör adı listeden çıkarıldı')
                self.treeWidget.clear()
                self.fillFolderTreeWidget()#Klasör listesini de güncelle
                self.treeWidget.expandAll() #ağacı genişlet
            else:
                print('Kök dizine ulaşıdı yukarı çıkılmaz...')
        elif(self.treeWidget.currentItem()==self.rootTreeWidget):
            print('Ağaç köküne tıklandı birşey yapma')
        else:
            self.activeWayFolderList.append(ai.text(0))
            self.treeWidget.clear()
            self.fillFolderTreeWidget()#Disk listesine tıklandığında Klasör listesini de güncelle
            self.treeWidget.expandAll()
            '''

        if not (((self.treeWidget.currentItem()==self.goUpTtreeWidget)or(self.treeWidget.currentItem()==self.rootTreeWidget))):
            print('Eklenecek alt klasör:',ai.text(0))
            '''

#KULLANILMAYAN METOD TANIMLARI

    def onRightClick(self):
        print('fff')


#Sağ liste için sağ klik menüleri
    def listItemRightClicked(self, QPos):
        self.listMenu= QtGui.QMenu()
        menu_item = self.listMenu.addAction("Remove Item")
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
        parentPosition = self.listWidget_extractedmeters.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show()

    def menuItemClicked(self):
        currentItemName=str(self.listWidget_extractedmeters.currentItem().text() )
        print(currentItemName)


