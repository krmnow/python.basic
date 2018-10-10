class enemy:
    def __init__(self, name="enemy", hit_points=0, lives=1):
        self.name = name
        self.hit+points = hit_points
        self.lives = lives
        
    def take_demage(self, demage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remianing_points
            print
        else:
            self.lives = 1
            
    def __str__(self):
        return "Name {0.name}, lives {0.lives}, hist: {0.hit_points}".format(self)
    
class troll(enemy):
    pass
