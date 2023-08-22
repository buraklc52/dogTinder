import random
import streamlit as st
import functions as fn
import sqlite3
from datetime import datetime

fn.createTable("chat","id INTEGER","mesaj text","tarih text")

conn = sqlite3.connect("dogtinder.db")
c = conn.cursor()
c.execute("SELECT *,rowid FROM favoriler WHERE durum = 'yes'")
favoriler = c.fetchall()
favoriler.reverse()
for fav in favoriler:
    st.sidebar.image(fav[0])

liste = []
for fav in favoriler:
    liste.append(f"{fav[1]} {fav[4]}")

secim = st.selectbox("Köpek Seç",liste)

dogid = int(secim.split(" ")[-1])
c.execute("SELECT isim FROM favoriler WHERE rowid=?",(dogid,))
sonuc = c.fetchone()

col5,col6, = st.columns(2)
with col5:
    st.image(sonuc[0])
with col6:
    sil = st.button("Eşleşmeyi Kaldır")
    if sil:
        c.execute("DELETE FROM favoriler WHERE rowid=?", (dogid,))
        conn.commit()


c.execute("SELECT * FROM chat WHERE id=?",(dogid,))
mesajlar = c.fetchall()

for msj in mesajlar:
    randommsj = random.choice(["Hayır", "Salak", "Defol", "hmm", "Tamam", "Sen?"])
    col1,col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.warning(msj[1])
    col3,col4 = st.columns(2)
    with col3:
        st.info(randommsj)
    with col4:
        pass

col1,col2,col3,col4 = st.columns(4)
with col1:
    alev = st.button("🔥")
    if alev:
        fn.insertTable("chat", dogid, "🔥", str(datetime.now()))
with col2:
    cicek = st.button("🌹")
    if cicek:
        fn.insertTable("chat", dogid, "🌹", str(datetime.now()))
with col3:
    kalp = st.button("❤️")
    if kalp:
        fn.insertTable("chat", dogid, "❤️", str(datetime.now()))
with col4:
    pistol = st.button("🔫")
    if pistol:
        fn.insertTable("chat", dogid , "🔫" , str(datetime.now()))


mesaj = st.text_area(f"{secim} İlgi çekici birşeyler yaz...")
gonder = st.button("Gönder")
if gonder:
    fn.insertTable("chat",dogid,mesaj,str(datetime.now()))

