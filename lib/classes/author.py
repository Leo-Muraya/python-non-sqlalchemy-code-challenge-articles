class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
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