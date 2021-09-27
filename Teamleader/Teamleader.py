import ProductionWorker
class teamleader(ProductionWorker.productionworker):
    def __init__(self,name,employee_num,shift,pay_rate,monthly_bonus,required_Trainig_hours,attended_training_hours):
        ProductionWorker.productionworker.__init__(self,name,employee_num,shift,pay_rate)
        self.__monthly_bonus = monthly_bonus
        self.__required_Trainig_hours = required_Trainig_hours
        self.__attended_training_hours = attended_training_hours
    #setters
    def setmonthlybonus(self, monthly_bonus):
        self.__monthly_bonus = monthly_bonus
    def setrequiredtrainighours(self,required_Trainig_hours):
        self.__required_Trainig_hours = required_Trainig_hours
    def setattendedtrainghours(self, attended_training_hours):
        self.__attended_training_hours = attended_training_hours
    #getters
    def getmonthlybonus(self):
        return self.__monthly_bonus
    def getrequiredtraininghours(self):
        return self.__required_Trainig_hours
    def getattendedtrainghours(self):
        return self.__attended_training_hours
def main():
    print("Please enter your information.")
    print("------------------------------")
    name = input("Name:")
    emp_num = int(input("Employee Number:"))
    s  = shiftfunction()
    pay = float(input("Enter Payrate:"))
    bonus = input("Bonus:")
    required_Trainig_hours = input("Required Hours:")
    attended_training_hours = input("Attended Hours:")

    obj =teamleader("name","emp_num","s","Payrate","monthly_bonus","required_Trainig_hours","attended_training_hours")
    obj.setname(name)
    obj.setemplyeenumber(emp_num)
    obj.setshift(s)
    obj.setpayrate(pay)
    obj.setmonthlybonus(bonus)
    obj.setrequiredtrainighours(required_Trainig_hours)
    obj.setattendedtrainghours(attended_training_hours)


    #display
    print("\nDisplay information")
    print("______________________")
    print(f"Name:{obj.getname()}")
    print(f"Employee Number:{obj.getemployeenumber()}")
    print(f"shift:{obj.getshift()}")
    print(f"Payrate:{obj.getpayrate()}" )
    print(f"Monthly Bonus:{obj.getmonthlybonus()}")
    print(f"Required Hours:{obj.getrequiredtraininghours()}")
    print(f"Attended Hours:{obj.getattendedtrainghours()}")
    #will desplay the hours needed to meet the required hours or the overtime

    if  int(attended_training_hours) < int(required_Trainig_hours):
        print("You did not complete the hours.")
        short = int(required_Trainig_hours) - int(attended_training_hours)
        print(f"You were {short} hours short.")
    elif int(attended_training_hours) > int(required_Trainig_hours):
        print("You exceed your hours and made overtime.")
        over = int(attended_training_hours) - int(required_Trainig_hours)
        print(f"You overtime is {over} hours .")




#validation functions
def shiftfunction():
    shift = int(input("Enter shift:"))
    while shift < 1 or shift > 2:
        print("Invalid number. Try-agin ")
        print("1 - morning\n2- night ")
        shift = int(input("Enter shift:"))
    return shift




main()
