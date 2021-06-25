from classes.ninja import Ninja
from classes.pirate import Pirate

ninja = Ninja("Sasuke")
pirate = Pirate("Davey Jones")
player = None

print("A fight between pilferers begins!")
action = input("Are you team pirate or team ninja?\nType 'n' for ninja.\nType 'p' for pirate")
action = action.lower()

if action == 'n':
    player = ninja
elif action == 'p':
    player = pirate
else:
    action = input("Please choose a valid team.\nAre you team pirate or team ninja?\nType 'n' for ninja.\nType 'p' for pirate")
