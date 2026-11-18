from enum import Enum


class ClothingType(Enum):
    SHIRT = "сорочка"
    JEANS = "джинси"
    JACKET = "куртка"
    SHOES = "взуття"
    HAT = "шапка"


SIZES = ["XS", "S", "M", "L", "XL", "XXL"]


class Clothing:
    def __init__(self, name, description, location, colour, size, type):
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self._size = size
        self.type = type

    def __del__(self):
        print(f"Об'єкт '{self.name}' видалено")

    def get_size(self):
        return self._size

    def set_size(self, size):
        if size in SIZES:
            self._size = size
        else:
            print("Такого розміру немає")

    def __str__(self): #всередині класу
        return f"{self.name}, {self.type.value}, {self.colour}, розмір {self._size}, {self.location}, {self.description}"

    def is_warm(self):
        return self.type in (ClothingType.JACKET, ClothingType.HAT)


class Wardrobe:
    def __init__(self):
        self.clothes = []

    def add(self, item):
        self.clothes.append(item)

    def remove(self, name):
        for item in self.clothes:
            if item.name == name:
                self.clothes.remove(item)
                return

    def show_all(self):
        for item in self.clothes:
            print(item)

    def sort_by_size(self):
        self.clothes.sort(key=lambda c: SIZES.index(c.get_size()))

    def are_go_out(self, clothes):
        types = []
        for c in clothes:
            if c.type not in types:
                types.append(c.type)
        count = len(types)
        print("Кількість типів одягу:", count)
        if count > 3:
            print("Готова вийти")
        else:
            print("Не готова вийти")


def main():
    shirt = Clothing("Сорочка", "бавовна", "полиця", "білий", "M", ClothingType.SHIRT)
    jeans = Clothing("Джинси", "прямі", "шафа", "синій", "L", ClothingType.JEANS)
    jacket = Clothing("Куртка", "зимова", "вішалка", "чорний", "S", ClothingType.JACKET)
    shoes = Clothing("Кросівки", "спортивні", "взуттєва шафа", "білий", "XL", ClothingType.SHOES)

    wardrobe = Wardrobe()
    wardrobe.add(shirt)
    wardrobe.add(jeans)
    wardrobe.add(jacket)

    wardrobe.sort_by_size()
    wardrobe.show_all()
    wardrobe.are_go_out(wardrobe.clothes)

    wardrobe.add(shoes)
    wardrobe.are_go_out(wardrobe.clothes)

    print(shirt)

    jacket.set_size("XL")
    print(jacket.get_size(), jacket.is_warm(), jeans.is_warm())

    wardrobe.remove("Джинси")
    wardrobe.show_all()


main()