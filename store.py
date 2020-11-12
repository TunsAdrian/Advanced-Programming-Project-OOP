from category import Category
from categories import Categories
from products import Products
import product
from json import JSONDecodeError
import menus


def add_category():
    new_category = Category(input("Please enter a new category:\n"))
    Categories.add_category(new_category)
    print("Category " + str(new_category) + " added successfully")
    input("Press any key in order to continue\n")


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
    except JSONDecodeError:
        input("Error on retrieving the categories. Press any key in order to continue\n")


def list_categories():
    # display the existing categories
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
        input("Press any key in order to continue\n")
    except JSONDecodeError:
        input("Error on retrieving the categories. Press any key in order to continue\n")


def add_product():
    selected_category = Category(input("Input the desired category: "))
    try:
        categories = Categories.load_categories()
        if categories.count(selected_category) > 0:
            print(menus.ADD_PRODUCT_SUBMENU)
            try:
                selected_option = int(input("Choose an option: "))
                if selected_option == 1:
                    necklace_attributes = "(name, price, description, color, material, length)"
                    create_product("Necklace", necklace_attributes, selected_category)
                elif selected_option == 2:
                    bracelet_attributes = "(name, price, description, color, material, weight)"
                    create_product("Bracelet", bracelet_attributes, selected_category)
                elif selected_option == 3:
                    earring_attributes = "(name, price, description, material, length, weight)"
                    create_product("Earring", earring_attributes, selected_category)
                elif selected_option == 4:
                    print("Going back...\n")
                else:
                    error_handler()
            except ValueError:
                input("\nPlease try again by selecting a number for your option. Press any key to continue...")
                add_product()
    except JSONDecodeError:
        input("Error on retrieving the categories. Press any key in order to continue\n")


def create_product(product_name, product_attributes, category):
    attributes = input(f"Introduce the {product_attributes} for the {product_name}, separated by a comma\n")
    product_attributes = attributes.split(',')

    result = getattr(product, product_name)
    new_product = result(product_attributes[0], product_attributes[1], product_attributes[2],
                         product_attributes[3], product_attributes[4], product_attributes[5])
    Products.add_product(new_product, product_name, category)
    input(f"{product_name} added successfully. Press any key in order to continue\n")


def remove_product():
    pass


def display_products():
    # display the existing products
    try:
        products = Products.load_products()
        for prod in products:
            print(prod)
        input("\nPress any key in order to continue\n")
    except JSONDecodeError:
        input("Error on retrieving the products. Press any key in order to continue\n")


def place_order():
    pass


def display_orders():
    pass


def error_handler():
    print("This option does not exist")


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
        print(menus.MAIN_MENU)
        try:
            option = int(input("\nChoose an option: "))
            if option != 9:
                store_menu(option)
            else:
                print("\nLeaving the shop. See you soon!")
                break
        except ValueError:
            input("\nPlease try again by selecting an int number for the option. Press any key to continue...")
