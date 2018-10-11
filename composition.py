class tag(object):
    
    def __init__(self, name, contects):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '<{}/>'.format(name)
        self.contects = contects
    
    def __str__(self):
        return "{0.start_tag}{0.contecs}{0.end_tag}".format(self)
        
    def display(self):
        print(self)
