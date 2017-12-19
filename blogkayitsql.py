import sqlite3
baglanti = sqlite3.connect('blogKayitFormu.db')
if(baglanti):
    print('Baglanti Baþarýlý!')
else:
    print('Baðlantý Baþarýsýz!')
isaretci=baglanti.cursor()
isaretci.execute('''CREATE TABLE blogkayitformu (id VARCHAR(10) PRIMARY KEY, cep_telefonu VARCHAR(11),
adi VARCHAR(50), soyadi VARCHAR(50),
cinsiyeti VARCHAR(10),adres VARCHAR(70), eposta VARCHAR(50),
dogum_tarihi VARCHAR(25))''')
db=isaretci.execute('SELECT name FROM sqlite_master')
print(db.fetchall())
