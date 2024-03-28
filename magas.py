class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item, None)

    def update_price(self, item, price):
        if item in self.items:
            self.items[item] = price


stores = []

while True:
    store_name = input("Введите название магазина или введите 'end' для завершения создания: ")
    if store_name == 'end':
        break

    store_address = input("Введите адрес магазина: ")

    new_store = Store(store_name, store_address)

    while True:
        item = input("Введите наименование товара или 'end' для завершения ввода товаров: ")
        if item == 'end':
            break
        price = float(input("Введите цену товара: "))
        new_store.add_item(item, price)

    stores.append(new_store)

print("Список магазинов:")
for i, store in enumerate(stores):
    print(f"{i + 1}. {store.name} ({store.address})")

store_index = int(input("Выберите магазин по номеру: ")) - 1
chosen_store = stores[store_index]

print(f"Товары в магазине {chosen_store.name}:")
for item, price in chosen_store.items.items():
    print(f"{item}: {price}")

while True:
    action = input(
        "Выберите действие: 'добавь товар', 'обнови цену', 'убери товар', 'запроси цену', 'end' для выхода: ")

    if action == 'end':
        break
    elif action == 'добавь товар':
        new_item = input("Введите наименование нового товара: ")
        new_price = float(input("Введите цену нового товара: "))
        chosen_store.add_item(new_item, new_price)
    elif action == 'обнови цену':
        item = input("Введите наименование товара для обновления цены: ")
        new_price = float(input("Введите новую цену: "))
        chosen_store.update_price(item, new_price)
    elif action == 'убери товар':
        item = input("Введите название товара для удаления: ")
        chosen_store.remove_item(item)
    elif action == 'запроси цену':
        item = input("Введите название товара для запроса цены: ")
        price = chosen_store.get_price(item)
        if price is not None:
            print(f"Цена товара '{item}': {price}")
        else:
            print("Такого товара нет в ассортименте.")
####
while True:
    action = input(
        "Выберите действие: 'добавь товар', 'обнови цену', 'убери товар', 'запроси цену', 'вернуться к списку магазинов', 'выход': ")

    if action == 'вернуться к списку магазинов':
        print("Список магазинов:")
        for i, store in enumerate(stores):
            print(f"{i + 1}. {store.name} ({store.address})")
    elif action == 'выход':
        break
    else:
        if action == 'end':
            break
        elif action == 'добавь товар':
            new_item = input("Введите наименование нового товара: ")
            new_price = float(input("Введите цену нового товара: "))
            chosen_store.add_item(new_item, new_price)
        elif action == 'обнови цену':
            item = input("Введите наименование товара для обновления цены: ")
            new_price = float(input("Введите новую цену: "))
            chosen_store.update_price(item, new_price)
        elif action == 'убери товар':
            item = input("Введите название товара для удаления: ")
            chosen_store.remove_item(item)
        elif action == 'запроси цену':
            item = input("Введите название товара для запроса цены: ")
            price = chosen_store.get_price(item)
            if price is not None:
                print(f"Цена товара '{item}': {price}")
            else:
                print("Такого товара нет в ассортименте.")

        print(f"Обновленный список товаров в магазине {chosen_store.name}:")
        for item, price in chosen_store.items.items():
            print(f"{item}: {price}")