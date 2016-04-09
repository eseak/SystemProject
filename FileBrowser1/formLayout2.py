# -*- coding: utf-8 -*-
#__author__ = 'Ese'
# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psutil,os
from PyQt5.QtGui import QKeySequence
import shutil

from PyQt5.QtWidgets import (QAction,QFileDialog)

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

        #   DEĞİKENLERE VARSAYILAN DEĞERLERİ ATAMA
        self.setDiskList()
        self.fillDiskListBox()
        self.activeWayFolderList=[]
        self.activeWayFolderList.append(self.diskList.__getitem__(0))
        self.activeWay=self.diskList.__getitem__(0)
        self.outputZipFileWay=os.getcwd()        #Varsayılan çıkı olarak aktif dizini ata
        self.outputZipFileName='MyZippedFile'#Varsayılan çıkı dosya adı
        self.ListWidget2SelectedFileNames=[]#Dizinden seçielen dosyaların listesi
        self.targetZipFormat='zip'#Varsayılan çıkış dosya formatı
        # print('BAŞLANGIÇTA ATANAN YOL, EN KÜÇÜK İNDİSLİ DİSK:',self.activeWay)

        self.listWidget.currentItemChanged.connect(self.diskFileList)
        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.setMaximumWidth(250)
        self.verticalLayout.addWidget(self.treeWidget)
        self.treeWidget.itemSelectionChanged.connect(self.fillFileList)
        self.treeWidget.itemDoubleClicked.connect(self.treeDoubleClicked)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget2.setObjectName("listWidget2")
        self.listWidget2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection) #Liste kutusunu çoklu seçime olarak ayarla
        self.listWidget2.itemDoubleClicked.connect(self.onRightClick)#Şuan kullanılmıyor.
        self.horizontalLayout.addWidget(self.listWidget2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 25))
        self.menubar.setObjectName("menubar")
#SONRDAN EKLENEN MENÜ KODU
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        MainWindow.setMenuBar(self.menubar)
        self.actionSe_ili_Dosyalar_S_k_t_r = QtWidgets.QAction(MainWindow)
        self.actionSe_ili_Dosyalar_S_k_t_r.setObjectName("actionSe_ili_Dosyalar_S_k_t_r")
        self.actionSe_ili_Dosyalar_S_k_t_r_ve_ifrele = QtWidgets.QAction(MainWindow)
        self.actionSe_ili_Dosyalar_S_k_t_r_ve_ifrele.setObjectName("actionSe_ili_Dosyalar_S_k_t_r_ve_ifrele")
        self.menuDosya.addAction(self.actionSe_ili_Dosyalar_S_k_t_r)
        self.menuDosya.addAction(self.actionSe_ili_Dosyalar_S_k_t_r_ve_ifrele)
        self.actionSe_ili_Dosyalar_S_k_t_r.triggered.connect(self.onZipMenuSelected)
        self.menubar.addAction(self.menuDosya.menuAction())
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('..***********.')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.actionSe_ili_Dosyalar_S_k_t_r.setText(_translate("MainWindow", "Seçili Dosyaları Sıkıştır"))
        self.actionSe_ili_Dosyalar_S_k_t_r_ve_ifrele.setText(_translate("MainWindow", "Seçili Dosyaları Sıkıştır ve Şifrele"))
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

    def fillDiskListBox(self):
        dl=self.getDiskList()
        for diskname in dl:
            self.listWidget.addItem(diskname)
    #***************************************************************

    #Diske tıklandığında çalışan metod
    def diskFileList(self):
        self.treeWidget.clear()    #Sol taraftaki dizin ağacını temizle
        self.selectedDiskName=self.listWidget.currentItem().text()        #DiskLste kurtusunda seçilmiş disk aının değerin,i al
        self.activeWayFolderList.clear()#Aktif dizin silsilesini temizle
        self.activeWayFolderList.append(self.selectedDiskName)        #Seçilen dis adını yol dizinler listesine ekle
        self.fillFolderTreeWidget()#Disk listesine tıklandığında Klasör listesini de güncelle
        self.treeWidget.expandAll()

    #Sol taraftak klasör ağacını dolduran metod: Diske tıklandığında veya Klasör ağcandan double click(hazır değil) yapıldığında çalışır
    def fillFolderTreeWidget(self):
        self.createActiveWay()       #Önce son tıklamaya göre aktif dizini güncelleyelim
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
        self.statusbar.showMessage(self.activeWay)
        print('DİZİN AĞACI DOLDURULDU: YENİ AKTİF YOL YAZILIYOR:',self.activeWay)


    #Klasör ağacından itemChanged olayı yapılınca
    def fillFileList(self):
        print('Klasör ağacından bir seçim yapıldı')
        ai=self.treeWidget.currentItem()#seçili item
        self.activeFolderContent=os.listdir(self.activeWay)#Aktif dizindeki dosyaları listele
        if ai==self.goUpTtreeWidget:
            print('^Yukarı itemi seçildi...........')

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

    #Menüden sıkıştır seçildiğinde
    def onZipMenuSelected(self):
        print('Menüden sıkıştır seçildi...')
        ListWidget2SelectedItems=self.listWidget2.selectedItems()
        #print(type(seciliItems))
        if(len(ListWidget2SelectedItems)>0):
            print('Seçili bir şeyler var...')
            for k in ListWidget2SelectedItems:
                self.ListWidget2SelectedFileNames.append(k.text())
                print(k.text())

            self.outputZipFileWay = str(QFileDialog.getExistingDirectory(self.centralwidget, "Çıkış dosyası için konum seçiniz"))
            if os.path.isdir(self.outputZipFileWay):
                print('Seçilen yol geçerlidir....:',self.outputZipFileWay)
                self.showDialog()
        else:
            print('Seçili item bulunmadı')

    def showDialog(self):
        self.outputZipFileName, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Çıkış dosya adı',  'Dosya adı giriniz:')
        print("is dir sonucu:"+str(os.path.isdir(self.outputZipFileWay+'/'+self.outputZipFileName)))
        if not os.path.isdir(self.outputZipFileWay+'/'+self.outputZipFileName):
            os.mkdir(self.outputZipFileWay+'/'+self.outputZipFileName)
            print('Dizin olmadığında oluşturuldu')

        if ok:
            selectionList = ['zip', 'tar', 'gztar', 'bztar']
            sel = QtWidgets.QInputDialog.getItem(self.centralwidget, 'Çıkış dosya formatı', 'Dosya uzantısı seç:', selectionList, current=0, editable=False)
            if sel[1]:
                self.targetZipFormat = sel[0]
                print('Çıkış dosya formatı:',self.targetZipFormat)

                print(self.outputZipFileName)
                for file in self.ListWidget2SelectedFileNames:
                    print("Ziplenecek:"+file)
                    if os.path.isdir(self.activeWay+'/'+file):
                        print ("Yazdırılacak bir dizindir.")
                        shutil.copytree(self.activeWay+'/'+file,self.outputZipFileWay+'/'+self.outputZipFileName+"/"+file)
                    else:
                        print ("Yazdırılacak bir dosyadır.")
                        shutil.copy(self.activeWay+'/'+file,self.outputZipFileWay+'/'+self.outputZipFileName+'/'+file)
                print("Ziplenecek klasör ve içeriği hazır...")
                print("Sıkıştırma başlıyor...")
                shutil.make_archive(self.outputZipFileWay+'/'+self.outputZipFileName , self.targetZipFormat,self.outputZipFileWay+'/'+self.outputZipFileName)
                print("Sıkıştırma tamamlandı...")
                print("Geçici dosyalar siliniyor...")
                shutil.rmtree(self.outputZipFileWay+'/'+self.outputZipFileName )
        #*****************AŞAĞIDAKİ METOD SAĞ LİSTEDE İTEMLERE ÇİFT TIKLANMAI DURUMUNDA*********************
    def onRightClick(self):
        print('Liste 2 ye çift tıklandı...')

