from category import Category
from categories import Categories
from orders import Orders
from products import Products
from order import Order
import product
from json import JSONDecodeError
import menus


def add_category():
    new_category = Category(input("Please enter a new category:\n"))
    Categories.add_category(new_category)
    input("Category -" + str(new_category) + "- added successfully. Press enter key in order to continue\n")


def remove_category():
    option_remove_category = int(input(
        "Warning! Deleting a category will also delete all the products inside of it.\n1. Continue\n2. Go back\n"))
    if option_remove_category == 1:
        category_to_remove = Category(input("Introduce the name of the category to be removed:\n"))
        try:
            categories = Categories.load_categories()
            if categories.count(category_to_remove) > 0:
                products = Products.load_products()
                for prod in products:
                    if prod.get_category_name() == category_to_remove.name:
                        Products.remove_product(prod)
                Categories.remove_category(category_to_remove)
                input("Category -" + str(
                    category_to_remove) + "- and all its products were removed successfully.\nPress enter key in order to continue\n")
            else:
                category_option = int(input(
                    "This category does not exist in the list. Input 1 to try entering another category or any other number to return to the store menu:\n"))
                if category_option == 1:
                    remove_category()
        except JSONDecodeError:
            input("Error on retrieving the categories. Press enter key in order to continue\n")
    elif option_remove_category == 2:
        print("Going back...\n")
    else:
        error_handler()
        remove_category()


def list_categories():
    # display the existing categories or the categories with the products
    option_list_categories = int(input(
        "List the categories only or the categories with products?\n1. Categories only\n2. Categories and products\n3. Go back\n"))
    if option_list_categories == 1:
        try:
            categories = Categories.load_categories()
            for index, cat in enumerate(categories, start=1):
                print(f"{index}. {cat.name}")
            input("Press enter key in order to continue\n")
        except JSONDecodeError:
            input("Error on retrieving the categories. Press enter key in order to continue\n")
    elif option_list_categories == 2:
        try:
            categories = Categories.load_categories()
            products = Products.load_products()
            for index, cat in enumerate(categories, start=1):
                print(f"{index}. {cat.name}")
                for prod in products:
                    if prod.get_category_name() == cat.name:
                        print(f"\t{prod}", prod)
            input("Press enter key in order to continue\n")
        except JSONDecodeError:
            input("Error on retrieving the categories. Press enter key in order to continue\n")
    elif option_list_categories == 3:
        print("Going back...\n")
    else:
        error_handler()
        list_categories()


def add_product():
    selected_category = Category(input("Input the desired category: "))
    try:
        categories = Categories.load_categories()
        if categories.count(selected_category) > 0:
            print(menus.ADD_PRODUCT_SUBMENU)
            try:
                selected_option = int(input("Choose an option: "))
                if selected_option == 1:
                    necklace_attributes = "-name, price, description, color, material, length-"
                    create_product("Necklace", necklace_attributes, selected_category)
                elif selected_option == 2:
                    bracelet_attributes = "-name, price, description, color, material, weight-"
                    create_product("Bracelet", bracelet_attributes, selected_category)
                elif selected_option == 3:
                    earring_attributes = "-name, price, description, material, length, weight-"
                    create_product("Earring", earring_attributes, selected_category)
                elif selected_option == 4:
                    print("Going back...\n")
                else:
                    error_handler()
                    add_product()
            except ValueError:
                input("\nPlease try again by selecting a number for your option. Press enter key to continue...")
                add_product()
        else:
            try_again_option = int(input(
                "This category does not exist. Input 1 to try using another category or any other number to return to the store menu:\n"))
            if try_again_option == 1:
                add_product()
    except JSONDecodeError:
        input("Error on retrieving the categories. Press enter key in order to continue\n")


# initially I wanted to call the function create_product again if the attributes number was different than 6, but as
# this created recursive calls I used a while loop instead
def create_product(product_name, product_attribute_fields, category):
    product_attributes = []
    loop = True
    while loop:
        attributes = input(
            f"Introduce the {product_attribute_fields} for the {product_name}, each attribute separated by a comma\n")
        product_attributes = attributes.split(',')
        if product_attributes.__len__() != 6:
            product_attributes.clear()
            option_to_go = int(input(
                "Please make sure to include all the attributes. Input 1 to try again or any other number to return to the store menu:\n"))
            if option_to_go != 1:
                return
        else:
            loop = False
    result = getattr(product, product_name)
    new_product = result(category, product_attributes[0], product_attributes[1], product_attributes[2],
                         product_attributes[3], product_attributes[4], product_attributes[5])
    Products.add_product(new_product)
    input(f"{product_name} product added successfully. Press enter key in order to continue\n")


def remove_product():
    option_remove_product_menu = int(input(
        "You will have to input the index of the product you would like to remove. If you need to see the list of products, "
        "select option 2.\n1. Remove product\n2. Display all products\n3. Go back\n"))
    if option_remove_product_menu == 1:
        index_product_to_remove = int(input("Introduce the index of the product to be removed(starting from 1):\n"))
        try:
            products = Products.load_products()
            if 0 < index_product_to_remove <= products.__len__():
                product_to_remove = products[index_product_to_remove - 1]
                Products.remove_product(product_to_remove)
                input("Product -" + str(product_to_remove) +
                      "- removed successfully\nPress enter key in order to continue\n")
            else:
                product_option = int(input(
                    "This product does not exist in the list. Input 1 to try again or any other number to return to the store menu:\n"))
                if product_option == 1:
                    remove_product()
        except JSONDecodeError:
            input("Error on retrieving the products. Press enter key in order to continue\n")
    elif option_remove_product_menu == 2:
        display_products()
        remove_product()
    elif option_remove_product_menu == 3:
        print("Going back...\n")
    else:
        error_handler()
        remove_product()


def display_products():
    # display all existing products
    try:
        products = Products.load_products()
        for index, prod in enumerate(products, start=1):
            print(f"{index}. {prod}")
        input("\nPress enter key in order to continue\n")
    except JSONDecodeError:
        input("Error on retrieving the products. Press enter key in order to continue\n")


def place_order():
    option_place_order = int(input(
        "You will have to input the index of the product you would like to order. If you need to see the list of products, "
        "select option 2.\n1. Prepare order\n2. Display all products\n3. Go back\n"))
    if option_place_order == 1:
        index_product = int(input("Introduce the index of the product you want to order(starting from 1):\n"))
        try:
            products = Products.load_products()
            if 0 < index_product <= products.__len__():
                product_to_order = products[index_product - 1]
                quantity = 0
                loop = True
                while loop:
                    quantity = int(input("How many products of this kind you would like to order?\n"))
                    if quantity > 0:
                        loop = False
                delivery_address = input("Please write the address where this order should be delivered:\n")
                prepared_order = Order(product_to_order.__dict__, quantity, delivery_address)
                Orders.add_order(prepared_order)
                input(f"Your order has been placed successfully. Press enter key in order to continue\n")
        except JSONDecodeError:
            input("Error on retrieving the products. Press enter key in order to continue\n")
    elif option_place_order == 2:
        display_products()
        place_order()
    elif option_place_order == 3:
        print("Going back...\n")
    else:
        error_handler()
        remove_product()


def remove_order():
    option_remove_order_menu = int(input(
        "You will have to input the index of the order you would like to cancel. If you need to see the list of orders, "
        "select option 2.\n1. Cancel order\n2. Display all orders\n3. Go back\n"))
    if option_remove_order_menu == 1:
        index_order_to_remove = int(input("Introduce the index of the order to be removed(starting from 1):\n"))
        try:
            orders = Orders.load_orders()
            if 0 < index_order_to_remove <= orders.__len__():
                order_to_remove = orders[index_order_to_remove - 1]
                Orders.remove_order(order_to_remove)
                input(
                    f"Order with number {index_order_to_remove} was cancelled successfully\nPress enter key in order to continue\n")
            else:
                order_option = int(input(
                    "This order does not exist in the list. Input 1 to try again or any other number to return to the store menu:\n"))
                if order_option == 1:
                    remove_order()
        except JSONDecodeError:
            input("Error on retrieving the orders. Press enter key in order to continue\n")
    elif option_remove_order_menu == 2:
        display_orders()
        remove_order()
    elif option_remove_order_menu == 3:
        print("Going back...\n")
    else:
        error_handler()
        remove_order()


def display_orders():
    # display all existing orders
    try:
        orders = Orders.load_orders()
        for index, placed_order in enumerate(orders, start=1):
            print(f"{index}. {placed_order}")
        input("\nPress enter key in order to continue\n")
    except JSONDecodeError:
        input("Error on retrieving the orders. Press enter key in order to continue\n")


def error_handler():
    print("\nThis option does not exist\n")


def store_menu(menu_option):
    menu = {
        1: add_category,
        2: remove_category,
        3: list_categories,
        4: add_product,
        5: remove_product,
        6: display_products,
        7: place_order,
        8: remove_order,
        9: display_orders
    }

    func = menu.get(menu_option, error_handler)
    func()


if __name__ == '__main__':
    while True:
        print(menus.MAIN_MENU)
        try:
            option = int(input("\nChoose an option: "))
            if option != 10:
                store_menu(option)
            else:
                print("\nLeaving the shop. See you soon!")
                break
        except ValueError:
            input("\nPlease try again by selecting an int number for the option. Press enter key to continue...")
