import progressbar
from time import sleep
from tqdm import trange
from starterFunctions import*
from random import*
from player import Player, Enemy
from level import*

my_player = Player()

def main():
    
    animated_marker()
    
    print("\nHi, Welcome to Doblin Dimension!")
    
    my_player.classChoice()
    
  
if __name__ == "__main__":
  main()


print(f"Now you are ready for battle, {my_player.classType}!")


levelLoad()

#Level 1-3
level(my_player)

if my_player.health > 0:
  print("Congratualtions, You've Won!")