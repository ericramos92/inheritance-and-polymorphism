import Employee
class supervisor(Employee.emp):
    def __init__(self,name,employee_num,annual_salary,bonus):
        Employee.emp.__init__(self,name,employee_num)
        self.annual_salary = annual_salary
        self.bonus = bonus

    #setters
    def setannual_salary(self,annual_salary):
        self.annual_salary = annual_salary
    def setbonus(self, bonus):
        self.bonus = bonus
    #getters
    def getannual_salary(self):
        return self.annual_salary
    def getbonus(self):
        return self.bonus
    #display
    def __str__(self):
        return 'Name:' + Employee.emp.getname(self)+ \
                '\nEmployee Number: ' + str(Employee.emp.getemployeenumber(self)) + \
                '\nAnnual Salary: ' + str(self.annual_salary) + \
                '\nbonus: ' + str(self.bonus)

def main():
    print("Please enter your information.")
    print("------------------------------")
    name = input("Name:")
    emp_num = int(input("Employee Number:"))
    annual_salary = int(input("Enter Annual Salary:"))
    bonus = float(input("Enter Bonus:"))
    #create object to access classes
    obj = supervisor(name,emp_num,annual_salary,bonus)
    print("          display         ")
    print("--------------------------")
    print(obj)





main()
