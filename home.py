import tkinter as tk
root = tk.Tk()
root.title("house")
root.geometry("800x600")

canvas = tk.Canvas(root, width =800,bg ="skyblue")
canvas.pack()
canvas.create_rectangle(0,450,800,600,fill ="pink",outline="black")
root.mainloop()
