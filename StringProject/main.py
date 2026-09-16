import tkinter as tk
from tkinter import messagebox

from function1 import find_text
from function2 import count_text
from function3 import replace_text
from function4 import uppercase_text
from function5 import lowercase_text
from function6 import capitalize_text
from function7 import reverse_text
from function8 import remove_space
from function9 import text_length
from function10 import find_number


# -----------------------------
# สร้างหน้าต่างหลัก
# -----------------------------

root = tk.Tk()
root.title("String Search & Formatter")
root.geometry("850x650")
root.resizable(False, False)

# สี
BG_COLOR = "#f4f6f8"
HEADER_COLOR = "#263238"
BUTTON_COLOR = "#455a64"
TEXT_COLOR = "#263238"

root.configure(bg=BG_COLOR)


# -----------------------------
# หัวข้อโปรแกรม
# -----------------------------

title = tk.Label(
    root,
    text="STRING SEARCH & FORMAT TOOL",
    font=("Arial", 22, "bold"),
    bg=HEADER_COLOR,
    fg="white",
    pady=15
)

title.pack(fill="x")


# -----------------------------
# ช่องใส่ข้อความ
# -----------------------------

input_label = tk.Label(
    root,
    text="ข้อความที่ต้องการประมวลผล",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

input_label.pack(pady=(20, 5))


text_input = tk.Text(
    root,
    height=6,
    width=85,
    font=("Arial", 12)
)

text_input.pack()


# -----------------------------
# ช่อง Keyword
# -----------------------------

keyword_label = tk.Label(
    root,
    text="คำที่ต้องการค้นหา / คำเดิม",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

keyword_label.pack(pady=(15, 5))


keyword_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

keyword_entry.pack()


# -----------------------------
# ช่องคำใหม่สำหรับ Replace
# -----------------------------

new_label = tk.Label(
    root,
    text="คำใหม่สำหรับ Replace",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

new_label.pack(pady=(10, 5))


new_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

new_entry.pack()


# -----------------------------
# ช่องแสดงผล
# -----------------------------

result_label = tk.Label(
    root,
    text="ผลลัพธ์",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

result_label.pack(pady=(15, 5))


result_box = tk.Text(
    root,
    height=5,
    width=85,
    font=("Arial", 12),
    state="disabled"
)

result_box.pack()


# -----------------------------
# ฟังก์ชันแสดงผล
# -----------------------------

def show_result(result):

    result_box.config(state="normal")

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, str(result))

    result_box.config(state="disabled")


# -----------------------------
# ฟังก์ชันดึงข้อความ
# -----------------------------

def get_text():

    return text_input.get("1.0", tk.END).strip()


# -----------------------------
# ปุ่มที่ 1
# ค้นหาคำ
# -----------------------------

def run_find():

    text = get_text()
    keyword = keyword_entry.get()

    if not text or not keyword:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความและคำที่ต้องการค้นหา"
        )
        return

    result = find_text(text, keyword)

    show_result(result)


# -----------------------------
# ปุ่มที่ 2
# นับคำ
# -----------------------------

def run_count():

    text = get_text()
    keyword = keyword_entry.get()

    if not text or not keyword:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความและคำที่ต้องการค้นหา"
        )
        return

    result = count_text(text, keyword)

    show_result(f"พบคำว่า '{keyword}' จำนวน {result} ครั้ง")


# -----------------------------
# ปุ่มที่ 3
# Replace
# -----------------------------

def run_replace():

    text = get_text()
    old_text = keyword_entry.get()
    new_text = new_entry.get()

    if not text or not old_text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความและคำเดิม"
        )
        return

    result = replace_text(text, old_text, new_text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 4
# ตัวพิมพ์ใหญ่
# -----------------------------

def run_uppercase():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = uppercase_text(text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 5
# ตัวพิมพ์เล็ก
# -----------------------------

def run_lowercase():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = lowercase_text(text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 6
# Capitalize
# -----------------------------

def run_capitalize():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = capitalize_text(text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 7
# Reverse
# -----------------------------

def run_reverse():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = reverse_text(text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 8
# ลบช่องว่าง
# -----------------------------

def run_remove_space():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = remove_space(text)

    show_result(result)


# -----------------------------
# ปุ่มที่ 9
# นับตัวอักษร
# -----------------------------

def run_length():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = text_length(text)

    show_result(f"จำนวนตัวอักษรทั้งหมด = {result}")


# -----------------------------
# ปุ่มที่ 10
# ค้นหาตัวเลข
# -----------------------------

def run_number():

    text = get_text()

    if not text:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาใส่ข้อความ"
        )
        return

    result = find_number(text)

    show_result(result)


# -----------------------------
# สร้าง Frame สำหรับปุ่ม
# -----------------------------

button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=20)


# -----------------------------
# สร้างปุ่ม 10 ปุ่ม
# -----------------------------

buttons = [

    ("1. Find Text", run_find),
    ("2. Count Text", run_count),
    ("3. Replace Text", run_replace),
    ("4. Uppercase", run_uppercase),
    ("5. Lowercase", run_lowercase),
    ("6. Capitalize", run_capitalize),
    ("7. Reverse", run_reverse),
    ("8. Remove Space", run_remove_space),
    ("9. Text Length", run_length),
    ("10. Find Number", run_number)

]


for index, (text, command) in enumerate(buttons):

    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        width=18,
        height=2,
        font=("Arial", 10, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        relief="flat",
        cursor="hand2"
    )

    row = index // 5
    column = index % 5

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# -----------------------------
# เริ่มโปรแกรม
# -----------------------------

root.mainloop()