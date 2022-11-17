from menu import products


def calculate_tab(table: list) -> dict:
    subtotal = 0
    for product in table:
        for item in products:
            if item['_id'] == product['_id']:
                subtotal += item['price'] * product['amount']
    return {'subtotal': f'${round(subtotal, 2)}'}
