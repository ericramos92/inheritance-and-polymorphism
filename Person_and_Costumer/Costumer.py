import Person
class cost(Person.per):
    def __init__(self,name, address, phone,comprador,mail):
        Person.per.__init__(self,name, address, phone)
        self.comprador = comprador
        self.mail = mail

    def setcomprador(self,comprador):
        self.comprador = comprador
    def setmail(self,mail):
        self.mail = mail

    def getcomprador(self):
        return self.comprador
    def getmail(self):
        return self.mail
    def __str__(self):
        return "Name:"+Person.per.getname(self) +\
                "\nAddress:"+Person.per.getaddress(self) +\
                "\nPhone:"+Person.per.getphone(self) +\
                "\nCostumer Number:"+cost.getcomprador(self) + \
                "\nMailing:" + cost.getmail(self)






def main():
    name = input("Name:")
    address = input("Address:")
    phone = input("Phone:")
    costumer = input("Costumer Number:")
    mailing =input("Would you like to get mailing?(Y or N)")
    obj = cost(name,address,phone,costumer,mailing)


    print("      Dispaly       ")
    print("--------------------")
    print(obj)


main()
