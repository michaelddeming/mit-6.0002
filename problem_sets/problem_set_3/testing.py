
from ps3 import RectangularRoom
from ps3 import Position


pos = Position(0,6)

room = RectangularRoom(
    width=5, # cols
    height=5, # rows
    dirt_amount=1
)

# print(room.get_num_cleaned_tiles())
# room.room[0][0] = 0
# print(room.get_num_cleaned_tiles())
# room.room[0][1] = 0
# print(room.get_num_cleaned_tiles())

# print(room.is_position_in_room(pos=pos))

print(room.get_dirt_amount(0,0))