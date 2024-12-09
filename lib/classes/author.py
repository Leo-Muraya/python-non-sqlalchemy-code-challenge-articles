class Author:
    def __init__(self, name,):
        self._name = name
        self._articles = []
        self._magazines = []   

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(self._magazines)) 

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def add_magazine(self, magazine):
        if magazine not in self._magazines:
            self._magazines.append(magazine)

    def write_article(self, magazine, title):
        return Article(self, magazine, title)
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")