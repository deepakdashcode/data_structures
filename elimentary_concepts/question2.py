def Push(Package: list):
    EmpId = int(input('Enter the employee id\n'))
    Ename: str = input('Enter the name of employee\n')
    Salary = int(input('Enter the salary of the employee\n'))
    current_employee = (EmpId, Ename, Salary)
    Package.append(current_employee)


def Pop(Package: list):
    if len(Package) == 0:
        print('Underflow')
    else:
        Package.pop()

Package=[]
Push(Package)
print(Package)