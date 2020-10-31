from json import JSONEncoder


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

    # define the Product class, which is the base class for all the  products in the store


class Product:
    def __init__(self, name):
        self.name = name


class Necklace(Product):
    def __init__(self, name, color, material, length):
        super().__init__(name)
        self.color = color
        self.material = material
        self.length = length

    def __str__(self):
        print(
            f"Necklace:{self.name} price:{self.price}$ description:{self.description}  from {self.material} and color {self.color}, has length {self.length}cm")


class Bracelet(Product):
    def __init__(self, name, color, material, weight):
        super().__init__(name)
        self.color = color
        self.material = material
        self.weight = weight

    def __str__(self):
        print(
            f"Bracelet:{self.name} price:{self.price}$ description:{self.description}  from {self.material} and color {self.color}, weights {self.weight}kg")


class Earring(Product):
    def __init__(self, name, material, length, weight):
        super().__init__(name)
        self.material = material
        self.length = length
        self.weight = weight

    def __str__(self):
        print(
            f"Earring:{self.name} price:{self.price}$ description:{self.description}  from {self.material} and length {self.length}cm, weights {self.weight}kg")
