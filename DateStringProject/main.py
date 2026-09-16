import tkinter as tk
from tkinter import filedialog, messagebox
import re

# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("Date - String Format Analyzer")
root.geometry("1000x700")
root.minsize(850, 600)

BG_COLOR = "#f4f6f8"
TEXT_COLOR = "#263238"
ACCENT_COLOR = "#607d8b"
WHITE = "#ffffff"

root.configure(bg=BG_COLOR)

title_label = tk.Label(
    root,
    text="Date - String Format Analyzer",
    font=("Segoe UI", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    root,
    text="Text processing with Python re module",
    font=("Segoe UI", 10),
    bg=BG_COLOR,
    fg=ACCENT_COLOR
)
subtitle_label.pack(pady=(0, 15))

input_frame = tk.LabelFrame(
    root,
    text=" Input Text ",
    font=("Segoe UI", 11, "bold"),
    bg=WHITE,
    fg=TEXT_COLOR,
    bd=1,
    relief="solid"
)
input_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)

input_text = tk.Text(
    input_frame,
    height=8,
    font=("Consolas", 11),
    bg=WHITE,
    fg=TEXT_COLOR,
    wrap="word",
    bd=0
)
input_text.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)
# =========================
# Load and Clear
# =========================

def load_text():
    try:
        file_path = filedialog.askopenfilename(
            title="Select Text File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()

            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, data)

    except Exception as error:
        messagebox.showerror("Load Error", str(error))


def clear_text():
    input_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)


button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)
button_frame.pack(fill="x", padx=25, pady=5)

load_button = tk.Button(
    button_frame,
    text="Load Text",
    command=load_text,
    font=("Segoe UI", 10, "bold"),
    bg=ACCENT_COLOR,
    fg=WHITE,
    padx=25,
    pady=8
)
load_button.pack(side="left", padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Segoe UI", 10, "bold"),
    bg="#78909c",
    fg=WHITE,
    padx=25,
    pady=8
)
clear_button.pack(side="left")

result_frame = tk.LabelFrame(
    root,
    text=" Result ",
    font=("Segoe UI", 11, "bold"),
    bg=WHITE,
    fg=TEXT_COLOR,
    bd=1,
    relief="solid"
)
result_frame.pack(fill="both", expand=True, padx=25, pady=10)

result_text = tk.Text(
    result_frame,
    height=8,
    font=("Consolas", 11),
    bg="#f8f9fa",
    fg=TEXT_COLOR,
    bd=0
)
result_text.pack(fill="both", expand=True, padx=10, pady=10)
# =========================
# 10 Regex Functions
# =========================

def find_date_ddmmyyyy(text):
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)


def find_date_yyyymmdd(text):
    return re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)


def find_emails(text):
    return re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)


def find_phone(text):
    return re.findall(r"\b0\d{2}[- ]?\d{3}[- ]?\d{4}\b", text)


def find_numbers(text):
    return re.findall(r"\b\d+\b", text)


def find_urls(text):
    return re.findall(r"https?://[^\s]+", text)


def find_hashtags(text):
    return re.findall(r"#[A-Za-z0-9_ก-๙]+", text)


def find_mentions(text):
    return re.findall(r"@[A-Za-z0-9_ก-๙]+", text)


def find_times(text):
    return re.findall(r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b", text)


def find_decimals(text):
    return re.findall(r"\b\d+\.\d+\b", text)
# =========================
# Result Function
# =========================

def show_result(title, function):
    try:
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            raise ValueError("กรุณาใส่ข้อความก่อนค้นหา")

        results = function(text)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"{title}\n")
        result_text.insert(tk.END, "=" * 40 + "\n\n")
        result_text.insert(tk.END, f"พบทั้งหมด: {len(results)} รายการ\n\n")

        if results:
            for number, item in enumerate(results, 1):
                result_text.insert(tk.END, f"{number}. {item}\n")
        else:
            result_text.insert(tk.END, "ไม่พบข้อมูล")

    except Exception as error:
        messagebox.showerror("Error", str(error))


# =========================
# 10 Search Buttons
# =========================

search_frame = tk.LabelFrame(
    root,
    text=" Search Functions ",
    font=("Segoe UI", 11, "bold"),
    bg=WHITE,
    fg=TEXT_COLOR,
    bd=1,
    relief="solid"
)
search_frame.pack(fill="x", padx=25, pady=8)

buttons = [
    ("Date 1", "DD/MM/YYYY", find_date_ddmmyyyy),
    ("Date 2", "YYYY-MM-DD", find_date_yyyymmdd),
    ("Email", "EMAIL", find_emails),
    ("Phone", "PHONE", find_phone),
    ("Number", "NUMBER", find_numbers),
    ("URL", "URL", find_urls),
    ("Hashtag", "HASHTAG", find_hashtags),
    ("Mention", "MENTION", find_mentions),
    ("Time", "TIME", find_times),
    ("Decimal", "DECIMAL", find_decimals)
]

for button_text, title, function in buttons:
    tk.Button(
        search_frame,
        text=button_text,
        command=lambda t=title, f=function: show_result(t, f),
        font=("Segoe UI", 9, "bold"),
        bg=ACCENT_COLOR,
        fg=WHITE,
        width=10,
        pady=6
    ).pack(side="left", padx=4, pady=8)

info_label = tk.Label(
    root,
    text="Click a button to search the input text",
    font=("Segoe UI", 9),
    bg=BG_COLOR,
    fg=ACCENT_COLOR
)
info_label.pack(pady=(0, 8))

root.mainloop()
