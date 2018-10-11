class tag(object):
    
    def __init__(self, name, contects):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '<{}/>'.format(name)
        self.contects = contects
    
    def __str__(self):
        return "{0.start_tag}{0.contecs}{0.end_tag}".format(self)
        
    def display(self):
        print(self)

class doctype(tag):
    def __init__(self):
        super().__init__("!DOCTYPE HTML PUBLIC", '')
        self.end_tag = ''
        
class head(tag):
    
    def __init__(self):
        super().__init__('head', '')
        
class body(tag):
    
    def __init__(self):
        super().__init__('body', '')
        self.body_contects = []

    def add_tag(self, name, contects):
        new_tag = tag (name, contects)
        self.body_contects.append(new_tag)
        
    def display(self):
        for tag in self._body_contects:
            self.contects += str(tag)
            
            super().display
