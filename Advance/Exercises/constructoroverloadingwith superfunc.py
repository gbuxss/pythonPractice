class Employee:

    def __init__(self, name, job, address):
        self.name = name
        self.job = job
        self.address = address

    def disp_info(self):
        print(self.name, self.job, self.address)


class Manager(Employee):
    def __init__(self, name, job, address, salary):
        super().__init__(name, job, address)
        self.salary = salary

    def show_salary(self):
        print(self.salary)
        super().disp_info()


e = Employee("jack", "Manager", "USA")
m = Manager(name="Jon", job="operator", address="chicago", salary="5000")
m.show_salary()
e.disp_info()

