# gui/GUI_HelloWorld.py
# "Hallo Welt" Ausgabe in einem Fenster

from tkinter import *
from tkinter import ttk

mainWin = Tk()

label_1 = ttk.Label(mainWin, text='Hallo Welt')
label_1.grid()

mainWin.mainloop()
