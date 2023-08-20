class Magazine:
    _all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)
        self._contributors = []

    @classmethod    
    def all(cls):
        return cls._all
    
    def add_contributors(self, author):
        self._contributors.append(author)

    def contributors(self):
        return self._contributors    
            