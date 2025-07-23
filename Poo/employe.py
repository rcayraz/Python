class Employee:
    """
    A class to represent an Employee.
    Attributes
    ----------
    name : str
        name of the employee
    salary : float
        salary of the employee
    Methods
    -------
    display():
        Prints the name and salary of the employee.
    apply_raise(percentage):
        Applies a raise to the employee's salary based on the given percentage.
    get_salary:
        Property that returns the current salary of the employee.
    set_salary(new_salary):
        Property setter that sets a new salary for the employee, ensuring it is not negative.
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name, ", Salary:", self.salary)

    def apply_raise(self, percentage):
        self.salary = self.salary + (self.salary * percentage / 100)
    
    @property
    def get_salary(self):
        return self.salary
    
    @get_salary.setter
    def set_salary(self, new_salary):
        if new_salary < 0:
            print("The salary can't be negative")
        else:
            self.salary = new_salary



employee1 = Employee("John", 1000)
employee1.display()
employee1.apply_raise(10)
employee1.display()

employee1.set_salary = -1000  # Muestra el mensaje, pero no cambia el salario

print(employee1.get_salary)


employee1.set_salary = 500   
employee1.display()
