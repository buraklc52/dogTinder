import json
from urllib.request import urlopen
import sqlite3
import random

def randomPhoto():
  veri = json.load(urlopen("https://dog.ceo/api/breeds/image/random"))
  resim = veri['message']
  cins = resim.split("/")[-2]
  return (resim,cins)

def randomText():
  liste = [
      "1.90 Altı Yazmasın",
      "Evliler X",
      "Fakirler X",
      "Amacına Uygun Kullanmıyorum",
      "Hayat Okulu",
      "Selam ile Gelme",
      "06AKP1903 # Ankara",
      "52PC7164 # Ordu"
  ]

  bio = random.choice(liste)
  return bio

  #CREATE TABLE IF NOT EXISTS urunler(isim text,soyisim text,yas integer)

def createTable(tabloisim,*sutunlar):
  conn = sqlite3.connect("dogtinder.db")
  c = conn.cursor()
  s = str(sutunlar)
  s = s.replace("'","")
  s = s.replace("\"","")
  komut = f"CREATE TABLE IF NOT EXISTS {tabloisim}{s}"
  c.execute(komut)
  conn.commit()

  #INSTERT INTO urunler VALUES("burak",12)

def insertTable(tabloisim,*data):
    conn = sqlite3.connect("dogtinder.db")
    c = conn.cursor()
    veri = str(data)
    c.execute(f"INSERT INTO {tabloisim} VALUES{veri}")
    conn.commit()

def getTable(tabloisim):
    conn = sqlite3.connect("dogtinder.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {tabloisim}")
    sonuc = c.fetchall()

    return sonuc