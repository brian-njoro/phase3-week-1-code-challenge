class Magazine:
    _all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)
        self._articles = []
        self._contributors = []

    def category(self):
        return self.category    

    @classmethod    
    def all(cls):
        return cls._all
    
    def add_contributors(self, author):
        self._contributors.append(author)

    def contributors(self):
        return self._contributors 

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine 
            else:
                print("!!ERROR!!") 
        return None  

    def _article_titles(self):
        return [article.title for article in self._articles]


    @classmethod 
    #uncertain
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        #check if a magazine was found using the find_by_name method.
        if magazine:
            return magazine._article_titles() #unable to make instance method _article_titles accessible in the class method
        else:
            return []
    
    #also uncertain
    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            pass
        #return [author for author, count in authors.items() if count > 2]