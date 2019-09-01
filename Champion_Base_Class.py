class Champion:

    def __init__(self, name, health, attack_damage, DPS, attack_range, attack_speed, armor, magical_resistance, price, lvl, team):

        #le contructeur sera le meme pour tt les persos on cherchera les valeur sur la feuille excel et on ajoutera les skills
        #dans la classe de chaque perso
        #sa c est les variables communes a tt les persos
        
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.DPS = DPS
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.armor = armor
        self.magical_resistance = magical_resistance
        self.price = price
        self.lvl = lvl
        self.team = team


    #ici les methodes communes a tt les persos
    #affichage stats
    #se deplacer
    #ciblage
        #attaquer
        #DPS
    #lvl up du perso

    def print_stats(self):
    
        #juste la pour check que tt ce passe bien comme il le faut
        
        print(self.name)
        print(self.health)
        print(self.attack_damage)
        print(self.DPS)
        print(self.attack_range)
        print(self.attack_speed)
        print(self.armor)
        print(self.magical_resistance)
        print(self.price)
        print(self.lvl)
        print(self.team)
    

    def lvl_up(self):

        #on va chercher les valeurs dans la feuille excel a la place des 0 mais ducoup chaque perso aura sa propre fonction lvl_up
        #cette fonction etait un test elle ne sera pas dans la classe de base

        self.name = 0
        self.health = 0 
        self.attack_damage = 0
        self.DPS = 0
        self.attack_range = 0
        self.attack_speed = 0
        self.armor = 0
        self.magical_resistance = 0
        self.price = 3 * self.price
        self.lvl = self.lvl + 1
        

        
