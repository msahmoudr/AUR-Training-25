from random import randint

class Employee:
    def __init__(self,name,family,manager= None):
        self._name = name
        self._family =family.copy()
        self._manager = manager
        self.salary= 2500
        self._ID =randint(1000,9999)

    @property
    def getID(self):
        return self._ID

    @property
    def getFamily(self):
        return self._family.copy()
    def getName (self):
        return self._name
    def getManager(self):
        return self._manager
    def setManager(self,str):
        self._manager=str
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary=salary

    def apply_raise(self, managed_employee: 'Employee', raise_percent: int):
        if managed_employee._manager ==self:

            R = managed_employee.getSalary() *raise_percent/ 100
            managed_employee.setSalary(managed_employee.getSalary() +R)

            print(f"New salary for {managed_employee._name} is {managed_employee.salary}")
            return True
        raise ValueError(f"{self._name} is not the manager of {managed_employee._name}")

if __name__ == '__main__':

    name = 'John Smith'
    family= {
    'Son': {
    'Insured': True,
    'Age': 16
    },
    'Wife': {
    'Insured': False,
    'Age': 32
    } }
    boss =Employee('AUR', {})
    my_employee = Employee(name,family, boss)
    not_boss = Employee('Adam Cater', {})


    print(my_employee.getSalary())
    boss.apply_raise(my_employee, 25)

    print(id(my_employee.getFamily))
    print(id(my_employee._family))
    boss.apply_raise(my_employee, 25)

    try:
        not_boss.apply_raise(my_employee, 25)
    except ValueError :
        print("Value error")

