#!/usr/bin/env python3
import ipdb

# from classes.many_to_many import Article
# from classes.many_to_many import Author
# from classes.many_to_many import Magazine
# from classes.many_to_many import RelationshipManager
from classes.many_to_many import Article, Author, Magazine, RelationshipManager

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author1 = RelationshipManager.add_author("Gorilla")
    author2 = RelationshipManager.add_author("pp endkaka")

    magazine1 = RelationshipManager.add_magazine("Tech Weekly", "Technology")
    magazine2 = RelationshipManager.add_magazine("Art Monthly", "Art")

    article1 = RelationshipManager.add_article(author1, magazine1, "Chapo")
    article2 = RelationshipManager.add_article(author1, magazine2, "MUSTAAAARD")
    article3 = RelationshipManager.add_article(author2, magazine1, "Bling Bling")

    print(RelationshipManager.find_articles_by_author(author1))
    print(RelationshipManager.find_authors_by_magazine(magazine1))

 
    ipdb.set_trace()
