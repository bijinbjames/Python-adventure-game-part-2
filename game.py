import tkinter as tk
from PIL import Image, ImageTk


class Game:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Adventure Game")
        
        # Create the player and the rooms
        self.player = Player()
        self.entrance = Entrance()
        self.gallery = Gallery()
        self.arena = Arena()
        self.throne_room = ThroneRoom()
        self.playroom = Playroom()
        self.chamber = Chamber()
        self.arcade = Arcade()
        self.scullery = Scullery()
        self.dungeon = Dungeon()
        self.undercroft = Undercroft()
        
        # Set the starting location for the player
        self.player.location = self.entrance
        
        # Display the entrance
        self.display_location()
        
    def display_location(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Display the image for the current location
        image = Image.open(self.player.location.image)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.root, image=photo)
        label.image = photo
        label.pack()
        
        # Display the buttons for the available exits
        for direction in self.player.location.exits:
            button = tk.Button(self.root, text=direction, command=lambda d=direction: self.move(d))
            button.pack()
        
        # Display the options for the current location
        for option in self.player.location.options:
            button = tk.Button(self.root, text=option, command=lambda o=option: self.do_option(o))
            button.pack()
    
    def move(self, direction):
        # Update the player's location
        if direction == "North":
            self.player.location = self.player.location.north
        elif direction == "South":
            self.player.location = self.player.location.south
        elif direction == "East":
            self.player.location = self.player.location.east
        elif direction == "West":
            self.player.location = self.player.location.west
        
        # Display the new location
        self.display_location()
    
    def do_option(self, option):
        # Handle the option selected by the player
        if option == "Attack Witch":
            if "Knife" in self.player.inventory:
                # The player has the knife and can defeat the witch
                self.player.location.options.remove("Attack Witch")
                self.player.location.options.append("Take Golden Key")
                self.display_location()
            else:
                # The player does not have the knife and dies
                self.display_death()
        elif option == "Take Knife":
            self.player.inventory.append("Knife")
            self.player.location.options.remove("Take Knife")
        elif option == "Take Golden Key":
            self.player.inventory.append("Golden Key")
            self.player.location.options.remove("Take Golden Key")
            self.display_location()
        elif option == "Open Cell":
            if "Golden Key" in self.player.inventory:
                # The player has the golden key and can open the cell
                self.player.location.options.remove("Open Cell")
                self.player.location.options.append("Take Puppy")
                self.display_location()
            else:
                # The player does not have the key and cannot open the cell
                self.display_failure()
        elif option == "Take Puppy":
            self.display_victory()
    
    def display_death(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Display the death message
        label = tk.Label(self.root, text="You have been killed by the witch. Game over.")
        label.pack()
        
        # Display the play again button
        button = tk.Button(self.root, text="Play Again", command=self.restart)
        button.pack()
    
    def display_failure(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Display the failure message
        label = tk.Label(self.root, text="You do not have the key to open the cell. Try again.")
        label.pack()
        
        # Display the continue button
        button = tk.Button(self.root, text="Continue", command=self.display_location)
        button.pack()
    
    def display_victory(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Display the victory message
        label = tk.Label(self.root, text="You have found the puppy! Congratulations, you have won the game!")
        label.pack()
        
        # Display the play again button
        button = tk.Button(self.root, text="Play Again", command=self.restart)
        button.pack()
    
    def restart(self):
        # Create a new game and start the main loop
        game = Game()
        game.root.mainloop()

class Player:
    def __init__(self):
        self.location = None
        self.inventory = []

class Room:
    def __init__(self, name, image, north=None, south=None, east=None, west=None, options=[]):
        self.name = name
        self.image = image
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.options = options
class Entrance(Room):
    def __init__(self):
        super().__init__(name="Entrance", image="entrance.jpg", north=Gallery())

class Gallery(Room):
    def __init__(self):
        super().__init__(name="Gallery", image="gallery.jpg", south=Entrance(), options=["Attack Witch"])

class Arena(Room):
    def __init__(self):
        super().__init__(name="Arena", image="arena.jpg", east=ThroneRoom())

class ThroneRoom(Room):
    def __init__(self):
        super().__init__(name="Throne Room", image="throne_room.jpg", west=Arena(), south=Playroom())

class Playroom(Room):
    def __init__(self):
        super().__init__(name="Playroom", image="playroom.jpg", north=ThroneRoom(), east=Chamber())

class Chamber(Room):
    def __init__(self):
        super().__init__(name="Chamber", image="chamber.jpg", west=Playroom(), north=Scullery())

class Arcade(Room):
    def __init__(self):
        super().__init__(name="Arcade", image="arcade.jpg", north=Scullery(), south=Dungeon())

class Scullery(Room):
    def __init__(self):
        super().__init__(name="Scullery", image="scullery.jpeg", south=Chamber(), options=["Take Knife"])

class Dungeon(Room):
    def __init__(self):
        super().__init__(name="Dungeon", image="dungeon.jpg", north=Arcade(), south=Undercroft())

class Undercroft(Room):
    def __init__(self):
        super().__init__(name="Undercroft", image="undercroft.jpg", north=Dungeon(), options=["Open Cell"])
        
    @property
    def exits(self):
        # Return the available exits
        exits = []
        if self.north:
            exits.append("North")
        if self.south:
            exits.append("South")
        if self.east:
            exits.append("East")
        if self.west:
            exits.append("West")
        return exits


# Create the game and start the main loop
game = Game()
game.root.mainloop()

