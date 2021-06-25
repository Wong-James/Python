class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.defending = False
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        
        if not pirate.defending:
            pirate.health -= self.strength
        else:
            pirate.defending = False
    
    def defend(self):
        self.defending = True
        return self