class enemy:
    def __init__(self, name="enemy", hit_points=0, lives=1):
        self.name = name
        self.hit+points = hit_points
        self.lives = lives
        self.alive = True
        
    def take_demage(self, demage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remianing_points
            print
        else:
            self.lives = 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False
            
    def __str__(self):
        return "Name {0.name}, lives {0.lives}, hist: {0.hit_points}".format(self)
    
class troll(enemy):
    
    def __init__(self, name):
        super(troll, self).__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}, {0.name} stopiing you".format(self))
        
class vampire(enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)
        
    def dodges(self):
        import random
        if random.randit(1,3) == 3:
            print("+++++ {0.name} doges +++".format(self))
            return True
        else:
            return False
        
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)
        
        
