import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("380x580")
root.configure(bg="#1c1c1c")
root.resizable(False, False)

expression = tk.StringVar()

# หน้าจอแสดงผล
display = tk.Entry(
    root,
    textvariable=expression,
    font=("Segoe UI", 28),
    justify="right",
    bg="#1c1c1c",
    fg="white",
    bd=0,
    insertbackground="white"
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew",
             padx=15, pady=20, ipady=20)

# ฟังก์ชัน
def press(value):
    expression.set(expression.get() + value)

def clear():
    expression.set("")

def backspace():
    expression.set(expression.get()[:-1])

def calculate():
    try:
        exp = expression.get().replace("×", "*").replace("÷", "/")
        result = eval(exp)
        expression.set(str(result))
    except:
        expression.set("Error")

# ปุ่ม
buttons = [
    ("C",1,0), ("⌫",1,1), ("(",1,2), (")",1,3),
    ("7",2,0), ("8",2,1), ("9",2,2), ("÷",2,3),
    ("4",3,0), ("5",3,1), ("6",3,2), ("×",3,3),
    ("1",4,0), ("2",4,1), ("3",4,2), ("-",4,3),
    ("0",5,0), (".",5,1), ("=",5,2), ("+",5,3),
]

for text, row, col in buttons:

    if text == "=":
        cmd = calculate
        bg = "#ff9500"
        fg = "white"

    elif text == "C":
        cmd = clear
        bg = "#d4d4d2"
        fg = "black"

    elif text == "⌫":
        cmd = backspace
        bg = "#d4d4d2"
        fg = "black"

    elif text in ["+", "-", "×", "÷"]:
        cmd = lambda t=text: press(t)
        bg = "#ff9500"
        fg = "white"

    else:
        cmd = lambda t=text: press(t)
        bg = "#505050"
        fg = "white"

    button = tk.Button(
        root,
        text=text,
        command=cmd,
        font=("Segoe UI", 20, "bold"),
        bg=bg,
        fg=fg,
        bd=0,
        activebackground="#666",
        activeforeground="white"
    )

    button.grid(row=row, column=col,
                sticky="nsew",
                padx=6,
                pady=6,
                ipadx=10,
                ipady=18)

# ปรับขนาด Grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()