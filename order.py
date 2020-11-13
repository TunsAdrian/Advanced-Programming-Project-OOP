from json import JSONEncoder, JSONDecoder, dump, loads


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    # based on the object type, which is added at the end of the dict, the proper object will be created and returned
    def decode(self, o):
        data = loads(o)
        values = []
        for key in data.keys():
            values.append(data[key])
        order = Order(*values)
        return order


class Order:
    def __init__(self, product, quantity, address):
        self.product = product
        self.quantity = quantity
        self.address = address

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.product == other.product and self.quantity == other.quantity and self.address == other.address

    def __str__(self):
        return f"Order to {self.address}, containing {self.quantity} of {self.product}"
