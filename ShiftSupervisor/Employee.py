class emp:
    def __init__(self,name,employee_num):
        self.__name = name
        self.__employee_num = employee_num
    #setters
    def setname(self,name):
        self.__name = name
    def setemplyeenumber(self,employee_num):
        self.__employee_num = employee_num
    #getters
    def getname(self):
        return self.__name
    def getemployeenumber(self):
        return self.__employee_num
