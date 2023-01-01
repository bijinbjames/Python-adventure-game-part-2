import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Adventure Game")
        self.geometry("700x600")

        # Add a welcome label
        welcome_label = tk.Label(self, text="Welcome! Let's go on an adventure.", font=("Helvetica", 16))
        welcome_label.pack(side="top", fill="x", pady=10)

        # Add an image
        image = Image.open("welcome.jpg")
        image = image.resize((600, 400), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=image)
        image_label.image = image
        image_label.pack()

        # Add a start button
        start_button = tk.Button(self, text="START!", command=self.start_adventure)
        start_button.pack(pady=10)

    def start_adventure(self):
        # This function will be called when the start button is clicked
        pass

if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()