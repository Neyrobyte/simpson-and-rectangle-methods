from tkinter import *
import math
import core

# Цвета и шрифты
BG           = "#0d1117"   # основной фон
BG_CARD      = "#171b22"   # фон карточки
BG_INPUT     = "#252a33"   # фон полей ввода
BG_METHOD    = "#252a33"   # фон кнопок метода (неактивный)
ACCENT       = "#0f5144"   # акцент
ACCENT_HOVER = "#0c3e34"   # акцент при наведении
FG           = "#e8e8f0"   # основной текст
FG_DIM       = "#828499"   # второстепенный текст
FG_RESULT    = "#a5f3a0"   # цвет результата
ERROR_FG     = "#f28b82"   # цвет ошибки
BORDER       = "#4e535a"   # граница

FONT_LABEL   = ("Segoe UI", 11)
FONT_MONO    = ("Consolas", 11)
FONT_RESULT  = ("Consolas", 13)


# Разметка окна
root = Tk()
root.title("Криволинейная трапеция")
root.configure(bg=BG)

size_x = 460
size_y = 680
pos_x = int((root.winfo_screenwidth()  - size_x) / 2)
pos_y = int((root.winfo_screenheight() - size_y) / 2)
root.geometry(f"{size_x}x{size_y}+{pos_x}+{pos_y}")
root.resizable(False, False)


# Вспомогательные виджеты
def make_entry(parent, **kw):
    # Универсальный стиль для полей ввода
    return Entry(
        parent,
        bg=BG_INPUT,
        fg=FG,
        insertbackground=ACCENT,
        relief="flat",
        font=FONT_MONO,
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=ACCENT,
        **kw
    )

def section_label(parent, text):
    # Заголовок для секций (пределы, функция, число разбиений, метод)
    return Label(
        parent,
        text=text,
        bg=BG_CARD,
        fg=FG_DIM,
        font=FONT_LABEL,
        anchor="w"
    )

def divider(parent):
    # Разделитель между секциями
    return Frame(
        parent,
        bg=BORDER,
        height=1
    )


# Карточка
card = Frame(
    root,
    bg=BG_CARD,
    bd=0,
    highlightthickness=1,
    highlightbackground=BORDER
)
card.place(
    x=20,
    y=20,
    width=420,
    height=640
)

Label(
    card,
    text="Калькулятор интеграла",
    bg=BG_CARD,
    fg=FG,
    font=("Segoe UI", 12, "bold")
).pack(
    pady=(14, 0)
)

Label(
    card,
    text="Площадь криволинейной трапеции",
    bg=BG_CARD,
    fg=FG_DIM,
    font=FONT_LABEL
).pack(
    pady=(2, 12)
)

divider(card).pack(
    fill="x",
    padx=16
)


# Пределы + функция
limits_frame = Frame(
    card,
    bg=BG_CARD
)
limits_frame.pack(
    fill="x",
    padx=20,
    pady=(14, 0)
)

integral_col = Frame(
    limits_frame,
    bg=BG_CARD
)
integral_col.pack(
    side="left",
    padx=(0, 10)
)

entry_b = make_entry(
    integral_col,
    width=5,
    justify="center"
)
entry_b.pack(
    pady=(0, 2)
)
entry_b.insert(0, "1")

Label(
    integral_col,
    text="∫",
    bg=BG_CARD,
    fg=FG_DIM,
    font=("Georgia", 38)
).pack()

entry_a = make_entry(
    integral_col,
    width=5,
    justify="center"
)
entry_a.pack(
    pady=(2, 0)
)
entry_a.insert(0, "0")

right_col = Frame(
    limits_frame,
    bg=BG_CARD
)
right_col.pack(
    side="left",
    fill="both",
    expand=True
)

section_label(
    right_col,
    "f(x)"
).pack(
    anchor="w",
    pady=(0, 3)
)

entry_func = make_entry(
    right_col,
    width=24
)
entry_func.pack(
    fill="x",
    ipady=5
)
entry_func.insert(0, "x**2")


# Число разбиений
divider(card).pack(
    fill="x",
    padx=16,
    pady=(16, 0)
)

n_frame = Frame(
    card,
    bg=BG_CARD
)
n_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

section_label(
    n_frame,
    "Число разбиений (n)"
).pack(
    anchor="w",
    pady=(0, 4)
)

entry_n = make_entry(
    n_frame,
    width=10,
    justify="center"
)
entry_n.pack(
    anchor="w",
    ipady=4
)
entry_n.insert(0, "1000")


# Выбор метода
divider(card).pack(
    fill="x",
    padx=16
)

method_frame = Frame(
    card,
    bg=BG_CARD
)
method_frame.pack(
    fill="x",
    padx=20,
    pady=12
)

section_label(
    method_frame,
    "Метод вычисления"
).pack(
    anchor="w",
    pady=(0, 8)
)

METHODS = [
    ("Левый прямоугольник",   "left"),
    ("Средний прямоугольник", "mid"),
    ("Правый прямоугольник",  "right"),
    ("Симпсон",               "simpson"),
]

method_var = StringVar(value="mid")
method_btns = {}

row1 = Frame(
    method_frame,
    bg=BG_CARD
)
row1.pack(
    fill="x",
    pady=(0, 4)
)

row2 = Frame(
    method_frame,
    bg=BG_CARD
)
row2.pack(
    fill="x"
)

rows = [row1, row1, row2, row2]

def select_method(key):
    method_var.set(key)
    for k, b in method_btns.items():
        if k == key:
            b.config(
                bg=ACCENT,
                fg="#ffffff"
            )
        else:
            b.config(
                bg=BG_METHOD,
                fg=FG_DIM
            )

for i, (label, key) in enumerate(METHODS):
    b = Button(
        rows[i],
        text=label,
        bg=BG_METHOD,
        fg=FG_DIM,
        activebackground=ACCENT_HOVER,
        activeforeground="#ffffff",
        relief="flat",
        font=("Segoe UI", 9),
        bd=0,
        cursor="hand2",
        pady=6,
        command=lambda k=key: select_method(k)
    )
    b.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 4) if i % 2 == 0 else 0
    )
    method_btns[key] = b

select_method("mid")


# Кнопка "Вычислить"
divider(card).pack(
    fill="x",
    padx=16
)

btn_frame = Frame(
    card,
    bg=BG_CARD
)
btn_frame.pack(
    fill="x",
    padx=20,
    pady=12
)

btn = Button(
    btn_frame,
    text="  Вычислить  ",
    bg=ACCENT,
    fg="#ffffff",
    activebackground=ACCENT_HOVER,
    activeforeground="#ffffff",
    relief="flat",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    cursor="hand2",
    pady=8
)
btn.pack(
    fill="x"
)


# Результат
divider(card).pack(
    fill="x",
    padx=16
)

res_frame = Frame(
    card,
    bg=BG_CARD
)
res_frame.pack(
    fill="x",
    padx=20,
    pady=(10, 0)
)

section_label(
    res_frame,
    "Результат"
).pack(
    anchor="w",
    pady=(0, 6)
)

result_var = StringVar(value="—")

result_label = Label(
    res_frame,
    textvariable=result_var,
    bg=BG_INPUT,
    fg=FG_RESULT,
    font=FONT_RESULT,
    anchor="center",
    pady=10,
    highlightthickness=1,
    highlightbackground=BORDER,
    relief="flat",
    wraplength=360
)
result_label.pack(
    fill="x"
)


# Логика
_MATH_NS = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}

CORE_METHODS = {
    "left":    core.rectangle_left,
    "mid":     core.rectangle_mid,
    "right":   core.rectangle_right,
    "simpson": core.simpson,
}

def build_func(expr: str):
    code = compile(expr, "<f(x)>", "eval")
    def f(x):
        return eval(
            code,
            {"__builtins__": {}},
            {**_MATH_NS, "x": x}
        )
    return f

def calculate():
    result_label.config(
        fg=FG_RESULT
    )
    try:
        a      = float(entry_a.get())
        b      = float(entry_b.get())
        n      = int(entry_n.get())
        expr   = entry_func.get().strip()
        method = method_var.get()

        if n <= 0:
            raise ValueError("n должно быть положительным")

        f     = build_func(expr)
        value = CORE_METHODS[method](f, a, b, n)
        result_var.set(f"{value:.10g}")
    except Exception as ex:
        result_label.config(
            fg=ERROR_FG
        )
        result_var.set(f"Ошибка: {ex}")


btn.config(
    command=calculate
)

root.bind(
    "<Return>",
    lambda _: calculate()
)


root.mainloop()