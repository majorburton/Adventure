class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print "You are carrying:"
        for item in self.items:
            print item.get_name()

class Item():
    def __init__(self, name):
        self.name = name
        self.known_commands = {}

    def get_name(self):
        return self.name


class Literature(Item):
    def __init__(self, name, contents = "This item is blank."):
        Item.__init__(self, name)
        self.contents = contents
        self.known_commands["read"] = self.read

    def read(self, command):
        print self.contents

    def self_contents(self, contents):
        self.contents = contents

class Note_1(Literature):
    def __init__(self, name, contents = "Wow I can't believe I finally made it. Gotta note this one."):
        Item.__init__(self, name)
        self.contents = contents

class Lamp(Item):
    def __init__(self, name, battery_level = 100, state = "off"):
        Item.__init__(self, name)
        self.battery_level = battery_level

    def turn_on(self):
        self.state = "on"

    def turn_off(self):
        self.state = "off"

    def change_batteries(self):
        self.battery_level = 100

    def compute_usage(self):
        # Compute the time it's been on and then drain the battery and equal amount
        pass



