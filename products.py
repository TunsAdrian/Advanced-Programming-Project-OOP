from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
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
            from the json representation of products. The content of the
            products.txt file should look something like:

            "{\"name\": \"Necklaces\"}"
            "{\"name\": \"Bracelets\"}"

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the products
            list. We have avoided this by overloading the __eq__() operator in
            product class. More on this during the lectures.
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
    def remove_product(cls, cat):
        """ Removes a product from the products collection. We pass the product
            to be removed as a parameter to the function and then, as a first step
            we remove it from the class variable 'products'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        cls.load_products()
        if cat in cls.products:
            cls.products.remove(cat)
            with open("products.txt", 'w') as f:
                for cat in cls.products:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
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
