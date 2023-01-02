import tkinter as tk
import datetime

journey = []

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
        super().__init__(name="Entrance", image="entrance.jpg", north=Gallery(), west=Arcade(), east=Playroom(), options=["Go North", "Go West", "Go East"])

class Gallery(Room):
    def __init__(self):
        super().__init__(name="Gallery", image="gallery.jpg", south=Entrance(), west=Arena(), east=ThroneRoom(), options=["Attack Witch", "Go South", "Go West", "Go East"])

class Arena(Room):
    def __init__(self):
        super().__init__(name="Arena", image="arena.jpg", east=Gallery(), options=["Go East"])

class ThroneRoom(Room):
    def __init__(self):
        super().__init__(name="Throne Room", image="throne_room.jpg", west=Gallery(), options=["Go West"])

class Playroom(Room):
    def __init__(self):
        super().__init__(name="Playroom", image="playroom.jpg", west=Entrance(), east=Chamber(), options=["Go West", "Go East"])

class Chamber(Room):
    def __init__(self):
        super().__init__(name="Chamber", image="chamber.jpg", west=Playroom(), options=["Go West"])

class Arcade(Room):
    def __init__(self):
        super().__init__(name="Arcade", image="arcade.jpg", north=Scullery(), south=Dungeon(), west=Entrance(), options=["Go North", "Go South", "Go West"])

class Scullery(Room):
    def __init__(self):
        super().__init__(name="Scullery", image="scullery.jpeg", south=Arcade(), options=["Take Knife", "Go South"])

class Dungeon(Room):
    def __init__(self):
        super().__init__(name="Dungeon", image="dungeon.jpg", north=Arcade(), south=Undercroft(), options=["Go North", "Go South"])

class Undercroft(Room):
   
    def __init__(self):
        super().__init__(name="Undercroft", image="undercroft.jpg", north=Dungeon(), options=["Open Cell", "Go North"])

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []
        self.alive = True
        self.has_puppy = False

class Game:
    def __init__(self):
        # Create the rooms
        entrance = Entrance()
        gallery = Gallery()
        arena = Arena()
        throne_room = ThroneRoom()
        playroom = Playroom()
        chamber = Chamber()
        arcade = Arcade()
        scullery = Scullery()
        dungeon = Dungeon()
        undercroft = Undercroft()

        # Create the player
        player = Player(entrance)

        # Create the root window
        self.root = tk.Tk()
        self.root.title("Adventure Game")
        self.root.geometry("800x600")

        # Create the frames
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack()

        # Create the widgets
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()
        self.text_label = tk.Label(self.text_frame, text="Welcome to the Abandoned Castle! You are searching for your lost puppy. Can you find your way through the castle and rescue your furry friend?", wraplength=750)
        self.text_label.pack()
        self.option_buttons = []

        # Set the current room and update the display
        self.current_room = entrance
        self.player = player
        self.update_display()

    def update_display(self):
        # Update the image
        self.image_label.config(image=self.current_room.image)
                # Update the options
        for button in self.option_buttons:
            button.pack_forget()
        self.option_buttons.clear()
        for option in self.current_room.options:
            button = tk.Button(self.button_frame, text=option, command=lambda option=option: self.do_option(option))
            self.option_buttons.append(button)
            button.pack()

        # Update the text
        self.text_label.config(text=f"You are in the {self.current_room.name}. {self.current_room.description}")

    def do_option(self, option):
        if option == "Go North":
            self.go_north()
        elif option == "Go South":
            self.go_south()
        elif option == "Go East":
            self.go_east()
        elif option == "Go West":
            self.go_west()
        elif option == "Attack Witch":
            self.attack_witch()
        elif option == "Take Knife":
            self.take_knife()
        elif option == "Open Cell":
            self.open_cell()

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

    def attack_witch(self):
        if "Knife" in self.player.inventory:
            self.current_room.options.remove("Attack Witch")
            self.current_room.description = "You have defeated the witch and found the Golden Key!"
            self.player.inventory.append("Golden Key")
            self.update_display()
        else:
            self.text_label.config(text="You don't have a weapon to attack the witch with. You were killed by the witch. Game Over.")
            self.player.alive = False
            self.end_game()

    def take_knife(self):
        self.current_room.options.remove("Take Knife")
        self.current_room.description = "You have taken the Knife."
        self.player.inventory.append("Knife")
        self.update_display()

    def open_cell(self):
        if "Golden Key" in self.player.inventory:
            self.current_room.description = "You have unlocked the cell and rescued your puppy! You win!"
            self.player.has_puppy = True
            self.player.inventory.remove("Golden Key")
            self.update_display()
            self.end_game()
        else:
            self.text_label.config(text="You don't have the Golden Key to unlock the cell. Keep searching for it!")

    def end_game(self):
        for button in self.option_buttons:
            button.pack_forget()
        self.option_buttons.clear()
        if self.player.has_puppy:
            self.text_label.config(text="Congratulations, you have rescued your puppy! You win!")
        elif not self.player.alive:
            self.text_label.config(text="Game Over")
        else:
            self.text_label.config(text="Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.root.mainloop()


# After the game is over, log the journey
if game.player.alive:
    result = "Success"
else:
    result = "Failure"

# Write the journey and result to a log file
with open("journey_log.txt", "a") as log_file:
    log_file.write(f"{datetime.datetime.now()}: Result: {result}\n")
    for room in journey:
        log_file.write(f"{room}\n")