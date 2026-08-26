import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

# ============================================================
# Basic Computer Programming - Student Grade Calculator
# Midterm 50 + Final 50 = Total 100
# Grade: A, B+, B, C+, C, D+, D, F
# ============================================================

APP_TITLE = "Basic Computer Programming | Grade Calculator"
STUDENT_COUNT = 20


def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    return "F"


def validate_score(value):
    if value == "":
        return 0.0
    score = float(value)
    if not 0 <= score <= 50:
        raise ValueError
    return score


class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1180x720")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#f4f7fb")

        self.name_vars = []
        self.mid_vars = []
        self.final_vars = []
        self.total_vars = []
        self.grade_vars = []
        self.row_widgets = []

        self.setup_style()
        self.build_ui()
        self.load_demo_students()

    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            background="white",
            foreground="#1f2937",
            rowheight=38,
            fieldbackground="white",
            font=("Segoe UI", 10)
        )
        style.configure(
            "Treeview.Heading",
            background="#172554",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )
        style.map(
            "Treeview",
            background=[("selected", "#dbeafe")],
            foreground=[("selected", "#111827")]
        )

    def build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#172554", height=100)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Basic Computer Programming",
            bg="#172554",
            fg="white",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(anchor="w", padx=28, pady=(16, 0))

        subtitle = tk.Label(
            header,
            text="Student Grade Calculator  •  Midterm 50 + Final 50",
            bg="#172554",
            fg="#bfdbfe",
            font=("Segoe UI", 10)
        )
        subtitle.pack(anchor="w", padx=30)

        # Main container
        main = tk.Frame(self.root, bg="#f4f7fb")
        main.pack(fill="both", expand=True, padx=22, pady=18)

        # Statistics cards
        cards = tk.Frame(main, bg="#f4f7fb")
        cards.pack(fill="x", pady=(0, 15))

        self.stat_labels = {}
        stats = [
            ("Students", "20"),
            ("Average", "0.00"),
            ("Highest", "0.00"),
            ("Lowest", "0.00"),
            ("Passed", "0")
        ]

        for title, value in stats:
            card = tk.Frame(
                cards, bg="white", highlightbackground="#e5e7eb",
                highlightthickness=1
            )
            card.pack(side="left", fill="x", expand=True, padx=5)

            tk.Label(
                card, text=title, bg="white", fg="#64748b",
                font=("Segoe UI", 9, "bold")
            ).pack(anchor="w", padx=15, pady=(10, 0))

            lbl = tk.Label(
                card, text=value, bg="white", fg="#172554",
                font=("Segoe UI", 17, "bold")
            )
            lbl.pack(anchor="w", padx=15, pady=(0, 10))
            self.stat_labels[title] = lbl

        # Toolbar
        toolbar = tk.Frame(main, bg="#f4f7fb")
        toolbar.pack(fill="x", pady=(0, 10))

        tk.Label(
            toolbar,
            text="Student Scores",
            bg="#f4f7fb",
            fg="#111827",
            font=("Segoe UI", 14, "bold")
        ).pack(side="left")

        button_frame = tk.Frame(toolbar, bg="#f4f7fb")
        button_frame.pack(side="right")

        self.make_button(button_frame, "Calculate Grades", "#2563eb",
                         self.calculate_all).pack(side="left", padx=4)
        self.make_button(button_frame, "Clear Scores", "#64748b",
                         self.clear_scores).pack(side="left", padx=4)
        self.make_button(button_frame, "Save CSV", "#059669",
                         self.save_csv).pack(side="left", padx=4)

        # Table
        table_frame = tk.Frame(
            main, bg="white", highlightbackground="#e5e7eb",
            highlightthickness=1
        )
        table_frame.pack(fill="both", expand=True)

        columns = ("no", "name", "mid", "final", "total", "grade")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=20
        )

        headings = {
            "no": "No.",
            "name": "Student Name",
            "mid": "Midterm / 50",
            "final": "Final / 50",
            "total": "Total / 100",
            "grade": "Grade"
        }

        widths = {
            "no": 60,
            "name": 360,
            "mid": 150,
            "final": 150,
            "total": 150,
            "grade": 110
        }

        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(
                col,
                width=widths[col],
                anchor="center" if col != "name" else "w"
            )

        # Scrollbars
        y_scroll = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=y_scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        y_scroll.pack(side="right", fill="y")

        # Editable input panel
        input_panel = tk.Frame(main, bg="#f4f7fb")
        input_panel.pack(fill="x", pady=(12, 0))

        tk.Label(
            input_panel,
            text="Tip: Double-click a student's name or score in the table to edit.",
            bg="#f4f7fb",
            fg="#64748b",
            font=("Segoe UI", 9)
        ).pack(side="left")

        self.tree.bind("<Double-1>", self.edit_cell)

        # Footer
        footer = tk.Label(
            self.root,
            text="Grade criteria: A ≥80 | B+ 75–79 | B 70–74 | C+ 65–69 | "
                 "C 60–64 | D+ 55–59 | D 50–54 | F <50",
            bg="#e2e8f0",
            fg="#475569",
            font=("Segoe UI", 9),
            pady=7
        )
        footer.pack(fill="x")

    def make_button(self, parent, text, bg, command):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg="white",
            activebackground=bg,
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            padx=14,
            pady=8,
            cursor="hand2",
            font=("Segoe UI", 9, "bold")
        )

    def load_demo_students(self):
        names = [
            "Student 01", "Student 02", "Student 03", "Student 04",
            "Student 05", "Student 06", "Student 07", "Student 08",
            "Student 09", "Student 10", "Student 11", "Student 12",
            "Student 13", "Student 14", "Student 15", "Student 16",
            "Student 17", "Student 18", "Student 19", "Student 20"
        ]

        for i, name in enumerate(names, start=1):
            self.tree.insert(
                "",
                "end",
                iid=str(i),
                values=(i, name, "", "", "", "-")
            )

    def edit_cell(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region != "cell":
            return

        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        if not row_id:
            return

        col_index = int(column.replace("#", "")) - 1
        if col_index not in (1, 2, 3):
            return

        x, y, width, height = self.tree.bbox(row_id, column)
        current = self.tree.item(row_id, "values")[col_index]

        entry = tk.Entry(
            self.tree,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        )
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, "" if current in ("-", "") else current)
        entry.select_range(0, tk.END)
        entry.focus()

        def finish_edit(_event=None):
            value = entry.get().strip()

            if col_index in (2, 3):
                if value:
                    try:
                        score = float(value)
                        if not 0 <= score <= 50:
                            raise ValueError
                        value = f"{score:g}"
                    except ValueError:
                        messagebox.showerror(
                            "Invalid Score",
                            "Midterm และ Final ต้องเป็นตัวเลข 0–50"
                        )
                        entry.destroy()
                        return

            values = list(self.tree.item(row_id, "values"))
            values[col_index] = value
            self.tree.item(row_id, values=values)

            if col_index in (2, 3):
                self.calculate_row(row_id)

            entry.destroy()

        entry.bind("<Return>", finish_edit)
        entry.bind("<FocusOut>", finish_edit)
        entry.bind("<Escape>", lambda e: entry.destroy())

    def calculate_row(self, row_id):
        values = list(self.tree.item(row_id, "values"))

        try:
            mid = validate_score(str(values[2]).strip())
            final = validate_score(str(values[3]).strip())
        except ValueError:
            values[4] = ""
            values[5] = "-"
            self.tree.item(row_id, values=values)
            return

        total = mid + final
        grade = get_grade(total)

        values[2] = f"{mid:g}"
        values[3] = f"{final:g}"
        values[4] = f"{total:g}"
        values[5] = grade

        self.tree.item(row_id, values=values)

    def calculate_all(self):
        valid_scores = []

        for row_id in self.tree.get_children():
            values = list(self.tree.item(row_id, "values"))

            try:
                mid = validate_score(str(values[2]).strip())
                final = validate_score(str(values[3]).strip())
            except ValueError:
                messagebox.showerror(
                    "Invalid Score",
                    f"ตรวจสอบคะแนนของ {values[1]}\n"
                    "คะแนน Midterm และ Final ต้องอยู่ระหว่าง 0–50"
                )
                return

            # Require both scores to be entered
            if str(values[2]).strip() == "" or str(values[3]).strip() == "":
                messagebox.showwarning(
                    "Incomplete Data",
                    f"กรุณากรอกคะแนน Midterm และ Final ของ {values[1]} ให้ครบ"
                )
                return

            total = mid + final
            grade = get_grade(total)

            values[2] = f"{mid:g}"
            values[3] = f"{final:g}"
            values[4] = f"{total:g}"
            values[5] = grade

            self.tree.item(row_id, values=values)
            valid_scores.append(total)

        self.update_statistics(valid_scores)
        messagebox.showinfo(
            "Calculation Complete",
            "รวมคะแนนและตัดเกรดนักศึกษา 20 คนเรียบร้อยแล้ว"
        )

    def update_statistics(self, scores):
        if not scores:
            return

        average = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)
        passed = sum(1 for s in scores if s >= 50)

        self.stat_labels["Average"].config(text=f"{average:.2f}")
        self.stat_labels["Highest"].config(text=f"{highest:.2f}")
        self.stat_labels["Lowest"].config(text=f"{lowest:.2f}")
        self.stat_labels["Passed"].config(text=f"{passed}/20")

    def clear_scores(self):
        if not messagebox.askyesno(
            "Confirm",
            "ต้องการล้างคะแนน Midterm, Final, Total และ Grade ใช่หรือไม่?"
        ):
            return

        for row_id in self.tree.get_children():
            values = list(self.tree.item(row_id, "values"))
            values[2:] = ["", "", "", "-"]
            self.tree.item(row_id, values=values)

        self.stat_labels["Average"].config(text="0.00")
        self.stat_labels["Highest"].config(text="0.00")
        self.stat_labels["Lowest"].config(text="0.00")
        self.stat_labels["Passed"].config(text="0")

    def save_csv(self):
        path = filedialog.asksaveasfilename(
            title="Save Grade Report",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")]
        )

        if not path:
            return

        try:
            with open(path, "w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "No.", "Student Name", "Midterm", "Final", "Total", "Grade"
                ])

                for row_id in self.tree.get_children():
                    writer.writerow(self.tree.item(row_id, "values"))

            messagebox.showinfo(
                "Saved",
                f"บันทึกไฟล์เรียบร้อยแล้ว\n{path}"
            )
        except OSError as error:
            messagebox.showerror("Save Error", str(error))


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeApp(root)
    root.mainloop()
