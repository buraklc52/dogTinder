import streamlit as st
import json
from urllib.request import urlopen
import sqlite3
import functions as fn
from datetime import datetime

fn.createTable("favoriler","isim text","cins text","tarih text","durum text")

conn = sqlite3.connect("dogtinder.db")
c = conn.cursor()
c.execute("SELECT * FROM favoriler WHERE durum='pasif'")
step = c.fetchall()
if len(step) == 0:
    sayac = 0
    while sayac < 10:
        sayac = sayac + 1
        resim = fn.randomPhoto()
        fn.insertTable("favoriler",resim[0],resim[1],str(datetime.today()),'pasif')

elif len(step) > 0:
    lucky = step[0]
    st.image(lucky[0])
    yes = st.button("Yes")
    no = st.button("No")
    if yes:
        c.execute("UPDATE favoriler SET durum = 'yes' WHERE isim=?",(lucky[0],))
        conn.commit()
    if no:
        c.execute("UPDATE favoriler SET durum = 'no' WHERE isim=?", (lucky[0],))
        conn.commit()
