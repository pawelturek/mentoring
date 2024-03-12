import json
#name i salary wyprintowac jako lista tupli

def GetNamesSalariesFromJson(filePath:str) -> list[tuple[str,str]]:
    data_list = []
    data_tuple = ()
    with open(filePath, "r") as f:
        data = json.load(f)
        return [(d["name"], d["salary"]) for d in data['employees']]

def ShowEmployeesStatus(filePath:str, statusFilter:str) -> list[str]:
    with open(filePath, "r") as f:
        data = json.load(f)
        return [d['name'] for d in data['employees'] if 'status' in d and d["status"] == statusFilter]


def AvgEmployeesAge(filePath:str) -> list[str]:
    salarySum = []
    numberOfEmployees = 0
    with open(filePath, "r") as f:
        data = json.load(f)
    salarySum = [d['age'] for d in data['employees']]
    numberOfEmployees = len(data['employees'])
    return sum(salarySum)/numberOfEmployees


def AddEmployee(filePath:str, filePathtoSave:str):
    EmployeesList = []
    with open(filePath, "r") as f:
            EmployeesList = json.load(f)
        print(type(EmployeesList['employees']))
        EmployeesList['employees'].append(
            {
                "name": "Bob Johnson",
                "age": 22,
                "department": "Driver",
                "salary": 30000,
                "status": "False",
                "project": {
                    "name": "Project Drive",
                    "start_date": "2020-01-01",
                    "end_date": "2023-12-31"
                }
            }
        )

        with open(filePathtoSave, 'w') as f:
            json.dump(EmployeesList, f,
                        indent=4)
        result_set = set()

        # for employee in EmployeesList['employees']:
        #    print('to jest employee: ',employee['name'])
        #    result_set.add(employee['name'])
        listD = set([d["name"] for d in EmployeesList['employees']])
        print('zbior: ',listD)



print(GetNamesSalariesFromJson('Jsontest 1.json'))
print(ShowEmployeesStatus('Jsontest 1.json', "False"))
print(AvgEmployeesAge('Jsontest 1.json'))
AddEmployee('Jsontest 1.json','Jsontest 2.json')
