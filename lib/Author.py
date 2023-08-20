from Article import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article._magazine() for article in self._articles))
    
   
