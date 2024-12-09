#ignore the article, author and magazine.py's
class Author:
    def __init__(self, name,):
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


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine

        
        author.add_article(self)
        author.add_magazine(magazine)

        magazine.add_article(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Author must be an instance of Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be an instance of Magazine")
    


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")      

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def titles(self):
        return [article.title for article in self._articles]

    def prolific_authors(self):
        author_counts = {author: 0 for author in self.contributors()}
        for article in self._articles:
            author_counts[article.author] += 1
        return [author for author, count in author_counts.items() if count > 2]




