import tkinter as tk

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
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Entrance", image="image/entrance.jpg", north=north, south=south, east=east, west=west)

class Gallery(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Gallery", image="image/gallery.jpg", north=north, south=south, east=east, west=west, options=["Attack Witch"])

class Arena(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Arena", image="image/arena.jpg", north=north, south=south, east=east, west=west)

class ThroneRoom(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Throne Room", image="image/throne_room.jpg", north=north, south=south, east=east, west=west)

class Playroom(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Playroom", image="image/playroom.jpeg", north=north, south=south, east=east, west=west)

class Chamber(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Chamber", image="image/chamber.jpg", north=north, south=south, east=east, west=west)

class Arcade(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Arcade", image="image/arcade.jpg", north=north, south=south, east=east, west=west)

class Scullery(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Scullery", image="image/scullery.jpeg", north=north, south=south, east=east, west=west, options=["Take Knife"])

class Dungeon(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Dungeon", image="image/dungeon.jpg", north=north, south=south, east=east, west=west)

class Undercroft(Room):
    def __init__(self, north=None, south=None, east=None, west=None):
        super().__init__(name="Undercroft", image="image/undercroft.jpeg", north=north, south=south, east=east, west=west, options=["Open Cell"])

class Player:
    def __init__(self):
        self.inventory = []
        self.current_room = None

class Game:
    def __init__(self):
        # Create the Gallery and Entrance objects
        arena = Arena()
        throne_room = ThroneRoom()
        arcade = Arcade()
        playroom = Playroom()
        gallery = Gallery(south=Entrance(), west=arena, east=throne_room)
        entrance = Entrance(north=Gallery(), west=arcade, east=playroom)
        chamber = Chamber(west=playroom)
        scullery = Scullery(south=arcade)
        undercroft = Undercroft(north=dungeon)
        dungeon = Dungeon(north=arcade, south=undercroft)

        # Set up the rest of the game
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.player = Player()
        self.current_room = entrance
        self.player.current_room = self.current_room
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        self.text_label = tk.Label(self.root, text=self.current_room.name)
        self.text_label.pack()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.update_display()

    def update_display(self):
        # Clear the button frame
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Update the text label
        self.text_label.config(text=self.current_room.name)

        # Update the image
        image = tk.PhotoImage(file=self.current_room.image)
        self.image_label.config(image=image)
        self.image_label.image = image

        # Create buttons for each option
        for option in self.current_room.options:
            button = tk.Button(self.button_frame, text=option, command=lambda opt=option: self.do_option(opt))
            button.pack()

        # Create buttons for each direction
        if self.current_room.north:
            button = tk.Button(self.button_frame, text="North", command=self.go_north)
            button.pack()
        if self.current_room.south:
            button = tk.Button(self.button_frame, text="South", command=self.go_south)
            button.pack()
        if self.current_room.east:
            button = tk.Button(self.button_frame, text="East", command=self.go_east)
            button.pack()
        if self.current_room.west:
            button = tk.Button(self.button_frame, text="West", command=self.go_west)
            button.pack()

        def do_option(self, option):
        # Handle the "Attack Witch" option
            if option == "Attack Witch" and "Knife" in self.player.inventory:
                self.current_room.options.remove("Attack Witch")
                self.current_room.options.append("Take Golden Key")
            elif option == "Attack Witch":
                self.text_label.config(text="You were killed by the witch!")
                self.button_frame.destroy()
                self.image_label.destroy()

        # Handle the "Take Knife" option
            elif option == "Take Knife":
                self.player.inventory.append("Knife")

            # Handle the "Take Golden Key" option
            elif option == "Take Golden Key":
                self.player.inventory.append("Golden Key")

            # Handle the "Open Cell" option
            elif option == "Open Cell" and "Golden Key" in self.player.inventory:
                self.text_label.config(text="You found your puppy and won the game!")
                self.button_frame.destroy()
                self.image_label.destroy()
            elif option == "Open Cell":
                self.text_label.config(text="You need the Golden Key to open the cell.")

        # Update the display
        self.update_display()

    def go_north(self):
        self.current_room = self.current_room.north
        self.player.current_room = self.current_room
        self.update_display()

    def go_south(self):
        self.current_room = self.current_room.south
        self.player.current_room = self.current_room
        self.update_display()

    def go_east(self):
        self.current_room = self.current_room.east
        self.player.current_room = self.current_room
        self.update_display()

    def go_west(self):
        self.current_room = self.current_room.west
        self.player.current_room = self.current_room
        self.update_display()

# Create the game and start the main loop
game = Game()
game.root.mainloop()



