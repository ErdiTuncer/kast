from enum import Enum

class Material(Enum):
    WOOD = 'Wood'
    CARBONFIBER = 'CarbonFiber'
    GLASS = 'Glas'

class Wardrobe:
    def __init__(self, name = "", material = Material.WOOD, broken = False, occupied = False, open = False):
        self.name = name
        self.material = material
        self.broken = broken
        self.occupied = occupied
        self.open = open
        if isinstance(material, Material):
            self._material = material
        else:
            raise TypeError("Input must be a material")

    def __str__(self):
        return self.material + ", " + self.name + ", " + str(self.opened) + ", " + str(self.occupied) + ", " + str(self.broken)

    def open(self):
        if self.broken == True:
            return "Cant open the door, because you broke the closet"
        if self.open == True:
            return "the wardrobe is open"
        else:
            self.open = True
            return "You opened the door"
    def close(self):
        if self.broken == True:
            return "Cant close the door, because you broke the closet"
        if self.open == False:
            return "The door is already closed"
        else:
            self.open = True
            return "The door is closed now"

    def broken(self):
        if self.broken == True:
            return "The Wardrobe is broken"
        else:
            self.broken = False
            return "Wardrobe is OK"

    def getIn(self):
        if self.broken == True:
            return "Cant get in, because you broke the closet"
        if self.occupied == False and self.opened == True:
            self.occupied = True
            self.open = False
            return "Your are in wardrobe"

    def getOut(self):
        if self.broken == True:
            return "Cant get out, because you broke the closet"
        if self.occupied == True:
            self.occupied = False
            self.open = True
            return "You are now out the closet"
        else:
            return "You cant get out because, you are not in the closet"

    def broken(self):
        if self.broken == True:
            return "The wardrobe is broken"
        else:
            return "The status of wardrobe is OK"

    def kick(self):
        if self.broken == True:
            return "Cant kick the door, because you broke the closet"
        if self.occupied == True:
            return "Cant kick the door, you are in the closet"
        if self.material == Material.GLASS:
            self.broken = True
            return "You broke the Glass, and you are bleeding"
        elif self.material == Material.CARBONFIBER:
            return "That most hurt, carbon is very strong"

        return "You got a splinter, and the wardrobe is still intact"
