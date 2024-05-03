import tkinter as tk
from PIL import ImageTk

class Character:
    def __init__(self, canvas, x, y, image_path, scale=1):
        self.canvas = canvas
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(scale, scale)  # Réduire la taille de l'image
        self.character = canvas.create_image(x, y, anchor=tk.NW, image=self.image)
        self.x_speed = 0
        self.y_speed = 0

    def move(self):
        self.canvas.move(self.character, self.x_speed, self.y_speed)

class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=1200, height=800)
        self.canvas.pack(expand= yes, fill = both) 

        self.character = Character(self.canvas, 200, 200, "sacha.png", scale= 8)  

        self.master.bind("<KeyPress>", self.key_press)
        self.master.bind("<KeyRelease>", self.key_release)

        self.game_loop()

    def key_press(self, event):
        if event.keysym == "Up":
            self.character.y_speed = -2
        elif event.keysym == "Down":
            self.character.y_speed = 2
        elif event.keysym == "Left":
            self.character.x_speed = -2
        elif event.keysym == "Right":
            self.character.x_speed = 2

    def key_release(self, event):
        if event.keysym in ["Up", "Down"]:
            self.character.y_speed = 0
        elif event.keysym in ["Left", "Right"]:
            self.character.x_speed = 0

    def game_loop(self):
        self.character.move()
        self.master.after(10, self.game_loop)

root = tk.Tk()
game = Game(root)
root.mainloop()

print("Coline")