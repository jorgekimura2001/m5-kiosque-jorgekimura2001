from menu import products


def get_product_by_id(id: int) -> dict:

    product_found = {}
    for item in products:
        if item['_id'] == id:
            product_found = item

    return product_found


def get_products_by_type(type: str) -> list:

    products_found = []

    for item in products:
        if item['type'] == type:
            products_found.append(item)

    return products_found


def menu_report() -> str:

    menu_count_type = 0
    menu_name_type = ""
    menu_count = len(products)
    menu_sum = 0
    menu_type = {}
    for item in products:
        menu_sum += item['price']
    menu_average = round(menu_sum / menu_count, 2)
    for item in products:
        if not menu_type.get(item['type']):
            menu_type[item['type']] = 1
        else:
            menu_type[item['type']] += 1

    for key, value in menu_type.items():
        if value > menu_count_type:
            menu_name_type = key
            menu_count_type = value
    return f'Products Count: {menu_count} - Average Price: ${menu_average} - Most Common Type: {menu_name_type}'


def add_product(menu: list, **new_product) -> dict:
    new_id = len(menu) + 1
    new_product['_id'] = new_id
    menu.append(new_product)
    return new_product
