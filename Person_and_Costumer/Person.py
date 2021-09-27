class per:
    def __init__(self,name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    #setter
    def setname(self,name):
        self.__name = name
    def setaddress(self,address):
        self.__address = address
    def setphone(self,phone):
        self.__phone = phone
    #getters
    def getname(self):
        return self.__name
    def getaddress(self):
        return self.__address
    def getphone(self):
        return self.__phone
