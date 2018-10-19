class wing(object):
    
    def __init__(self, ratio):
            self.ratio = ratio
    
    def fly(self):
        if self.ratio > 1:
            print("Smiesznie")
        elif self.ratio = 1:
            print("ciezko idzie ale latam")
        else:
            print("dziekuje, postoje")



class duck(object):

    def __init__(self):
        self.wing = wing(1.8)
    
    def walk(self):
        print("waddle, waddle, waddle")
    def swim(self):
        print("Wskakuj do wody")
        
    def quack(self):
        print("kwa kwa")
        
    def fly(self):
        self.wing.fly()
        
class pingwin(self):

    def walk(self):
        print("Chce chodzic")

    def swim(self):
        print("Nie umiem plywac")

    def quack(self):
        print("Jestem pinginem, odzywam sie inaczej)"

def test_duck(duck):
duck.walk()
duck.swim()
duck.quack()


class mallard(duck):
    pass
  
class flock(obcject):
    
    def __init__(self):
        srlf.flock = []
        
    def add.duck(self, duck: Duck) -> None:
        if isinstance(duck, duck):
            
            self.flock.append(duck)
        
    def migrate(self):
        for duck in self.flock:
            duck.fly()
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem
                #raise

  
if __ name_ == '__main__':
    dondald = duck()
  #  test_duck(donald)
