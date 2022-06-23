class Electronics:
    def __init__(self, category, brand):
        self.category = category
        self.brand = brand

    def show_info(self):
        print("Category:", self.category)
        print("Brand:", self.brand)


class Television(Electronics):
    def __init__(self, category, brand, price):
        super().__init__(category, brand)
        self.price = price

    def show_tv_info(self):
        super().show_info()
        print("Price:", self.price, )


class Computer(Television):
    def __init__(self, category, brand, price, comp_type="Laptop"):
        super().__init__(category, brand, price)
        self.comp_type = comp_type

    def __repr__(self):
        print(self.category)
        print(self.brand)
        print(self.comp_type)
        print(self.price)


t = Television("Television", "Samsung", "$1250.45")
t.show_tv_info()

c = Computer("Computer", "Dell", "$1999.99")
c.__repr__()
