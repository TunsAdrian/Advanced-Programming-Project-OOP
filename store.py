from category import Category
from categories import Categories
from json import JSONDecodeError


# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier

def add_category():
    new_category = Category(input("Please enter a new category:\n"))
    Categories.add_category(new_category)
    print("Category " + str(new_category) + " added successfully")
    iinput("Press any key in order to continue\n")


def remove_category():
    new_category = Category(input("Introduce the category to be removed:\n"))
    try:
        categories = Categories.load_categories()
        if categories.count(new_category) > 0:
            Categories.remove_category(new_category)
            print("Category " + str(new_category) + " removed successfully")
            input("Press any key in order to continue\n")
        else:
            category_option = int(input(
                "This category does not exist in the list. Press 1 to try entering another category or 2 to return to the store menu\n"))
            if category_option == 1:
                remove_category()
    except JSONDecodeError as e:
        input("Error on retrieving the categories. Press any key in order to continue\n")


def list_categories():
    # display the existing categories
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
        input("Press any key in order to continue\n")
    except JSONDecodeError as e:
        input("Error on retrieving the categories. Press any key in order to continue\n")


def add_product():
    pass


def remove_product():
    pass


def display_products():
    pass


def place_order():
    pass


def display_orders():
    pass


def error_handler():
    print("This option does not exist")


MENU_DISPLAY = """Welcome to our shop
1. Add a category
2. Remove a category
3. Display categories
4. Add a product
5. Remove a product
6. Display a product
7. Place an order
8. Display orders
9. Exit"""


def store_menu(menu_option):
    menu = {
        1: add_category,
        2: remove_category,
        3: list_categories,
        4: add_product,
        5: remove_product,
        6: display_products,
        7: place_order,
        8: display_orders
    }

    func = menu.get(menu_option, error_handler)
    func()


if __name__ == '__main__':
    while True:
        print(MENU_DISPLAY)
        option = int(input("\nChoose an option: "))
        if option != 9:
            store_menu(option)
        else:
            print("\nExiting program")
            break
