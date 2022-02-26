from random import*
from combat import*
from player import Player, Enemy
import randomEnemy

def level(my_player):
  #Level 1,2,3
  i = 1
  while my_player.health > 0 and i != 4:
    print(f"\n\n------LEVEL {i}------")
  
    tiles = randrange(4,9,1)
    if i == 1:
      location = "Jungle"
    elif i == 2:
      location = "Factory"
    elif i == 3:
      location = "Abyssal Plains"
      
    print(f"You are now in The {location}")
    """
    
    This code is intended to make random enemies, can have weighted values"""
    enemyList = ["Goblin", "Doblin", "Orc", ".Orc", "Troll", "Elf"]
    
    while (tiles > 0 and my_player.health > 0):
      print(f"\n**Spaces left to move: {tiles}**")
      the_enemy = randomEnemy.random_enemy_generator()
      fight_chance = randint(0,1)
      
      if fight_chance == 1:
        print(f"It's a surprise attack! The {the_enemy.name} has spotted you!\n")
        print(f"It has {the_enemy.health} HP!")
        print("What will you do?")
        while the_enemy.health > 0 and my_player.health > 0:
          
          cool_combat(my_player, the_enemy)
          print("You advance a space") #Error when Beating Game Would Show Up Upon Beting the Game
        if(my_player.health <= 0):
          print("\n\nGAME OVER!") #GAME OVER
        else:
          tiles = tiles - 1
      else:
        print("No enemy, you advance a space\n")
        tiles = tiles - 1
    i += 1