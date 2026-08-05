import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# Python List & String Learning GUI
# สำหรับใช้สอน + ทดลองโค้ด + แบบทดสอบ
# ============================================================

LESSONS = {
    "STRING": [
        {
            "title": "String 1: การสร้าง String",
            "content": "String คือข้อมูลข้อความที่อยู่ภายในเครื่องหมาย ' ' หรือ \" \".",
            "example": 'text = "Hello Python"\nprint(text)',
            "question": 'ข้อ 1: ข้อใดเป็น String ที่ถูกต้อง?',
            "choices": ['Hello', '"Hello"', '123', '[1, 2, 3]'],
            "answer": 1
        },
        {
            "title": "String 2: การเข้าถึงตัวอักษร",
            "content": "สามารถเข้าถึงตัวอักษรด้วย Index โดยตัวแรกเริ่มที่ตำแหน่ง 0",
            "example": 'text = "Python"\nprint(text[0])\nprint(text[2])',
            "question": 'ข้อ 2: text = "Python" แล้ว text[0] คืออะไร?',
            "choices": ['P', 'y', 'Python', '0'],
            "answer": 0
        },
        {
            "title": "String 3: การตัดข้อความ (Slicing)",
            "content": "Slicing ใช้เลือกช่วงของข้อความ เช่น text[1:4] จะเลือก Index 1 ถึงก่อน Index 4",
            "example": 'text = "Python"\nprint(text[1:4])',
            "question": 'ข้อ 3: "Python"[1:4] ได้ผลลัพธ์ใด?',
            "choices": ['Pyt', 'yth', 'tho', 'Python'],
            "answer": 1
        },
        {
            "title": "String 4: เมธอด String",
            "content": "String มีเมธอดช่วยจัดการข้อความ เช่น upper(), lower(), replace()",
            "example": 'text = "hello"\nprint(text.upper())\nprint(text.replace("h", "H"))',
            "question": 'ข้อ 4: "hello".upper() ได้อะไร?',
            "choices": ['hello', 'HELLO', 'Hello', 'ERROR'],
            "answer": 1
        },
        {
            "title": "String 5: ความยาวและการตรวจสอบข้อความ",
            "content": "ใช้ len() เพื่อหาจำนวนตัวอักษร และใช้ in เพื่อตรวจสอบว่ามีข้อความอยู่หรือไม่",
            "example": 'text = "Python"\nprint(len(text))\nprint("Py" in text)',
            "question": 'ข้อ 5: len("Python") มีค่าเท่าใด?',
            "choices": ['5', '6', '7', '0'],
            "answer": 1
        }
    ],
    "LIST": [
        {
            "title": "List 1: การสร้าง List",
            "content": "List ใช้เก็บข้อมูลหลายค่าไว้ด้วยกัน และเขียนข้อมูลไว้ภายใน [ ]",
            "example": 'fruits = ["apple", "banana", "orange"]\nprint(fruits)',
            "question": 'ข้อ 1: ข้อใดเป็น List ที่ถูกต้อง?',
            "choices": ['"apple", "banana"', '["apple", "banana"]', '{"apple", "banana"}', '"apple"'],
            "answer": 1
        },
        {
            "title": "List 2: การเข้าถึงสมาชิก",
            "content": "สมาชิกใน List เข้าถึงด้วย Index โดยสมาชิกตัวแรกมี Index เป็น 0",
            "example": 'fruits = ["apple", "banana", "orange"]\nprint(fruits[0])',
            "question": 'ข้อ 2: fruits[0] คืออะไร?',
            "choices": ['apple', 'banana', 'orange', '0'],
            "answer": 0
        },
        {
            "title": "List 3: เพิ่มและลบข้อมูล",
            "content": "ใช้ append() เพิ่มข้อมูลท้าย List และ remove() ลบข้อมูลที่ระบุ",
            "example": 'items = ["A", "B"]\nitems.append("C")\nitems.remove("A")\nprint(items)',
            "question": 'ข้อ 3: append("C") ทำหน้าที่อะไร?',
            "choices": ['ลบ C', 'เพิ่ม C ท้าย List', 'แก้ C', 'นับ C'],
            "answer": 1
        },
        {
            "title": "List 4: Slicing และ len()",
            "content": "สามารถเลือกข้อมูลบางส่วนด้วย Slicing และใช้ len() หาจำนวนสมาชิก",
            "example": 'numbers = [10, 20, 30, 40, 50]\nprint(numbers[1:4])\nprint(len(numbers))',
            "question": 'ข้อ 4: len([10, 20, 30]) มีค่าเท่าใด?',
            "choices": ['2', '3', '4', '10'],
            "answer": 1
        },
        {
            "title": "List 5: การวนลูป List",
            "content": "ใช้ for เพื่ออ่านสมาชิกใน List ทีละตัว เหมาะกับการประมวลผลข้อมูลหลายค่า",
            "example": 'colors = ["red", "green", "blue"]\nfor color in colors:\n    print(color)',
            "question": 'ข้อ 5: คำสั่งใดเหมาะสำหรับวนอ่านสมาชิกใน List?',
            "choices": ['for', 'if', 'def', 'import'],
            "answer": 0
        }
    ]
}

class LearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python List & String Learning")
        self.root.geometry("1100x720")
        self.root.minsize(900, 600)

        self.current_type = "STRING"
        self.current_index = 0
        self.score = 0
        self.quiz_index = 0
        self.quiz_answers = []
        self.quiz_mode = False

        self.build_ui()
        self.show_lesson("STRING", 0)

    def build_ui(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except:
            pass

        top = tk.Frame(self.root, bg="#eeeeee", height=58)
        top.pack(fill="x")
        top.pack_propagate(False)

        tk.Label(top, text="Python Learning", font=("Arial", 18, "bold"),
                 bg="#eeeeee").pack(side="left", padx=18)

        self.run_btn = tk.Button(top, text="▶  Run", bg="#08a96b", fg="white",
                                 font=("Arial", 12, "bold"), width=10,
                                 command=self.run_code)
        self.run_btn.pack(side="left", padx=10, pady=10)

        tk.Button(top, text="Reset", font=("Arial", 11),
                  command=self.reset_code).pack(side="left")

        self.status = tk.Label(top, text="STRING", font=("Arial", 11, "bold"),
                               bg="#eeeeee")
        self.status.pack(side="right", padx=20)

        main = tk.PanedWindow(self.root, orient="horizontal", sashwidth=5,
                              bg="#cccccc")
        main.pack(fill="both", expand=True)

        # Left: lessons
        left = tk.Frame(main, bg="#f7f7f7", width=270)
        main.add(left, minsize=230)

        tk.Label(left, text="บทเรียน", font=("Arial", 16, "bold"),
                 bg="#f7f7f7").pack(pady=(12, 5))

        switch = tk.Frame(left, bg="#f7f7f7")
        switch.pack(fill="x", padx=10)

        tk.Button(switch, text="STRING", command=lambda: self.load_type("STRING"),
                  width=10).pack(side="left", padx=3)
        tk.Button(switch, text="LIST", command=lambda: self.load_type("LIST"),
                  width=10).pack(side="left", padx=3)

        self.lesson_frame = tk.Frame(left, bg="#f7f7f7")
        self.lesson_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Button(left, text="📝 เริ่มแบบทดสอบ",
                  bg="#444444", fg="white", font=("Arial", 11, "bold"),
                  command=self.start_quiz).pack(fill="x", padx=12, pady=(0, 12))

        # Right side
        right = tk.Frame(main, bg="white")
        main.add(right, minsize=600)

        self.lesson_title = tk.Label(right, text="", font=("Arial", 17, "bold"),
                                     anchor="w", bg="white")
        self.lesson_title.pack(fill="x", padx=15, pady=(12, 5))

        self.lesson_text = tk.Label(right, text="", font=("Arial", 12),
                                    anchor="w", justify="left", bg="white",
                                    wraplength=750)
        self.lesson_text.pack(fill="x", padx=15, pady=4)

        editor_label = tk.Label(right, text="Code Editor", bg="#333333",
                                fg="white", anchor="w", padx=10)
        editor_label.pack(fill="x", padx=15, pady=(10, 0))

        editor_frame = tk.Frame(right)
        editor_frame.pack(fill="both", expand=True, padx=15)

        self.code = tk.Text(editor_frame, font=("Consolas", 13),
                            undo=True, wrap="none", bg="#ffffff")
        self.code.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(editor_frame, command=self.code.yview)
        scroll.pack(side="right", fill="y")
        self.code.config(yscrollcommand=scroll.set)

        output_label = tk.Label(right, text="Output", bg="black",
                                fg="white", anchor="w", padx=10)
        output_label.pack(fill="x", padx=15, pady=(8, 0))

        self.output = tk.Text(right, height=8, font=("Consolas", 12),
                              bg="black", fg="white", insertbackground="white")
        self.output.pack(fill="x", padx=15, pady=(0, 12))

        self.quiz_panel = None

    def load_type(self, lesson_type):
        self.current_type = lesson_type
        self.current_index = 0
        self.quiz_mode = False
        self.status.config(text=lesson_type)
        self.show_lesson(lesson_type, 0)

    def show_lesson(self, lesson_type, index):
        self.quiz_mode = False
        self.current_type = lesson_type
        self.current_index = index
        data = LESSONS[lesson_type][index]

        for w in self.lesson_frame.winfo_children():
            w.destroy()

        for i, lesson in enumerate(LESSONS[lesson_type]):
            tk.Button(
                self.lesson_frame,
                text=f"{i+1}. {lesson['title'].split(': ', 1)[1]}",
                anchor="w",
                command=lambda i=i: self.show_lesson(lesson_type, i)
            ).pack(fill="x", pady=2)

        self.lesson_title.config(text=data["title"])
        self.lesson_text.config(text=data["content"])
        self.code.delete("1.0", "end")
        self.code.insert("1.0", data["example"])
        self.output.delete("1.0", "end")
        self.output.insert("1.0", "กด ▶ Run เพื่อทดลองโปรแกรม\n")

    def reset_code(self):
        self.show_lesson(self.current_type, self.current_index)

    def run_code(self):
        if self.quiz_mode:
            return

        source = self.code.get("1.0", "end-1c")
        self.output.delete("1.0", "end")

        # จำกัด builtins เพื่อให้ใช้เป็นโปรแกรมสอนพื้นฐาน
        safe_globals = {
            "__builtins__": {
                "print": print,
                "len": len,
                "range": range,
                "str": str,
                "int": int,
                "float": float,
                "list": list,
            }
        }

        import io
        import contextlib

        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                exec(source, safe_globals, {})
            result = buffer.getvalue()
            self.output.insert("1.0", result if result else "รันสำเร็จ (ไม่มีข้อความแสดงผล)")
        except Exception as e:
            self.output.insert("1.0", f"Error: {type(e).__name__}: {e}")

    def start_quiz(self):
        self.quiz_mode = True
        self.quiz_index = 0
        self.score = 0
        self.quiz_answers = []
        self.show_quiz()

    def show_quiz(self):
        # ใช้คำถามรวม 10 ข้อ: String 5 + List 5
        if self.quiz_index >= 10:
            self.finish_quiz()
            return

        if self.quiz_index < 5:
            data = LESSONS["STRING"][self.quiz_index]
            category = "STRING"
            number = self.quiz_index + 1
        else:
            data = LESSONS["LIST"][self.quiz_index - 5]
            category = "LIST"
            number = self.quiz_index - 4

        for w in self.lesson_frame.winfo_children():
            w.destroy()

        self.lesson_title.config(text=f"แบบทดสอบ {category} ข้อ {number}/5")
        self.lesson_text.config(text=data["question"])
        self.code.delete("1.0", "end")
        self.code.insert("1.0", "เลือกคำตอบด้านซ้าย แล้วกดปุ่มด้านล่าง")

        self.output.delete("1.0", "end")
        self.output.insert("1.0", "แบบทดสอบทั้งหมด 10 ข้อ | String 5 ข้อ + List 5 ข้อ")

        for i, choice in enumerate(data["choices"]):
            tk.Button(
                self.lesson_frame,
                text=f"{chr(65+i)}. {choice}",
                anchor="w",
                command=lambda i=i, data=data: self.answer_quiz(i, data)
            ).pack(fill="x", pady=3)

        tk.Button(self.lesson_frame, text="ออกจากแบบทดสอบ",
                  command=lambda: self.show_lesson(self.current_type, self.current_index)
                  ).pack(fill="x", pady=(15, 3))

    def answer_quiz(self, selected, data):
        if selected == data["answer"]:
            self.score += 1
            msg = "✓ ถูกต้อง!"
        else:
            msg = f"✗ ยังไม่ถูก คำตอบคือ {chr(65 + data['answer'])}"

        self.quiz_answers.append(selected)
        self.output.delete("1.0", "end")
        self.output.insert("1.0", msg)
        self.quiz_index += 1
        self.root.after(700, self.show_quiz)

    def finish_quiz(self):
        self.quiz_mode = False
        for w in self.lesson_frame.winfo_children():
            w.destroy()

        percent = self.score * 10
        if percent >= 80:
            level = "ดีมาก"
        elif percent >= 60:
            level = "ผ่าน"
        else:
            level = "ควรทบทวนบทเรียน"

        self.lesson_title.config(text="สรุปผลการทดสอบ")
        self.lesson_text.config(
            text=f"คะแนน {self.score}/10 คะแนน ({percent}%) — {level}"
        )
        self.code.delete("1.0", "end")
        self.code.insert("1.0", "String = 5 ข้อ\nList = 5 ข้อ")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", f"ผลสอบ: {self.score}/10\n{level}")

        tk.Button(self.lesson_frame, text="ทำแบบทดสอบอีกครั้ง",
                  bg="#08a96b", fg="white",
                  command=self.start_quiz).pack(fill="x", pady=5)
        tk.Button(self.lesson_frame, text="กลับไปบทเรียน",
                  command=lambda: self.show_lesson("STRING", 0)
                  ).pack(fill="x", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = LearningApp(root)
    root.mainloop()