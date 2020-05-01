from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''
        Room.objects.all().delete()
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 1
        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west
        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:
            print("room count", room_count)
            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1
            # Create a room in the given direction
            room_names = ["Grim Best Ritual Vault",
                          "Ill Long Magic Cell", "Many Dead Mind Court"]
            room_descriptions = [
                "as you go into the room with the spell. Only creatures capable of sleeping are affected. They awake as normal: loud noises, jolts, pain.  5th", "as you go into the room kill or take damage the spell ends.  Sleep Level 3 Enchantment  Description  1d4 enemies you can see of the GM", "as you go into the room with the spell and ask the GM any three questions.  Sleep Level 3 Enchantment  Description  1d4 enemies you can", "as you go into the room kill or maim. The GM will tell you what kind of creature it is and how you must counter it to exceed your own damage counter.", ]

            # Room name
            room_name = random.choice(room_names)
            # Room Description
            room_description = random.choice(room_descriptions)

            room = Room(title=f"{room_name}",
                        description=f"{room_description}", x=x, y=y)
            room.save()
            for attr, value in room.__dict__.items():
                print(attr, value)
            # Note that in Django, you'll need to save the room after you create it
            # Save the room in the World grid
            self.grid[y][x] = room
            # Connect the new room to the previous room
            if previous_room is not None:
                if room_direction not in reverse_dirs:
                    print("Invalid direction")
                    continue
                reverse_dir = reverse_dirs[room_direction]
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_dir)
            # Update iteration variables
            previous_room = room
            room_count += 1

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
# The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
# Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"
# Print string
        print(str)


world = World()
number_of_rooms = 100
width = 10
height = 10
world.generate_rooms(width, height, number_of_rooms)
world.print_rooms()
print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {number_of_rooms}\n")
