import os
import json
from typing import Any


class Employee:
    name: str='Bob'
    age: int
    salary: int
    department: str
    status: str = None

    def __init__(self, file_name: str, name: str = None, age: int = None, salary: int = None, department: str = None, status: str = None):
        #, employee_dict: dict[str, Any]
        self.employee_list = []
        self.file_name = file_name
        self.local_dir = r'C:\Users\turekp\Desktop\mentoring\AdventOfCode2022\pythonProject'
        self.file_path = os.path.join(self.local_dir, self.file_name)

        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.status = status

        try:
            with open(self.file_path, 'r') as f:
                self.employee_list = json.load(f)
        except IOError:
            raise IOError("{} not found in {}".format(
                self.file_name, self.local_dir))

    #def get_data(self):
    #    return self.employee_list

    def __str__(self):
        return ('======================================\n' + \
                'Name: '+self.name + '\nAge:' + str(self.age)+ '\nSalary:' + str(self.salary)+ '\nDepartment:' \
                + self.department + '\nStatus:' + str(self.status)
                )

    def load_object_list(self):
        final_list = []
        for d in self.employee_list['employees']:
            e = Employee('Jsontest 1.json', d['name'], d['age'], d['salary'], d['department'])
            final_list.append(e)

    def print_object_list(self):
        for e in self.final_list:
            return e

F = Employee('Jsontest 1.json')
F.load_object_list()
print(F.print_object_list())