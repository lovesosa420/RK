from operator import itemgetter


class Book:
    """Книга"""

    def __init__(self, id, b_name, price, shop_id):
        self.id = id
        self.b_name = b_name
        self.price = price
        self.shop_id = shop_id


class Shop:
    """Магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookShop:
    """
    'Книга в магазине' для реализации
    связи многие-ко-многим
    """

    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id


# Магазины
shops = [
    Shop(1, 'центральный магазин'),
    Shop(2, 'магазин знаний'),
    Shop(3, 'дом книги'),
]

# Книги
books = [
    Book(1, 'Преступление и наказание', 500, 1),
    Book(2, 'На дне', 700, 2),
    Book(3, 'Мцыри', 450, 3),
    Book(4, 'Преступление и наказание', 480, 2),
    Book(5, 'На дне', 710, 3),
    Book(6, 'Мцыри', 465, 1),
    Book(7, 'Преступление и наказание', 480, 3),
    Book(8, 'На дне', 690, 1),
    Book(9, 'Мцыри', 445, 2),
]

books_shops = [
    BookShop(1, 1),
    BookShop(1, 6),
    BookShop(1, 8),
    BookShop(2, 2),
    BookShop(2, 4),
    BookShop(2, 9),
    BookShop(3, 3),
    BookShop(3, 5),
    BookShop(3, 7),
]


def main():
    one_to_many = [(b.b_name, b.price, s.name)
                   for s in shops
                   for b in books
                   if b.shop_id == s.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, b.shop_id, b.book_id)
                         for s in shops
                         for b in books_shops
                         if s.id == b.shop_id]

    many_to_many = [(b.b_name, b.price, shop_name)
                    for shop_name, shop_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все магазины
    for s in shops:
        # Список книг в магазине
        s_books = list(filter(lambda i: i[2] == s.name, one_to_many))
        # Если магазин не пустой
        if len(s_books) > 0:
            # Цены книг в магазине
            s_price = [price for _, price, _ in s_books]
            # Средняя цена книги в магазине
            s_price_sum_sr = sum(s_price)//len(s_books)
            res_12_unsorted.append((s.name, s_price_sum_sr))

    # Сортировка по средней цене
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все магазины
    for s in shops:
        if 'магазин' in s.name:
            # Список книг магазина
            s_books = list(filter(lambda i: i[2] == s.name, many_to_many))
            # Только название книг
            s_books_names = [x for x, _, _ in s_books]
            # Добавляем результат в словарь
            # ключ - магазин, значение - список названий книг
            res_13[s.name] = s_books_names

    print(res_13)


if __name__ == '__main__':
    main()
