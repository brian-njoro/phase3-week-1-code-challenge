class Magazine:
    _all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)
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
            