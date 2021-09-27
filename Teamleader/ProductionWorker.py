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
