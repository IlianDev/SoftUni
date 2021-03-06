from abc import ABC


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        Food.__init__(self, quantity)


class Meat(Food):
    def __init__(self, quantity):
        Food.__init__(self, quantity)


class Seed(Food):
    def __init__(self, quantity):
        Food.__init__(self, quantity)

class Fruit(Food):
    def __init__(self, quantity):
        Food.__init__(self, quantity)

