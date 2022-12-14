from menu import products


def get_product_by_id(id: int) -> dict:
    if type(id) == int:
        product_found = {}
        for item in products:
            if item['_id'] == id:
                product_found = item

        return product_found
    
    raise TypeError('product id must be an int')


def get_products_by_type(product_type: str) -> list:
    if type(product_type) == str:
        products_found = []

        for item in products:
            if item['type'] == product_type:
                products_found.append(item)

        return products_found

    raise TypeError('product type must be a str')


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


def add_product(menu: list, **new_product: dict) -> dict:
    new_id = len(menu) + 1
    new_product['_id'] = new_id
    menu.append(new_product)
    return new_product


def add_product_extra(menu: list, *args: tuple, **new_product: dict) -> dict:

    product_correct = new_product.copy()

    for key in new_product.keys():
        if key not in args:
            product_correct.pop(key)

    for required in args:
        if required not in product_correct:
            raise KeyError(f'field {required} is required')

    print(product_correct)
    new_id = len(menu) + 1
    product_correct['_id'] = new_id
    menu.append(product_correct)
    return product_correct