market = [
    {"id": 123456, "product": "coca-cola 0.5", "department": "drinks", "price": 1.5, "quantity": 100},
    {"id": 234567, "product": "lays chips", "department": "snacks", "price": 1.0, "quantity": 50},
    {"id": 345678, "product": "apple", "department": "fruits", "price": 0.5, "quantity": 200}
]

# Вывод информации о всех товарах
def display_all_products():
    for product in market:
        print(product)

# Вывод информации о товаре по номеру
def display_product_by_id(product_id):
    for product in market:
        if product["id"] == product_id:
            print(product)
            return
    print("Товар с таким номером не найден")

# Вывод количества товаров, продающихся в определенном отделе
def count_products_by_department(department_name):
    count = 0
    for product in market:
        if product["department"] == department_name:
            count += 1
    print(f"Количество товаров в отделе {department_name}: {count}")

# Обновление информации о товаре по номеру
def update_product_by_id(product_id, new_info):
    for product in market:
        if product["id"] == product_id:
            product.update(new_info)
            return
    print("Товар с таким номером не найден")

# Удаление товара по номеру
def delete_product_by_id(product_id):
    for product in market:
        if product["id"] == product_id:
            market.remove(product)
            return
    print("Товар с таким номером не найден")
