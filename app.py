from tkinter import *
from tkinter import ttk
 
root = Tk()
root.geometry("300x250+400+200")
root.title("ChekNum")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

label = ttk.Label(text="Выберите источник данных:")
label.pack()

btn = ttk.Button(text="Далее")
btn.pack(expand=True)
 
root.mainloop()