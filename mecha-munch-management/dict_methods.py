"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    dic_values = current_cart.keys()
    for item in items_to_add:
        if item in dic_values:
            current_cart[item] += 1
        else:
            current_cart.setdefault(item, 1)
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    update_dict = dict.fromkeys(notes, 1)
    return update_dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_dict = dict(sorted(cart.items()))
    return sorted_dict


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    merged_dict = {}
    for key in cart:
        if key in isle_mapping:
            merged_dict[key] = [cart[key]] + isle_mapping[key]

    new_dict = dict(sorted(merged_dict.items(), key=lambda x: x[0], reverse=True))
    return new_dict


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated."""
    updated_inventory = {}

    for key, value in fulfillment_cart.items():
        if key in store_inventory:
            store_inventory[key][0] -= value[0]

    for key, value in store_inventory.items():
        if value[0] == 0:
            store_inventory[key][0] = 'Out of Stock'

    return store_inventory
