class Player:
    def __init__(self):
        self.health = 50
        self.attack = 150
        self.items = []
        self.name = ""
        self.weapon = ""
        self.defense = 3
        self.classType = ""
        self.potion = 2
    
    def defend(self):
      self.defense = self.defense * 2
    def reset_defense(self):
      self.defense //= 2
      
    def classChoice(self):
        print("What class would you like to play as? There is the Knight, Assassin, and the Mage.\n")
        print("1. Knight\n2. Assassin\n3. Mage\n")
              
        x = input()
        x = x.lower()
    
        if x == "1" or x == "knight":
          self.classType = "Knight"
          self.weapon = "sword"
        elif x == "assassin" or x == "2":
          self.classType = "Assassin"
          self.weapon = "daggers"
        elif x == "mage" or x == "3":
          self.classType = "Mage"
          self.weapon = "staff"
        else:
          #print("Overlooked some condition")
          print("Try Again: ")
          self.classChoice();
    #def playerAttack(self, weapon)

class Enemy(Player):
  def __init__(self, health, attack, name, defense):
    self.health = health
    self.attack = attack
    self.name = name
    self.defense = defense