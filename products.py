from json import JSONEncoder, JSONDecodeError, loads, dump

import product


# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    # also encode the type of the object
    def default(self, o):
        result = o.__dict__
        result['type'] = type(o).__name__
        return result


class Products:
    """ holds a list with all Product objects """
    products = []

    @classmethod
    def load_products(cls):
        """ reads the products.txt file and re-compose the Python objects
            from the json representation of products
        """
        decoder = product.Decoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError):
            cls.products = []
        return cls.products

    @classmethod
    def remove_product(cls, prod):
        """ Removes a product from the products collection. We pass the product
            to be removed as a parameter to the function and then, as a first step
            we remove it from the class variable 'products'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        cls.load_products()
        if prod in cls.products:
            cls.products.remove(prod)
            with open("products.txt", 'w') as f:
                for prod in cls.products:
                    e = Encoder()
                    encoded_prod = e.encode(prod)
                    dump(encoded_prod, f)
                    f.write("\n")

    @classmethod
    def add_product(cls, product_to_add):
        """ Adds a new product in the products collection. We need to save the
            new product on the disk too, so we have to call the Encoder class to
            transform the Python object in a JSON representation
        """
        cls.load_products()
        if product_to_add not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_product = e.encode(product_to_add)
                dump(encoded_product, f)
                f.write("\n")
