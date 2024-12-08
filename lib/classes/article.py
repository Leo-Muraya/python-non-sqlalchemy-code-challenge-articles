class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title
        self.author = author
        self.magazine = magazine

        # Update relationships
        author.add_article(self)
        author.add_magazine(magazine)

        magazine.add_article(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title