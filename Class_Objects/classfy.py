class Employee:
#constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")
emp.display()
try:
    print(emp.id)
except NameError:
    print("emp id not defined")
del emp
try:
    emp.display()
except NameError:
    print("employee not defined")
