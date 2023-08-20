class Magazine:
    _all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @classmethod    
    def all(cls):
        return cls._all
            