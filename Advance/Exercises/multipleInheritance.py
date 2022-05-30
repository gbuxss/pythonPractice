class Electronics:
    def __init__(self, catagory, brand):
        self.catagory = catagory
        self.brand = brand

    def show_info(self):
        print("Catagory:", self.catagory)
        print("Brand:", self.brand)


class Television(Electronics):
    def __init__(self, catagory, brand, price):
        super().__init__(catagory, brand)
        self.price = price

    def show_tv_info(self):
        super().show_info()
        print("Price:", self.price, )


class Computer(Television):
    def __init__(self, catagory, brand, price, comp_type="Laptop"):
        super().__init__(catagory, brand, price)
        self.comp_type = comp_type

    def __repr__(self):
        print(self.catagory)
        print(self.brand)
        print(self.comp_type)
        print(self.price)


t = Television("Television", "Samsung", "$1250.45")
t.show_tv_info()

c = Computer("Computer", "Dell", "$1999.99")
c.__repr__()
