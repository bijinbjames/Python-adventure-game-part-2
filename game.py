
import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("Adventure Game")
        self.geometry("500x500")

        # Add the label with the text "HI! Let's go on an adventure!"
        self.label = tk.Label(self, text="HI! Let's go on an adventure!", font=("Helvetica", 16))
        self.label.pack()

        # Load the JPG image and add it to the window
        self.image = Image.open("adventure.png")
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack()

        # Add the Yes and Exit buttons
        self.yes_button = tk.Button(self, text="Yes", command=self.start_adventure)
        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.yes_button.pack()
        self.exit_button.pack()

        # Add the scroll bar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Initialize the inventory variable
        self.inventory = []

    def start_adventure(self):
    # This function will be called when the Yes button is clicked

    # Remove the image and buttons from the window
        self.label.pack_forget()
        self.image_label.pack_forget()
        self.yes_button.pack_forget()
        self.exit_button.pack_forget()

        # Load the new image and add it to the window
        self.image = Image.open("palace.jpg")
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack()

        # Add the text to the window
        self.text = tk.Label(self, text="You are now in the Great Hall. All you see is a wide open empty hall with a big crystal chandelier hanging from the ceiling. Where do you want to go?", font=("Helvetica", 14), wraplength=400)
        self.text.pack()

        # Add the direction buttons to the window and assign their commands
        self.north_button = tk.Button(self, text="North", command=self.gallery)
        #self.south_button = tk.Button(self, text="South", command=self.entrance)
        #self.east_button = tk.Button(self, text="East", command=self.play_room)
        #self.west_button = tk.Button(self, text="West", command=self.arcade)
        self.north_button.pack()
        #self.south_button.pack()
        #self.east_button.pack()
        #self.west_button.pack()

        # Add the Get Item button to the window and assign its command
        self.get_item_button = tk.Button(self, text="Get Item", command=self.get_item)
        self.get_item_button.pack()

    def get_item(self):
        # This function will be called when the Get Item button is clicked

        # Add the knife to the inventory
        self.inventory.append("knife")

        # Update the text to show that the player has picked up the knife
        self.text.config(text="You have picked up the knife! You can now use it to attack the witch in the gallery.")


    def gallery(self):
    # This function will be called when the North button is clicked

    # Remove the image and buttons from the window
        self.image_label.pack_forget()
        self.text.pack_forget()
        self.north_button.pack_forget()
        self.south_button.pack_forget()
        self.east_button.pack_forget()
        self.west_button.pack_forget()

        # Load the new image and add it to the window
        self.image = Image.open("palace.jpg")
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack()

        # Add the text to the window
        self.text = tk.Label(self, text="You have entered the gallery. You see a bunch of paintings on the wall. You see a witch meditating in the center of the room, She is holding a golden key. KILL THE WITCH, to get access to the golden key.", font=("Helvetica", 14), wraplength=400)
        self.text.pack()

        # Add the Attack! button to the window
        self.attack_button = tk.Button(self, text="Attack!", command=self.attack)
        self.attack_button.pack()



if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()