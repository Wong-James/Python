from pet import Pet 

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def walk(self):
        self.pet.play()


    def feed(self):
        self.pet.eat()


    def bathe(self):
        self.pet.noise()



Fox = Pet("Ninetailed Fox", "Fox", "Fire-Breathing")
Naruto = Ninja("Naruto", "Izumaki", "Rice Balls", "Ground Beef", Fox)


Naruto.feed()
print(Naruto.pet.energy)
print(Naruto.pet.health)
Naruto.bathe()
Naruto.walk()
print(Naruto.pet.energy)
print(Naruto.pet.health)