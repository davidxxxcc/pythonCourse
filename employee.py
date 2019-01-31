# A sample Employee class
import datetime

class Employee:
    # class variable
    raise_amt = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    """when there's no need to acccess the class or instance variables, then that's static method"""
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return'{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    # define method email as a attribute
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

""" Inheritance """
class Developer(Employee):
    raise_amt = 1.15
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"-->{emp.fullname}")

if __name__ == '__main__':
    dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
    dev_2 = Developer('Test', 'User', 60000, 'Java')
    dev_1.fullname = 'frank chang'
    print(dev_1.first)
    print(dev_1.email)
    print(dev_1.fullname)
    del dev_1.fullname


    # print(dev_1.__repr__())
    # print(dev_1.__str__())
    # print(dev_1 + dev_2)
    #
    # mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    # print(help(mgr_1))
    # print(mgr_1.email)
    # print(mgr_1.print_emps())
    # print(isinstance(mgr_1, Developer))
    # print(isinstance(mgr_1, Manager))
    # print(issubclass(Manager, Employee))
    # print(dev_1.email)
    # print(dev_1.prog_lang)


    # print(help(Developer))

    # print(dev_1)
    # print(dev_2)

    # my_date = datetime.date(2016, 7, 11)
    # print(Employee.is_workday(my_date))
    # emp_1.raise_amt = 1.01  # type: float
    # print(f"Empolyee.raise_amt: {Employee.raise_amt}")
    # print(f"emp_1.raise_amt: {emp_1.raise_amt}")
    # print(f"emp_2.raise_amt: {emp_2.raise_amt}")
    # print(f"Employee.num_of_emps: {Employee.num_of_emps}")
    #
    # Employee.set_raise_amt(1.09)
    # print(f"Empolyee.raise_amt: {Employee.raise_amt}")
    #
    # emp_str_1 = 'John-Doe-7000'
    # emp_str_2 = 'Steve-Smith-30000'
    # emp_str_3 = 'Jane-Doe-90000'
    #
    # new_emp_1 = Employee.from_string(emp_str_1)
    # print(new_emp_1)
    # print(new_emp_1.email)
    # print(new_emp_1.pay)
