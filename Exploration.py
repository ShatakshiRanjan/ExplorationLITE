class room:

    def __init__(self, name):
        self.__exits={}
        self.__name = name
        self.__description = None

    def get_name(self):
        return self.__name
    def set_exits(self, exits):
        self.__exits = exits
    def get_exits(self):
        return self.__exits
    def set_desc(self, desc):
        self.__description = desc
    def get_desc(self):
        return self.__description

class item:
    def __init__(self, name):
        self.__name=name

    def set_items(self, name):
        self.__name = name
    def get_items(self):
        return self.__Name

class backpack:
    def __init__(self, name):
        self.__name = name
    

porch = room("Front Porch")
porch.set_desc("The sun is shining brigthly. The smell of wet grass\
surrounds the colourful, well-kept garden. Regardless, everything seems\
out of place.")
drawing_room = room("Drawing room")
drawing_room.set_desc("The sunlight lights up the dust covered\
interior of the house. Everything seems to been frozen in time,\
seemingly untouched.")
kitchen = room("Kitchen")
kitchen.set_desc("The dishes and utensils are neatly arranged.\
A few withering microgreen plant sits at the window sill.")
hallway = room("Hallway")
hallway.set_desc("Infront of you is a long narrow hallway. Pictures hang\
on both side of the wall covered with a hypnotic vintage wallpaper.")
roomA = room("Bedroom")
roomA.set_desc("A white sheet covers the dust covered bed. The curtains\
flow inwards as a gust of wind flow in through the slightly ajar window.")
basement=room("Basement")
basement.set_desc("A single light flickers from the ceiling. The wall\
infront of you is smeared with a huge text written in a dark red colour.\
It say 'Don't wonder around, it doesn't like intruders.'")
attic=room("Attic")
attic.set_desc("The ceiling here is quite low and dark although a box in\
the middle of the room is dimly lit by light passing through the door.")
bathroom=room("bathroom")
bathroom.set_desc("Drops of water drip from the wash basin's tap. You look\
up, finding your reflection looking back at you.")
roomB=room("Dark Room")
roomB.set_desc("An ominous feeling strikes you. The door shuts behind you\
and everything blacks out...")

porch.set_exits({"N":drawing_room})
drawing_room.set_exits({"S":porch, "W":kitchen, "N":hallway, "E":bathroom})
kitchen.set_exits({"E":drawing_room})
hallway.set_exits({"S":drawing_room, "W":roomA, "U":attic, "D":basement})
roomA.set_exits({"E":hallway, "W":bathroom})
bathroom.set_exits({"W":drawing_room, "E":roomA})
basement.set_exits({"U":hallway, "N":roomB})
attic.set_exits({"D":hallway})


current_room = porch
alive=True
while alive:
    print(current_room.get_name())
    print(current_room.get_desc())
    print("There are exits to the:")
    for exits in current_room.get_exits():
        print(exits)

    if current_room==roomB:
        print("You died")
        alive=False
    else:
        move=input("which direction would you like to go?")
        if move.upper() in current_room.get_exits():
            current_room = current_room.get_exits()[move.upper()]
        else:
            print("Oh no, you hit a wall... Consider going another way.")




    



        
