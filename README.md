## Github repository

https://github.com/Leo-Muraya/python-non-sqlalchemy-code-challenge-articles

# Magazine Author Article System

This Python-based system models the relationships between authors, magazines, and articles. Authors can write articles for magazines, and magazines can track articles, contributors, and article titles. The system ensures that relationships between these entities are valid and that data integrity is maintained.

## Overview

The system is composed of three primary classes:

- **Author**: Represents an author who can write articles and contribute to multiple magazines.
- **Article**: Represents an article written by an author for a specific magazine.
- **Magazine**: Represents a magazine that stores articles and tracks its contributors.

## Class Descriptions

### 1. `Author`
The `Author` class allows an author to write articles and associate with magazines.

#### Constructor:
- **`__init__(self, name)`**: Initializes an author with a name. The name must be a non-empty string.

#### Properties:
- **`name`**: The name of the author. This is a read-only property, meaning once the author is created, the name cannot be changed.

#### Methods:
- **`articles()`**: Returns a list of articles written by the author.
- **`magazines()`**: Returns a list of unique magazines the author has contributed to.
- **`add_article(article)`**: Adds an article to the author's list of articles.
- **`add_magazine(magazine)`**: Adds a magazine to the author's list of magazines.
- **`write_article(magazine, title)`**: Allows the author to write an article for a specific magazine with a given title.

### 2. `Article`
The `Article` class represents an article written by an author for a specific magazine.

#### Constructor:
- **`__init__(self, author, magazine, title)`**: Initializes an article with the given author, magazine, and title. It also ensures that the article is added to both the author's and magazine's list of articles.

#### Properties:
- **`title`**: The title of the article. The title is a read-only property that cannot be modified once set.

### 3. `Magazine`
The `Magazine` class represents a magazine that stores articles and tracks contributors.

#### Constructor:
- **`__init__(self, name, category)`**: Initializes a magazine with a name and category. The name must be between 2 and 16 characters long, and the category must be a non-empty string.

#### Properties:
- **`name`**: The name of the magazine. The name can be changed within the allowed length range (2 to 16 characters).
- **`category`**: The category of the magazine. The category can be changed to a non-empty string.

#### Methods:
- **`add_article(article)`**: Adds an article to the magazine's list of articles.
- **`articles()`**: Returns a list of articles in the magazine.
- **`contributors()`**: Returns a list of unique authors who have contributed to the magazine.
- **`titles()`**: Returns a list of titles of articles in the magazine.
- **`prolific_authors()`**: Returns a list of authors who have contributed more than two articles to the magazine.

## Example Usage

```python
# Create authors
john = Author("John Doe")

# Create magazines
tech_mag = Magazine("Tech Monthly", "Technology")
health_mag = Magazine("Health Today", "Health")

# Author writes articles
article1 = john.write_article(tech_mag, "The Future of AI")
article2 = john.write_article(tech_mag, "AI and Data Science")
article3 = john.write_article(health_mag, "Living Healthy in 2024")

# Get articles written by John
print(john.articles())  # Lists articles written by John

# Get unique magazines the author has contributed to
print(john.magazines())  # Lists magazines John has contributed to

# Get articles in "Tec
