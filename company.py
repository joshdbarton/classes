from employees import Employee


class Company():
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):

        return self.company_name

    def add_employee(self, customer):

        self.employees.add(customer)


bangazon = Company("bangazon", 1985)

wayne = Employee("Wayne", "lead guitar")
garth = Employee("Garth", "drummer")

bangazon.add_employee(wayne)
bangazon.add_employee(garth)

for employee in bangazon.employees:
    print(f"{employee.name}: {employee.title}")