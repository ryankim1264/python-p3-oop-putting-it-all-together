#!/usr/bin/env python3

class Book:
    all = []

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        Book.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        self._title = value

    title = property(get_title, set_title)

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    page_count = property(get_page_count, set_page_count)
    
    def turn_page(self):
           print("Flipping the page...wow, you read fast!")
    
        