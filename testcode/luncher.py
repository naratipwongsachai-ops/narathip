import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# -----------------------------
# ฟังก์ชันเปิดไฟล์ Python
# -----------------------------
def run_program(filename):
    try:
        path = os.path.join(os.path.dirname(__file__), filename)
        subprocess.Popen([sys.executable, path])
    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# หน้าต่างหลัก
# -----------------------------
root = tk.Tk()
root.title("Python Program Launcher")
root.geometry("450x450")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="GUI Python Launcher",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

# ปุ่มที่ 1
btn1 = tk.Button(
    root,
    text="Run Program 1",
    font=("Arial", 13, "bold"),
    bg="#ff4d4d",
    fg="white",
    width=25,
    height=2,
    command=lambda: run_program("draw.py")
)
btn1.pack(pady=8)

# ปุ่มที่ 2
btn2 = tk.Button(
    root,
    text="Run Program 2",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    width=25,
    height=2,
    command=lambda: run_program("kich.py")
)
btn2.pack(pady=8)

# ปุ่มที่ 3
btn3 = tk.Button(
    root,
    text="Run Program 3",
    font=("Arial", 13, "bold"),
    bg="#2196F3",
    fg="white",
    width=25,
    height=2,
    command=lambda: run_program("loyoy.py")
)
btn3.pack(pady=8)

# ปุ่มที่ 4
btn4 = tk.Button(
    root,
    text="Run Program 4",
    font=("Arial", 13, "bold"),
    bg="#FF9800",
    fg="white",
    width=25,
    height=2,
    command=lambda: run_program("print1.py")
)
btn4.pack(pady=8)

# ปุ่มที่ 5
btn5 = tk.Button(
    root,
    text="Run Program 5",
    font=("Arial", 13, "bold"),
    bg="#9C27B0",
    fg="white",
    width=25,
    height=2,
    command=lambda: run_program("variable.py")
)
btn5.pack(pady=8)

root.mainloop()