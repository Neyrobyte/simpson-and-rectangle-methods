from tkinter import *
import core

root = Tk()
root.title("Калькулятор площяди криволинейной трапеции")
# Центрирование и размер
size_x = 400
size_y = 400
pos_x = int((root.winfo_screenwidth() - size_x) / 2)
pos_y = int((root.winfo_screenheight() - size_y) / 2)
root.geometry(f"{size_x}x{size_y}+{pos_x}+{pos_y}")
root.resizable(False, False)
 
in_label = Label(text="Введите значения:")
in_label.pack()
 
root.mainloop()