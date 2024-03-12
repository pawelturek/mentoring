from typing import Any


class Employee:
    name:str='Bob'
    age:int
    salary:int
    department:str
    status:str = None

    def __init__(self, slownik:dict[str, Any]):

        self.name = slownik['name']
        self.age = slownik['age']
        self.salary = slownik['salary']
        self.department = slownik['department']


E = Employee({"name": "Jane Smith",
      "age": 28,
      "department": "Sales",
      "salary": 40000})
Employee.name='Jane'
print(E.name)

def showE():
    E = 10
    print(E)

showE()
print(E.name)
