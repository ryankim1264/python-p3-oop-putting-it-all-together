#!/usr/bin/env python3

class Shoe:
    all = []

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        Shoe.all.append(self)

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if not isinstance(value, str):
            raise Exception("Brand must be a string.")
        self._brand = value

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    size = property(get_size, set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
