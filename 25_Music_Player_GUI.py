import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Müzik çalar penceresini oluştur
music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")

# Müzik dosyalarının bulunduğu dizini seç
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# Şarkıları listelemek için bir Liste Kutusu oluştur
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    play_list.insert(tkr.END, item)

# Pygame ve ses çalma özelliklerini başlat
pygame.init()
pygame.mixer.init()

# Şarkı çalma, durdurma, duraklat ve devam ettirme işlevlerini tanımla
def play():
    selected_song = play_list.get(tkr.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# Müziğin başlığını göstermek için bir Etiket oluştur
var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

# Butonları oluştur ve düzenle
Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

# Widget'ları yerleştir
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

# Müzik çalar uygulamasını başlat
music_player.mainloop()