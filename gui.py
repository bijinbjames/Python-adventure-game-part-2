import tkinter as tk

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, location):
        self.location = location

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def go(self, direction):
        if direction == "north":
            self.move(gallery)
        elif direction == "south":
            self.move(arena)
        elif direction == "east":
            self.move(throne_room)
        elif direction == "west":
            self.move(play_room)

class Location:
    def __init__(self, name):
        self.name = name
    

    def look(self):
        if self.name == "Entrance":
            print("You are now in the Great Hall. All you see is a wide open empty hall with a big crystal chandelier hanging from the ceiling. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Gallery":
            print("You are now in the Gallery. There are paintings and sculptures on display all around you. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Arena":
            print("You are now in the Arena. You hear the sound of swords clashing and cheering crowds in the distance. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Throne Room":
            print("You are now in the Throne Room. You see a grand throne at the end of the room, surrounded by guards. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Play Room":
            print("You are now in the Play Room. There are toys and games scattered everywhere. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Chamber":
            print("You are now in the Chamber. It is a small, cozy room with a fireplace. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Arcade":
            print("You are now in the Arcade. There are rows of arcade games flashing and beeping. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Scullery":
            print("You are now in the Scullery. There are pots and pans hanging from the walls and a strong smell of cleaning products. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Dungeon":
            print("You are now in the Dungeon. It is dark and damp, and you hear the sound of dripping water. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")
        elif self.name == "Undercroft":
            print("You are now in the Undercroft. It is a cold, dark storage room. You can go 'north', 'south', 'east', or 'west'. Where do you want to go?")

class Item:
    def __init__(self, name):
        self.name = name

class GameGUI:
    def __init__(self, player):
        self.player = player
        self.window = tk.Tk()
        self.window.title("Game")

        # Create a label to display the player's location
        self.location_label = tk.Label(self.window, text=f"You are in the {player.location.name}")
        self.location_label.pack()

        # Create buttons for the player to move
        self.north_button = tk.Button(self.window, text="North", command=self.go_north)
        self.north_button.pack()
        self.south_button = tk.Button(self.window, text="South", command=self.go_south)
        self.south_button.pack()
        self.east_button = tk.Button(self.window, text="East", command=self.go_east)
        self.east_button.pack()
        self.west_button = tk.Button(self.window, text="West", command=self.go_west)
        self.west_button.pack()

        # Create a label to display the player's inventory
        self.inventory_label = tk.Label(self.window, text=f"Inventory: {self.format_inventory()}")
        self.inventory_label.pack()

        # Create buttons for the player to interact with items
        self.pickup_button = tk.Button(self.window, text="Pick up", command=self.pickup)
        self.pickup_button.pack()
        self.drop_button = tk.Button(self.window, text="Drop", command=self.drop)
        self.drop_button.pack()

        # Start the tkinter event loop
        self.window.mainloop()

    def go_north(self):
        self.player.go("north")
        self.location_label.config(text=f"You are in the {self.player.location.name}")

    def go_south(self):
        self.player.go("south")
        self.location_label.config(text=f"You are in the {self.player.location.name}")

    def go_east(self):
        self.player.go("east")
        self.location_label.config(text=f"You are in the {self.player.location.name}")

    def go_west(self):
        self.player.go("west")
        self.location_label.config(text=f"You are in the {self.player.location.name}")

    def pickup(self):
        # Check if there is an item at the player's location
        if self.player.location.item is not None:
            self.player.pickup(self.player.location.item)
            self.player.location.item = None
            self.inventory_label.config(text=f"Inventory: {self.format_inventory()}")
        else:
            print("There is no item to pick up.")

    def drop(self):
        # Check if the player has an item to drop
        if  len(self.player.inventory) > 0:
            self.player.location.item = self.player.inventory[0]
            self.player.drop(self.player.inventory[0])
            self.inventory_label.config(text=f"Inventory: {self.format_inventory()}")
        else:
            print("You don't have any items to drop.")

    def format_inventory(self):
        # Format the player's inventory as a string
        if  len(self.player.inventory) > 0:
            inventory_string = ", ".join([item.name for item in self.player.inventory])
            return inventory_string
        else:
            return "Empty"

# Create some locations
entrance = Location("Entrance")
gallery = Location("Gallery")
arena = Location("Arena")
throne_room = Location("Throne Room")
play_room = Location("Play Room")
chamber = Location("Chamber")
arcade = Location("Arcade")
scullery = Location("Scullery")
dungeon = Location("Dungeon")
undercroft = Location("Undercroft")

# Create some items
golden_key = Item("Golden Key")
flashlight = Item("Flashlight")

# Create a player
player = Player("Alice", entrance)

# Create the GUI
gui = GameGUI(player)
