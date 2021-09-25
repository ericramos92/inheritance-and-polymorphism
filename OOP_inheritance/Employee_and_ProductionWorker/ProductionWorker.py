import Employee
class productionworker(Employee.emp):
    def __init__(self,name,employee_num,shift,pay_rate):
        Employee.emp.__init__(self,name,employee_num)  #inheritance from super class
        self.__shift = shift
        self.__pay_rate = pay_rate
        #setters
    def setshift(self,shift):
        self.__shift = shift
    def setpayrate(self, pay_rate):
        self.__pay_rate = pay_rate
        #getters
    def getshift(self):
        if self.__shift == 1:
            return "Mornig shift"
        elif self.__shift ==2:
            return "Night shift"
    def getpayrate(self):
        return self.__pay_rate
def main():
    print("Please enter your information.")
    print("------------------------------")
    name = input("Name:")
    emp_num = int(input("Employee Number:"))
    s  = shiftfunction()
    pay = float(input("Enter Payrate:"))

    obj =productionworker("name","emp_num","s","Payrate")
    obj.setname(name)
    obj.setemplyeenumber(emp_num)
    obj.setshift(s)
    obj.setpayrate(pay)

    #display
    print("\nDisplay information")
    print("______________________")
    print(f"Name:{obj.getname()}")
    print(f"Employee Number:{obj.getemployeenumber()}")
    print(f"shift:{obj.getshift()}")
    print(f"Payrate:{obj.getpayrate()}" )
#validation functions
def shiftfunction():
    shift = int(input("Enter shift:"))
    while shift < 1 or shift > 2:
        print("Invalid number. Try-agin ")
        print("1 - morning\n2- night ")
        shift = int(input("Enter shift:"))
    return shift

main()
