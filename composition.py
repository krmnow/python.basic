class tag(object):
    
    def __init__(self, name, contects):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '<{}/>'.format(name)
        self.contects = contects
    
    def __str__(self):
        return "{0.start_tag}{0.contecs}{0.end_tag}".format(self)
        
    def display(self, file=None):
        print(self, file=file)

class doctype(tag):
    def __init__(self):
        super().__init__("!DOCTYPE HTML PUBLIC", '')
        self.end_tag = ''
        
class head(tag):
    
    def __init__(self):
        super().__init__('head', '')
        self._title_tag = tag('title', title)
            self.contects = str(self._title_tag)
        
class body(tag):
    
    def __init__(self):
        super().__init__('body', '')
        self.body_contects = []

    def add_tag(self, name, contects):
        new_tag = tag (name, contects)
        self.body_contects.append(new_tag)
        
    def display(self, file=None):
        for tag in self._body_contects:
            self.contects += str(tag)
            
            super().display(file=file)
            
class html_doc(object):
    
    def __init__(self):
        self._doc_type = doctype()
        self._head = head(title)
        self._body = body()
        
    def add_tag(self, name, contects):
        self._body.add_tag(name, contects)
        
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    my_page = html_doc('Demo Html document')
    my_page.add._tag('h1', "Main heading') 
    my_page.add._tag('h2', 'sub heading')
    my_page.add._tag('p', 'this is paragraph')
        with open('test.html', 'w') as test_doc:
            my_page.display
    
new_body = body()
new_body.add_tag('h1', 'agregation')
new_body.add_tag('p', 'unlike composition agregation uses instances')
new_body.add_tag('p', 'nie podmieni go')

my_page._body = new_body
with open("test2.html", 'w') as test_doc:
    my_page.display(file=test_doc)
