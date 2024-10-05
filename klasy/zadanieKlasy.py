import os
import json
from typing import Any


class Employees:


    def __init__(self, file_name: str):
        #, employee_dict: dict[str, Any]
        #self.employee_data = {}
        self.employees_object_list = []
        self.file_name = file_name
        self.local_dir = r'C:\Users\turekp\Desktop\mentoring\AdventOfCode2022\pythonProject'
        self.file_path = os.path.join(self.local_dir, self.file_name)

        try:
            with open(self.file_path, 'r') as f:
                self.employee_data = json.load(f)
        except IOError:
            raise IOError("{} not found in {}".format(
                self.file_name, self.local_dir))

        for d in self.employee_data['employees']:
            e = Employee(d['name'], d['age'], d['salary'], d['department'], d.get('status', None))
            self.employees_object_list.append(e)


    # def load_object_list(self):
    #
    #     DB_load = Employee('Jsontest 1.json')
    #     data = DB_load.get_data()
    #     for d in data['employees']:
    #         e = Employee(d['name'], d['age'], d['salary'], d['department'], d.get('status', None))
    #         employees_object_list.append(e)
    #     for i in employees_object_list:
    #        return i

    def Avg_Salary(self):
        salary_sum = sum([employee_object.salary for employee_object in self.employees_object_list])
        number_of_employees = len(self.employees_object_list)
        return salary_sum / number_of_employees

    def list_of_employees(self, status: str):
        name_salary_tuple = [(employee_object.name, employee_object.salary) for employee_object in self.employees_object_list if employee_object.status == status]
        return name_salary_tuple
class Employee:
    def __init__(self, name: str, age: int, salary: int, department: str, status: str = None):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.status = status


    def __str__(self):
        return ('======================================\n' + \
                'Name: '+self.name + '\nAge:' + str(self.age)+ '\nSalary:' + str(self.salary)+ '\nDepartment:' \
                + self.department + '\nStatus:' + str(self.status)
                )



es = Employees('Jsontest 1.json')
print(es.Avg_Salary())
print(es.list_of_employees('False'))

for x in es.employees_object_list:
    print(x)

    #funkcja aktywująca pracownika
    #ustawia status
    #mowi w swoim jezyku





