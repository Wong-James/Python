class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.defending = False

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if not ninja.defending:
            ninja.health -= self.strength
        else:
            ninja.defending = False             
        return self

    def defend(self):
        self.defending = True
        return self