from menu import products


def get_product_by_id(id):

    product_found = {}
    for item in products:
        if item['_id'] == id:
            product_found = item

    return product_found


def get_products_by_type(type):

    products_found = []

    for item in products:
        if item['type'] == type:
            products_found.append(item)

    return products_found


def menu_report():

    menu_count_type = 0
    menu_name_type = 0
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

    for index, item in enumerate(menu_type.items()):
        if item[1] > menu_count_type:
            menu_name_type = item[0]
            menu_count_type = item[1]
    return f'Products Count: {menu_count} - Average Price: {menu_average} - Most Common Type: {menu_name_type}'