from menu import Menu
class Resturent:
    def __init__(self,name):
        self.name=name
        self.employees=[] #here is our database
        self.menu=Menu()

    def add_empoloyee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print('-- Empoloyee List --')
        print(f'Name\t Phone\t Email\t Address')
        for emp in self.employees:
            print(f'{emp.name}\t {emp.phone}\t {emp.email}\t {emp.address}')