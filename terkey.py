#!/usr/bin/env python
import os, sys
from time import sleep

def kntl(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.1 / 2)

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
kntl(f'{a}Buat Munculin Tombol Kanan Kiri Di Termoz')
kntl(f'{b}Silahkan Tunggu...')
kntl(f'{a}Proses..')
sleep(1)
kntl(f'{b}[{c}!{b}]{c} Membuat Direktori Properti Termux..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
kntl(f'{b}[{c}!{b}]{c} Sukses !')
sleep(1)
kntl(f'{b}[{c}!{b}]{c} Membuat File Pengaturan..')
sleep(1)

key = extra-keys = "[['DRAWER','QUOTE','APOSTROPHE','ESC','BKSP','DEL','KEYBOARD'],['{}','-','/','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
kntl(f'{b}[{c}!{b}]{c} Sukses !')
sleep(1)
kntl(f'{b}[{c}!{b}]{c} Setting Up..')
sleep(2)
os.system('termux-reload-settings')
kntl(f'{b}[{c}!{b}]{c} Sukses, silahkan jalankan ulang termux anda !')

# Cuma Recode Punya Si Karjok
