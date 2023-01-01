import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Adventure Game")
        self.geometry("700x600")

        # Add a welcome label
        self.welcome_label = tk.Label(self, text="Welcome! Let's go on an adventure.", font=("Helvetica", 16))
        self.welcome_label.pack(side="top", fill="x", pady=10)

        # Add an image
        self.image = Image.open("welcome.jpg")
        self.image = self.image.resize((600, 400), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.image = self.image
        self.image_label.pack()

        # Add a start button
        self.start_button = tk.Button(self, text="START!", command=self.start_adventure)
        self.start_button.pack(pady=10)

    def start_adventure(self):
        # Remove the welcome label and start button
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        # Update the image
        self.image = Image.open("park.jpg")
        self.image = self.image.resize((600, 400), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.image)
        self.image_label.image = self.image

        # Add the new text and buttons
        self.text_label = tk.Label(self, text="On a cloudy day, you took your puppy to the park. You were playing fetch with your puppy, suddenly your puppy ran into the distance. You chased your puppy, puppy ran into a mysterious palace in the distance. You ran to the mysterious palace, You are standing in front of the door.", font=("Helvetica", 16), wraplength=550)
        self.text_label.pack(side="top", fill="x", pady=10)
        self.yes_button = tk.Button(self, text="Yes", command=self.enter_palace)
        self.yes_button.pack(side="left", padx=10)
        self.no_button = tk.Button(self, text="No", command=self.welcome_screen)
        self.no_button.pack(side="left", padx=10)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side="left", padx=10)

    def enter_palace(self):
        # This function will be called when the Yes button is clicked
        pass

    def welcome_screen(self):
        # Remove the text and buttons
        self.text_label.pack_forget()
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.quit_button.pack_forget()

        # Show the welcome label and start button again
        self.welcome_label.pack(side="top", fill="x", pady=10)
        self.start_button.pack(pady=10)

if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()