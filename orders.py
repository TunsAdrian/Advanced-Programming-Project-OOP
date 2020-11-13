from json import JSONEncoder, JSONDecodeError, loads, dump

import order


# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    def default(self, o):
        return o.__dict__


class Orders:
    """ holds a list with all Order objects """

    orders = []

    @classmethod
    def load_orders(cls):
        """ reads the orders.txt file and re-compose the Python objects
            from the json representation of orders. The content of the
            orders.txt file should look something like:

            "{\"name\": \"Necklaces\"}"
            "{\"name\": \"Bracelets\"}"

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the orders
            list. We have avoided this by overloading the __eq__() operator in
            order class. More on this during the lectures.
        """
        decoder = order.Decoder()

        try:
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.decode(data)
                    if decoded_order not in cls.orders:
                        cls.orders.append(decoded_order)
        except (JSONDecodeError, FileNotFoundError):
            cls.orders = []
        return cls.orders

    @classmethod
    def remove_order(cls, cat):
        """ Removes a order from the orders collection. We pass the order
            to be removed as a parameter to the function and then, as a first step
            we remove it from the class variable 'orders'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        cls.load_orders()
        if cat in cls.orders:
            cls.orders.remove(cat)
            with open("orders.txt", 'w') as f:
                for cat in cls.orders:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")

    @classmethod
    def add_order(cls, order_to_add):
        """ Adds a new order in the orders collection. We need to save the
            new order on the disk too, so we have to call the Encoder class to
            transform the Python object in a JSON representation
        """
        cls.load_orders()
        if order_to_add not in cls.orders:
            with open("orders.txt", 'a') as f:
                e = Encoder()
                encoded_order = e.encode(order_to_add)
                dump(encoded_order, f)
                f.write("\n")
