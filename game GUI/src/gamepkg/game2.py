import tkinter as tk
import random

SIZE = 3
TIME_LIMIT = 30


def start_game2():

    win = tk.Toplevel()
    win.title("Whack A Mole")
    win.geometry("500x550")
    win.configure(bg="#1e293b")
    win.resizable(False, False)

    score = 0
    time_left = TIME_LIMIT
    mole = None

    tk.Label(
        win,
        text="🔨 WHACK A MOLE",
        font=("Arial", 22, "bold"),
        bg="#1e293b",
        fg="white"
    ).pack(pady=15)

    info = tk.Frame(win, bg="#1e293b")
    info.pack()

    score_label = tk.Label(
        info,
        text="Score : 0",
        font=("Arial", 15, "bold"),
        bg="#1e293b",
        fg="gold"
    )
    score_label.grid(row=0, column=0, padx=20)

    timer_label = tk.Label(
        info,
        text=f"Time : {TIME_LIMIT}",
        font=("Arial", 15, "bold"),
        bg="#1e293b",
        fg="cyan"
    )
    timer_label.grid(row=0, column=1, padx=20)

    frame = tk.Frame(win, bg="#1e293b")
    frame.pack(pady=20)

    buttons = []

    def hit(index):
        nonlocal score

        if index == mole:
            score += 1
            score_label.config(text=f"Score : {score}")
            move_mole()

    for r in range(SIZE):
        for c in range(SIZE):

            b = tk.Button(
                frame,
                text="",
                width=8,
                height=4,
                font=("Arial", 20),
                bg="#475569",
                fg="white",
                activebackground="#64748b",
                command=lambda i=len(buttons): hit(i)
            )

            b.grid(row=r, column=c, padx=5, pady=5)

            buttons.append(b)

    def move_mole():
        nonlocal mole

        for b in buttons:
            b.config(text="", bg="#475569")

        mole = random.randint(0, 8)

        buttons[mole].config(
            text="🐹",
            bg="#f59e0b"
        )

    def countdown():
        nonlocal time_left

        time_left -= 1

        timer_label.config(
            text=f"Time : {time_left}"
        )

        if time_left <= 0:

            for b in buttons:
                b.config(state="disabled")

            tk.Label(
                win,
                text=f"🎉 GAME OVER\nFinal Score : {score}",
                font=("Arial",18,"bold"),
                bg="#1e293b",
                fg="white"
            ).pack(pady=15)

            return

        move_mole()

        win.after(1000, countdown)

    move_mole()
    win.after(1000, countdown)