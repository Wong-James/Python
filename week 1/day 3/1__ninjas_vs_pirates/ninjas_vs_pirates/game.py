from classes.ninja import Ninja
from classes.pirate import Pirate

ninja = Ninja("Sasuke")
pirate = Pirate("Davey Jones")
player = None
enemy = None

print("A fight between pilferers begins!")
action = input("Are you team pirate or team ninja?\nType 'n' for ninja.\nType 'p' for pirate\n")
action = action.lower()

if action == 'n':
    player = ninja
    enemy = pirate
elif action == 'p':
    player = pirate
    enemy = ninja
else:
    action = input("Please choose a valid team.\nAre you team pirate or team ninja?\nType 'n' for ninja.\nType 'p' for pirate\n")

while player.health > 0 and enemy.health > 0:
    if action == 'a':
        print(player.name + " attacks " + enemy.name + "!")
        player.attack(enemy).show_stats()
        enemy.show_stats()
        print(enemy.name + " attacks " + player.name + "!")
        enemy.attack(player)
        player.show_stats()
        enemy.show_stats()
        action = input(player.name + " choose your action!\nType 'd' to defend.\nType 'a' to attack\n")
    elif action == 'd':
        print(player.name + " defends!")
        player.defend().show_stats()
        enemy.show_stats()
        action = input(player.name + " choose your action!\nType 'd' to defend.\nType 'a' to attack\n")
    else:
        action = input("Please choose a valid action.\nType 'd' to defend.\nType 'a' to attack\n")


# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

