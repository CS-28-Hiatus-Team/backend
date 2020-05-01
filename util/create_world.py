from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.generator import World
import random

# Room.objects.all().delete()
world = World()
world.generate_rooms(10, 10, 100)

room_descriptions = [
    'This is a generic room',

]


room_tracker = {}

for row in world.grid:
    for rm in row:
        des = random.choice(room_descriptions)
        room = Room(title=f'{rm.name}', description=des)
        room.save()
        room_tracker[(rm.x, rm.y)] = room
        if rm.e_to != None:
            coords = (rm.e_to.x, rm.e_to.y)
            if coords in room_tracker:
                room_tracker[rm.x, rm.y].connect_rooms(
                    room_tracker[coords], 'e')
                room_tracker[coords].connect_rooms(
                    room_tracker[rm.x, rm.y], 'w')
        if rm.w_to != None:
            coords = (rm.w_to.x, rm.w_to.y)
            if coords in room_tracker:
                room_tracker[rm.x, rm.y].connect_rooms(
                    room_tracker[coords], 'w')
                room_tracker[coords].connect_rooms(
                    room_tracker[rm.x, rm.y], 'e')
        if rm.s_to != None:
            coords = (rm.s_to.x, rm.s_to.y)
            if coords in room_tracker:
                room_tracker[rm.x, rm.y].connect_rooms(
                    room_tracker[coords], 's')
                room_tracker[coords].connect_rooms(
                    room_tracker[rm.x, rm.y], 'n')

players = Player.objects.all()
for p in players:
    p.current_room = world.grid[0][0].id
    p.save()
