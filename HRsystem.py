
# Online Python - IDE, Editor, Compiler, Interpreter

class employee:
    def __init__(self,empl_id,name):
        self.empl_id=empl_id
        self.name=name
        
class salaryEmployee(employee):
    def __init__ (self,empl_id,name,weekly_salary):
        super(). __init__(empl_id,name)
        self.weekly_salary=weekly_salary
    def calculatePayroll():
        return weekly_salary
class hourlyEmployee(employee):
    def __init__(self,empl_id,name, hours_worked, hourly_rate ):
        super(). __init__(empl_id,name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate
    def calculatePayroll():
        return hours_worked*hourly_rate
class commisionEmployee(salaryEmployee):
    def __init__(self,empl_id,name,weekly_salary,commision_value):
        super(). __init__(empl_id,name,weekly_salary)
        self.commision_value=commision_value
        def calculatePayroll():
            return weekly_salary + commision_value


