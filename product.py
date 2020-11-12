from json import JSONEncoder, JSONDecoder, dump, loads
from abc import ABC


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    # based on the object type the proper object will be created and returned
    def decode(self, o):
        data = loads(o)
        values = []
        for key in data.keys():
            values.append(data[key])
        if values[-1] == 'Necklace':
            del values[-1]
            cat = Necklace(*values)
        elif values[-1] == 'Bracelet':
            del values[-1]
            cat = Bracelet(*values)
        elif values[-1] == 'Earring':
            del values[-1]
            cat = Earring(*values)
        else:
            raise Exception('A category that is not supported is presented in the products file')
        return cat


# define the Product class, which is the base class for all the  products in the store
# make it abstract class, as a simple Product should not be instantiated
class Product(ABC):
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.description == self.description


class Necklace(Product):
    def __init__(self, name, price, description, color, material, length):
        super().__init__(name, price, description)
        self.color = color
        self.material = material
        self.length = length

    def __eq__(self, other):
        return super().__eq__(other) and self.color == other.color and self.material == other.material and self.length == other.length

    def __str__(self):
        return f"Necklace: {self.name}, price: {self.price}$, description: {self.description}, of material {self.material} and color {self.color}, having a length of {self.length}cm"


class Bracelet(Product):
    def __init__(self, name, price, description, color, material, weight):
        super().__init__(name, price, description)
        self.color = color
        self.material = material
        self.weight = weight

    def __eq__(self, other):
        return super().__eq__(other) and self.color == other.color and self.material == other.material and self.weight == other.weight

    def __str__(self):
        return f"Bracelet: {self.name}, price: {self.price}$, description: {self.description}, of material {self.material} and color {self.color}, having a weight of {self.weight}kg"


class Earring(Product):
    def __init__(self, name, price, description, material, length, weight):
        super().__init__(name, price, description)
        self.material = material
        self.length = length
        self.weight = weight

    def __eq__(self, other):
        return super().__eq__(other) and self.material == other.material and self.length == other.length and self.weight == other.weight

    def __str__(self):
        return f"Earring: {self.name}, price: {self.price}$, description: {self.description}, of material {self.material}, having a length of {self.length}cm and a weight of {self.weight}kg"
