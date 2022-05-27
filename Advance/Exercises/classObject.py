class Employee:
    def __init__(self, name="John", address="USA", level="Consultant"):  # instance method
        self.name = name
        self.address = address
        self.level = level

    id = 1  # class object

    @classmethod  # class method
    def get_id(cls):
        return cls.id

    def dis_info(self):
        print(Employee.get_id())
        print("Name:", self.name)
        print("Address:", self.address)
        print("Level:", self.level)


Emp1 = Employee("Carl", "Chicago", "Manager")
Emp1.dis_info()
