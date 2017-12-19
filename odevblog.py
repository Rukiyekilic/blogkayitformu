from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from PyQt4 import QtGui, QtCore
import sqlite3
import os.path

i=11
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "blogKayitFormu.db")
print (db_path)
class girisEkrani(QtGui.QMainWindow):
    def __init__(self, ebeveyn=None):
        super(girisEkrani, self).__init__(ebeveyn)

        self.widget = QtGui.QWidget(self)
        self.setCentralWidget(self.widget)
        layout = QGridLayout(self.widget)

        # row1
        layout.addWidget(QLabel("Kullanici Adiniz :"), 0, 0)
        self.nick = QLineEdit()
        layout.addWidget(self.nick, 0, 1)

        # row2
        layout.addWidget(QLabel("Parolaniz :"), 1, 0)
        self.psw = QLineEdit()
        self.psw.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.psw, 1, 1)

        # row3
        self.giris = QPushButton("Giris")
        layout.addWidget(self.giris, 2, 0, 2, 2)

        self.widget.setLayout(layout)
        self.setWindowTitle('Giris Paneli')

        self.resize(300, 300)
        self.widget.setLayout(layout)
        self.giris.clicked.connect(self.girisKontrol)

    def girisKontrol(self):

        if self.nick.text() == 'admin' and self.psw.text() == '12345':
            dialog = blogKayitFormu(self)
            self.close()
            dialog.show()

        elif self.nick.text() != 'admin':

            QMessageBox.information(self.widget, 'Dikkat !',
                                    'Lutfen adinizi dogru girdiginizden emin olun.')
            # box.show()
        elif self.psw.text() != '12345':

            QMessageBox.information(self.widget, 'Dikkat !', 'Lutfen parolanizi dogru girdiginizden emin olun.')


class blogKayitFormu(QtGui.QMainWindow):
    def __init__(self, ebeveyn=None):
        super(blogKayitFormu, self).__init__(ebeveyn)
        # bu kisim uygulamanin tasarim kismidir

        self.widget = QtGui.QWidget(self)
        self.setCentralWidget(self.widget)

        grid = QGridLayout()
        grid.addWidget(QLabel('Ad:'), 0, 0)
        self.ad = QLineEdit()
        self.name=self.ad.text()
        grid.addWidget(self.ad, 0, 1, 1, 3)
        grid.addWidget(QLabel('Soyad:'), 1, 0)
        self.soyad = QLineEdit()
        self.surname=self.soyad.text()
        grid.addWidget(self.soyad, 1, 1, 1, 3)
        grid.addWidget(QLabel('Dogum Tarihi:'), 2, 0)
        self.dogumtarihi = QDateEdit(self)
        self.birthDate=self.dogumtarihi.text()
        grid.addWidget(self.dogumtarihi, 2, 1, 1, 3)
        grid.addWidget(QLabel('Cinsiyet:'), 3, 0)
        self.cinsiyetK = QRadioButton('Kadin')
        grid.addWidget(self.cinsiyetK, 3, 1)
        self.cinsiyetE = QRadioButton('Erkek')
        grid.addWidget(self.cinsiyetE, 3, 2)
        self.cinsiyetR = QRadioButton('Rengarenk')
        grid.addWidget(self.cinsiyetR, 3, 3)
        self.choices=[self.cinsiyetK,self.cinsiyetE,self.cinsiyetR]
        grid.addWidget(QLabel('Cep Telefonu:'), 4, 0)
        self.ceptelefonu = QLineEdit()
        self.phone=self.ceptelefonu.text()
        grid.addWidget(self.ceptelefonu, 4, 1, 1, 3)
        grid.addWidget(QLabel('E-Posta:'), 5, 0)
        self.eposta = QLineEdit()
        self.email=self.eposta.text()
        grid.addWidget(self.eposta, 5, 1, 1, 3)
        grid.addWidget(QLabel('Adres:'), 6, 0)
        self.adres = QLineEdit()
        #self.adres.insertPlainText("Lutfen Adresinizi Buraya Giriniz")
        self.address=self.adres.text()
        grid.addWidget(self.adres, 6, 1, 1, 3)
        self.adres.move(20, 20)
        self.adres.resize(50, 50)
        kaydet = QPushButton('Kaydet')
        grid.addWidget(kaydet, 7, 0, 1, 4)
        temizle = QPushButton('Temizle')
        grid.addWidget(temizle, 8, 0, 1, 4)
        self.setLayout(grid)
        self.setWindowTitle('Kayit Formu Penceresi')
        self.resize(600, 600)
        #########################################
        self.connect(kaydet, SIGNAL('pressed()'), self.kaydet)
        self.connect(temizle, SIGNAL('pressed()'), self.temizle)
        self.widget.setLayout(grid)

    def kaydet(self):
        baglanti = sqlite3.connect("blogKayitFormu.db")
        if(baglanti):
            print('Baglanti Basarili!')
        else:
            print('Baglanti Basarisiz!')
        isaretci=baglanti.cursor()
  
        #isaretci.execute("INSERT INTO blogkayitformu (?,?,?,?,?,?,?,?) VALUES(self.ad.text(),,),,,,)")
        #isaretci.execute("INSERT INTO blogkayitformu VALUES (?, ?, ?, ?,?,?,?);", (self.ad.text(), self.soyad.text(), self.dogumtarihi.text(), self.choices,self.ceptelefonu.text(),self.eposta.text(),self.adres.text()))
        isaretci.execute("INSERT INTO blogkayitformu (cep_telefonu,adi,soyadi,adres,eposta,dogum_tarihi) VALUES(?,?,?,?,?,?)",(self.ceptelefonu.text(),self.ad.text(),self.soyad.text(),self.adres.text(),self.eposta.text(),self.dogumtarihi.text()))

      #  sql="INSERT INTO kisiler (ad,soyad,dogumtarihi,cinsiyetK,cinsiyetE,cinsiyetR,ceptelefonu,eposta,adres)"
       # "VALUES (self.ad,selfsoyad,self.dogumtarihi,self.cinsiyetK,self.cinsiyetE,self.cinsiyetR,self.ceptelefonu,self.eposta,self.adres)"
         
        #seÃ§ili olan veritabanÄ±n verileri okuyalÄ±m
        oku = isaretci.execute('SELECT * FROM blogkayitformu')
        print(oku.fetchall())
         
        baglanti.commit()
        baglanti.close()
    def temizle(self):
         self.ad.setText('')
         self.soyad.setText('')
         self.ceptelefonu.setText('')
         self.eposta.setText('')
         self.adres.setPlainText(' ')

def main():
    #uyg = QApplication([])
    uyg = QtGui.QApplication(sys.argv)
    pencere = girisEkrani()
    pencere.show()
    # uyg.exec_()
    sys.exit(uyg.exec_())


if __name__== '__main__':
    main()

