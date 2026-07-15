import tkinter as tk

from src.gamepkg.game1 import start_game1
from src.gamepkg.game2 import start_game2


# ---------- สี ----------
BG = "#1f2937"
CARD = "#374151"
BTN = "#2563eb"
BTN_HOVER = "#3b82f6"
TEXT = "white"


root = tk.Tk()
root.title("Mini Game Hub")
root.geometry("700x500")
root.configure(bg=BG)
root.resizable(False, False)


# ---------- Title ----------
title = tk.Label(
    root,
    text="🎮 MINI GAME HUB",
    font=("Arial", 28, "bold"),
    fg="white",
    bg=BG
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Choose a game to play",
    font=("Arial", 13),
    fg="#d1d5db",
    bg=BG
)
subtitle.pack(pady=(0, 20))


# ---------- Card ----------
card = tk.Frame(
    root,
    bg=CARD,
    width=600,
    height=330
)

card.pack()
card.pack_propagate(False)


def hover_in(event):
    event.widget["bg"] = BTN_HOVER


def hover_out(event):
    event.widget["bg"] = BTN


def make_button(text, command):

    btn = tk.Button(
        card,
        text=text,
        command=command,
        font=("Arial", 16, "bold"),
        fg="white",
        bg=BTN,
        activebackground=BTN_HOVER,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=24,
        height=2
    )

    btn.bind("<Enter>", hover_in)
    btn.bind("<Leave>", hover_out)

    return btn


tk.Label(
    card,
    text="Select Your Adventure",
    bg=CARD,
    fg="white",
    font=("Arial", 18, "bold")
).pack(pady=20)


game1_btn = make_button(
    "🚀 Catch The Falling Balls",
    start_game1
)
game1_btn.pack(pady=18)


game2_btn = make_button(
    "🔨 Whack A Mole",
    start_game2
)
game2_btn.pack(pady=18)


footer = tk.Label(
    root,
    text="Version 1.0    |    Tkinter Mini Game Collection",
    bg=BG,
    fg="#9ca3af",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=15)

root.mainloop()