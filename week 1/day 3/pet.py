class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 10
        self.health = 100


    def sleep(self):
        self.energy += 25
        return self


    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    
    def play(self):
        self.health += 5
        return self

    
    def noise(self):
        print('woof')


class Dragon(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        
#fire_breathing_dragon = Dragon("name", "type", "tricks")

#print(fire_breathing_dragon.__dict__)

