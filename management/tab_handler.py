from .product_handler import get_product_by_id


def calculate_tab(table):
    calculate = 0
    for item in table:
        product = get_product_by_id(item["_id"])
        price = product["price"]
        amount = item["amount"]
        calculate += price * amount
    total = {"subtotal": f"${round(calculate,2)}"}
    return total
