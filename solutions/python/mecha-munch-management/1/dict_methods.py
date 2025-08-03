"""Functions to manage a users shopping cart items."""
from collections import Counter, defaultdict

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    c = Counter(items_to_add)
    c.update(current_cart)
    return c    


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = defaultdict(int)
    for n in notes:
        cart[n] += 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for ru in recipe_updates:
        ideas[ru[0]] = ru[1]           
            
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = defaultdict(list)
    for i in cart:
        fulfillment[i].append(cart[i])
        fulfillment[i].append(aisle_mapping[i][0])
        fulfillment[i].append(aisle_mapping[i][1])
        
    return dict(reversed(sorted(fulfillment.items())))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for i in fulfillment_cart:
        if fulfillment_cart[i][0] < store_inventory[i][0]:
            store_inventory[i][0] -= fulfillment_cart[i][0]
        else:
            store_inventory[i][0] = "Out of Stock"
    
    return store_inventory
