products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

list_of_category = []
total_price = {}

for product in products:
    if product['category'] not in list_of_category:
        list_of_category.append(product['category'])

print("Total de precios por categoría:")

for category in list_of_category:
    for product in products:   
        if product['category'] == category:
            total_price = product['price']
    print(f"{category}: {total_price}")