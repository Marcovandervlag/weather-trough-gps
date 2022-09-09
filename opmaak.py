from tkinter import *


def tekst(temperatuur, CITY, icon):
    kaas = 'Het is momenteel ' + temperatuur + f'°C in {CITY}' + '\n' + icon
    root = Tk()
    root.iconbitmap(default='weather.ico')
    root.geometry("300x64")
    root.title("Het weer door: KoalaTeen ")
    bg = PhotoImage(file="weather.png")
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)
    label2 = Label(root, text=kaas, bg="#458be5")
    label2.pack(pady=4)
    root.after(5000, lambda: root.destroy())
    root.mainloop()
