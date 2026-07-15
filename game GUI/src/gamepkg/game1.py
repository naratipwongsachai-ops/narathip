import tkinter as tk
import random

WIDTH = 600
HEIGHT = 500

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20

BALL_SIZE = 20


def start_game1():

    win = tk.Toplevel()
    win.title("Catch The Falling Balls")
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.resizable(False, False)

    canvas = tk.Canvas(
        win,
        width=WIDTH,
        height=HEIGHT,
        bg="#0f172a",
        highlightthickness=0
    )
    canvas.pack()

    score = 0
    hp = 3
    speed = 5

    score_text = canvas.create_text(
        70,
        20,
        text="Score : 0",
        fill="white",
        font=("Arial",16,"bold")
    )

    hp_text = canvas.create_text(
        520,
        20,
        text="❤❤❤",
        fill="red",
        font=("Arial",16)
    )

    player = canvas.create_rectangle(
        WIDTH//2-50,
        HEIGHT-40,
        WIDTH//2+50,
        HEIGHT-20,
        fill="#3b82f6",
        outline=""
    )

    balls = []

    left = False
    right = False

    def key_press(event):
        nonlocal left,right

        if event.keysym=="Left":
            left=True

        if event.keysym=="Right":
            right=True

    def key_release(event):
        nonlocal left,right

        if event.keysym=="Left":
            left=False

        if event.keysym=="Right":
            right=False

    win.bind("<KeyPress>",key_press)
    win.bind("<KeyRelease>",key_release)

    def spawn_ball():

        x=random.randint(20,WIDTH-20)

        ball=canvas.create_oval(
            x,
            0,
            x+BALL_SIZE,
            BALL_SIZE,
            fill=random.choice([
                "yellow",
                "orange",
                "cyan",
                "lime",
                "pink"
            ]),
            outline=""
        )

        balls.append(ball)

        win.after(700,spawn_ball)

    def update():

        nonlocal score,hp,speed

        x1,y1,x2,y2=canvas.coords(player)

        if left and x1>0:
            canvas.move(player,-8,0)

        if right and x2<WIDTH:
            canvas.move(player,8,0)

        remove=[]

        for ball in balls:

            canvas.move(ball,0,speed)

            bx1,by1,bx2,by2=canvas.coords(ball)

            px1,py1,px2,py2=canvas.coords(player)

            # รับลูกบอล
            if by2>=py1 and bx2>=px1 and bx1<=px2:

                score+=1

                canvas.itemconfig(
                    score_text,
                    text=f"Score : {score}"
                )

                remove.append(ball)

                if score%10==0:
                    speed+=1

            elif by2>HEIGHT:

                hp-=1

                canvas.itemconfig(
                    hp_text,
                    text="❤"*hp
                )

                remove.append(ball)

        for b in remove:

            if b in balls:
                balls.remove(b)

            canvas.delete(b)

        if hp<=0:

            canvas.create_text(
                WIDTH//2,
                HEIGHT//2-20,
                text="GAME OVER",
                fill="red",
                font=("Arial",28,"bold")
            )

            canvas.create_text(
                WIDTH//2,
                HEIGHT//2+20,
                text=f"Final Score : {score}",
                fill="white",
                font=("Arial",18)
            )

            return

        win.after(16,update)

    spawn_ball()
    update()