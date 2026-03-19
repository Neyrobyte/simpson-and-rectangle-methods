import tkinter as tk
from tkinter import ttk, messagebox
import math
import core

def calc(event=None):
    try:
        func_str = func_var.get()
        a = float(a_var.get())
        b = float(b_var.get())
        n = int(n_var.get())
        if (n <= 0):
            raise ValueError("n должно быть положительным целым числом")
        
        result = core.simpson(lambda x: eval(func_str), a, b, n)
        result_var.set(f"{result:.4f}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")

base_color = "#171719"
alt_color = "#171722"

root = tk.Tk()
root.geometry("600x300")
root.title("Интеграл — приближённое значение")
# 1. Цвет самого окна (будет видно в отступах, если они есть)
root.configure(bg='#2b2b2b') 

style = ttk.Style(root)
try:
    style.theme_use('clam')
except Exception:
    pass
# style.configure('TLabel', font=('Segoe UI', 30))
style.configure('TFrame', background=base_color)
style.configure('TLabel', font=('Segoe UI', 30), background=base_color, foreground='white')
style.configure('TButton', font=('Segoe UI', 30), background=alt_color, foreground='white')
style.configure('TEntry', font=('Segoe UI', 30), background='#330000', foreground='white')

main = ttk.Frame(root, padding=(12, 12, 12, 12), style='TFrame')
main.pack(fill=tk.BOTH, expand=True)

func_var = tk.StringVar(value='math.sin(x)')
a_var = tk.StringVar(value='0')
b_var = tk.StringVar(value='3.14')
n_var = tk.StringVar(value='100')
result_var = tk.StringVar()

# Layout
ttk.Label(main, text='f(x) =').grid(row=0, column=0, sticky=tk.W, pady=4)
entry_func = ttk.Entry(main, textvariable=func_var, width=36)
entry_func.grid(row=0, column=1, columnspan=3, sticky=tk.EW, padx=6)

ttk.Label(main, text='a:').grid(row=1, column=0, sticky=tk.W, pady=4)
entry_a = ttk.Entry(main, textvariable=a_var, width=12)
entry_a.grid(row=1, column=1, sticky=tk.W, padx=6)

ttk.Label(main, text='b:').grid(row=1, column=2, sticky=tk.W, pady=4)
entry_b = ttk.Entry(main, textvariable=b_var, width=12)
entry_b.grid(row=1, column=3, sticky=tk.W, padx=6)

ttk.Label(main, text='n:').grid(row=2, column=0, sticky=tk.W, pady=6)
entry_n = ttk.Entry(main, textvariable=n_var, width=12)
entry_n.grid(row=2, column=1, sticky=tk.W, padx=6)

calc_btn = ttk.Button(main, text='Вычислить', command=calc)
calc_btn.grid(row=2, column=3, sticky=tk.E, padx=6)

sep = ttk.Separator(main, orient='horizontal')
sep.grid(row=3, column=0, columnspan=4, sticky=tk.EW, pady=10)

ttk.Label(main, text='Результат:', font=('Segoe UI', 10)).grid(row=4, column=0, sticky=tk.W)
result_label = ttk.Label(main, textvariable=result_var, font=('Segoe UI', 14, 'bold'))
result_label.grid(row=4, column=1, columnspan=3, sticky=tk.W)

for i in range(4):
    main.columnconfigure(i, weight=1)

entry_func.focus_set()
root.bind('<Return>', calc)

root.resizable(False, False)
root.mainloop()