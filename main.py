import tkinter as tk
root = tk.Tk()
root.title("My first Canvas")

Canvas = tk.Canvas(root,width = 500,height = 350,bg ="white")
Canvas.pack()
Canvas.create_rectangle(40,40,220,150,fill="coral")
Canvas.create_oval( 280,50,440,190,fill ="light blue")
Canvas.create_line(50,250,500,250,width=4)
Canvas.create_text(275,310,text="Hello Canvas",font=("Arial",20))
root.mainloop()
