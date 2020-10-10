from category import Category
from categories import Categories
from json import JSONDecodeError


# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier

def add_category(category):
    pass


def delete_category(category):
    pass


def list_categories():
    pass


if __name__ == "__main__":
    # below some usage examples

    # create some categories
    cat_1 = Category("Necklaces")
    cat_2 = Category("Bracelets")
    cat_3 = Category("Earrings")

    # add them inside the Categories collection, and also save them
    # on the disk
    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    # display the existing categories
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
    except JSONDecodeError as e:
        categories = None

    # remove one category from the Categories collection
    Categories.remove_category(cat_3)

    # display again the existing categories
    for cat in categories:
        print(cat.name)
