from Adventure import Room
from inventory import Inventory
from inventory import Item


Field = Room('Field', 'You are in the middle of a small open field with a giant forest all around you. In your right hand is a brown teddy bear. On your back is a light pink bag.', 'f')
Fenced_Off_Forest_e = Room('Fenced off forest', 'There is a wooden fence blocking the way into the forest. Along the fence is a walkway. It seems to go around the entire field.', 'fof')
Fenced_Off_Forest_w = Room('Fenced off forest', 'There is a wooden fence blocking the way into the forest. Along the fence is a walkway. It seems to go around the entire field', 'fof')
Fenced_Off_Forest_s = Room('Fenced off forest', 'There is a wooden fence blocking the way into the forest. Along the fence is a walkway. It seems to go around the entire field. On the ground you can see a small bird made of gold with a crack in the head of it.', 'fof')
Forest_Entrance = Room('Forest Entrance', 'You approach a small gate leading into the forest. There is a note nailed to the gate and a lamp hooked onto the side. A small pink hammer can be seen poking out the grass on the ground.', 'fe')
Branched_Forest = Room('Branched Forest', 'There are 3 paths branching out in different directions: one to the east, one to the west, and one to the north with a piece of paper at the begining of every path.', 'df')
hallway2 = Room('upstairs hallway', 'you are in the hallway', 'uh')
bedroom1 = Room('bedroom', 'you are in the bedroom', 'b1')
bedroom2 = Room('bedroom', 'you are in the bedroom', 'b2')
bedroom3 = Room('bedroom', 'you are in the bedroom', 'b3')
Living = Room('living room', 'you are in the living room', 'lr')

Field.add_connection(Forest_Entrance, "thin pathway", ["to a small gate that leads into the forest.", "n"])
Field.add_connection(Fenced_Off_Forest_e, "thin pathway", ["to the east of the small field.", "e"])
Field.add_connection(Fenced_Off_Forest_w, "thin pathway", ["to the west of the small field.", "w"])
Field.add_connection(Fenced_Off_Forest_s, "thin pathway", ["to the south of the small field.", "s"])
Fenced_Off_Forest_e.add_connection(Field, "thin pathway", ["back to the middle of the field.", "w"])
Fenced_Off_Forest_e.add_connection(Forest_Entrance, "walkway along the fence leading to the left,", ["to a small gate.", "n"])
Fenced_Off_Forest_e.add_connection(Fenced_Off_Forest_s, "walkway along the fence leading to the right,", ["the opposite side of the small gate.", "s"])
Fenced_Off_Forest_w.add_connection(Field, "thin pathway", ["back to the center of the field", "e"])
Fenced_Off_Forest_w.add_connection(Forest_Entrance, "walkway along the fence leading to the right,", ["to a small gate.", "n"])
Fenced_Off_Forest_w.add_connection(Fenced_Off_Forest_s, "walkway along the fence leading left,", ["to the opposite side of the small gate.", "s"])
Fenced_Off_Forest_s.add_connection(Field, "thing pathway", ["back to the center of the field.", "n"])
Fenced_Off_Forest_s.add_connection(Fenced_Off_Forest_e, "walkway along the fence leading to the left,", ["to the east side of the field.", "e"])
Fenced_Off_Forest_s.add_connection(Fenced_Off_Forest_w, "walkway along the fence leading to the right,", ["to the west side of the field.", "w"])
Forest_Entrance.add_connection(Field, "Broken fence", ["south", "s"])
Forest_Entrance.add_connection(Branched_Forest, "Pathway", ["north", "n"])
Branched_Forest.add_connection(Forest_Entrance, "Pathway", ["south", "s"])

#Forest_Entrance.add_item(note())
#Forest_Entrance.add_item(lamp())
#Forest_Entrance.add_item(hammer())

inventory = Inventory()
current_room = Field
current_room.enter_room()

while True:
    command = raw_input("What would you like to do?  ")
    if command in ["exit", "x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        result.enter_room()
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
        print "I don't know what you mean."


#dining.add_room('s', kitchen)
#hallway.add_room('s', dining)
#hallway.add_room('u', hallway2)
#hallway.add_room('e', Living)
#Living.add_room('w', hallway)
#hallway2.add_room('d', hallway)
#hallway2.add_room('n', bedroom1)
#hallway2.add_room('e', bedroom2)
#hallway2.add_room('w', bedroom3)
#bedroom1.add_room('s', hallway2)
#bedroom2.add_room('w', hallway2)
#bedroom3.add_room('e', hallway2)


current_room = Field
Field.enter_room()

while True:
    direction = raw_input("Where do you wish to go?  ")
    if direction == 'x':
        break
    elif current_room.is_valid_direction(direction):
        current_room = current_room.next_room(direction)
        current_room.enter_room()
    else:
        print "Oof"