import tkinter as tk

root = tk.Tk()
root.title("Group 6: Basketball Shooting Simulator")
root.configure(bg="#101B35")

score = 0
x, y = 120, 250
vx, vy = 5, -10
gravity = 0.25
shooting = False

canvas = tk.Canvas(root, width=700, height=350, bg="#F5D7A1")
canvas.pack(padx=10, pady=10)

# Draw court
canvas.create_line(0, 320, 700, 320, fill="white", width=3)

# Draw player
canvas.create_oval(50, 210, 80, 240, fill="#E9B98A")
canvas.create_line(65, 240, 65, 290, fill="navy", width=6)
canvas.create_line(65, 250, 100, 235, fill="navy", width=4)
canvas.create_line(65, 290, 45, 320, fill="navy", width=4)
canvas.create_line(65, 290, 85, 320, fill="navy", width=4)

# Draw hoop and backboard
canvas.create_rectangle(590, 90, 600, 180, fill="white")
canvas.create_line(540, 165, 590, 165, fill="red", width=5)
canvas.create_line(545, 167, 555, 190, fill="white", width=2)
canvas.create_line(585, 167, 575, 190, fill="white", width=2)
canvas.create_line(555, 190, 575, 190, fill="white", width=2)

# Draw basketball
ball = canvas.create_oval(108, 238, 132, 262,
                          fill="#F28C28", outline="black")

score_label = tk.Label(root, text="Score: 0",
                       bg="#101B35", fg="white",
                       font=("Arial", 14, "bold"))
score_label.pack()

def shoot():
    global x, y, vx, vy, shooting
    if shooting:
        return
    x, y = 120, 250
    vx, vy = 5, -12
    shooting = True
    animate()

def animate():
    global x, y, vy, score, shooting

    old_y = y
    x += vx                 # Horizontal movement
    y += vy                 # Vertical movement
    vy += gravity           # Gravity creates the arc

    canvas.coords(ball, x-12, y-12, x+12, y+12)

    # Collision detection: ball enters the basket
    if old_y < 165 <= y and vy > 0 and 552 <= x <= 578:
        score += 1
        score_label.config(text=f"Score: {score}")
        shooting = False
        return

    if x < 700 and y < 350:
        root.after(20, animate)
    else:
        shooting = False

tk.Button(root, text="SHOOT", command=shoot,
          bg="#FFD447", fg="#101B35",
          font=("Arial", 12, "bold")).pack(pady=8)

root.mainloop()