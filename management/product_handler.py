from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type_of):
    list = []
    if type(type_of) != str:
        raise TypeError("product type must be a str")
    for product in products:
        if product["type"] == type_of:
            list.append(product)
    return list


def add_product(menu: list, **product):
    last_id = 0
    for item in menu:
        if item["_id"] > last_id:
            last_id = item["_id"]
    new_id = last_id + 1
    if len(menu) == 0:
        new_id = 1
    new_product = {"_id": new_id, **product}
    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)
    total_price = 0
    types = []
    counter_of_type = 0
    most_commmon_type = ""
    for product in products:
        price = product["price"]
        total_price += price
        types.append(product["type"])
    for type_of in types:
        total_types = types.count(type_of)
        if total_types > counter_of_type:
            counter_of_type = total_types
            most_commmon_type = type_of
    average_price = round(total_price / product_count, 2)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_commmon_type}"
