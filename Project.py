from __future__ import annotations
import random

Orders = []
Cash = 0

rest = 20
time = 50
Supplies = 100
class Worker():
    def __init__(self, name, job):
        """Super class for all worker classes

        Args:
            name (str): Who they are
            job (str): Work description
        """
        self.name = name
        self.energy = 100
        self.job = job
        
        

    def rest(self, energy):
        """Adds energy to all under the worker superclass

        Args:
            energy (int): How awake they are
        """
        self.energy += 20
        print(self.name + " took a well earned break, They now have "+ str(self.energy) + " energy")
        
    def OverTime(self, energy):
        """Add 30 extraturns

        Args:
            energy (int): How awake they are
        """
        self.energy -= 30
        print(self.name +  " had to work 30 more turns, they were happy...")
        

class Cook(Worker):
    def __init__(self, name, energy):
        super().__init__(name, energy)
        
    def Cooking(self, energy):
        """Cook food to later be served

        Args:
            energy (int): Energy used
        """
        self.energy -= 10
        print(self.name + " Made food (" + str(self.energy) + " energy)")

class Server(Worker):
    """_summary_

    Args:
        Worker (class): workers in "restaurant", player characters
    """
    def __init__(self, name, energy):
        super().__init__(name, energy)
    
    def ServeFood(self, energy):
        self.energy -= 5
        print(self.name + " Served some food (" + str(self.energy) + " energy)")
        

class Manager(Worker):
    def __init__(self, name, energy):
        super().__init__(name, energy)
    
    def Restock(self):
        self.energy -= 50
        print(self.name + " Ordered supplies for food (" + str(self.energy) + " energy)")

class Customer():
    def __init__(self, name):
        self.name = name
    
    def Order(Food):
        print("!!! A Customer Ordered " + Food + " !!!")
        Orders.append(Food)

Number = 0
HighCusNum = 0
Cook = Cook("Cook", 100)
Server = Server("Server", 100)
Manager = Manager("Manager", 150)
Cooked = []

while time != 0:
    if random.randint(1, 3) == 1:
        HighCusNum = Number + 1
        ThisCustomer = Customer("Customer_" + str(HighCusNum))
    
        Customer.Order(random.choice(["EGGS & BACON", "STEAK", "CHEESE BURGER", "LAMB", "FISH & CHIPS", "MEAT-EATERS SPECIAL", "PIZZA"]))
        

    print("(Cook, Serve, Rest, Restock, Overtime)")
    ACTION = input("Make a(n) action ")
    if ACTION.upper() == "COOK":
        if Cook.energy > 9:
            CookWhat = input("Cook What ?[Eggs & Bacon, Steak, Cheese Burger, Fish & Chips, etc]")
            Cooked.append(CookWhat.upper())
            Cook.Cooking(rest)
            if CookWhat.upper() == "EGGS & BACON":
                if Supplies > 4:
                    Supplies -= 5
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "STEAK":
                if Supplies > 1:
                    Supplies -= 2
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "CHEESE BURGER":
                if Supplies > 9:
                    Supplies -= 10
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "LAMB":
                if Supplies > 1:
                    Supplies -= 2
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "FISH & CHIPS":
                if Supplies > 2:
                    Supplies -= 3
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "MEAT-EATERS SPECIAL":
                if Supplies > 9:
                    Supplies -= 10
                else:
                    print("You couldn't make anything cause your out of supplies.")
            elif CookWhat.upper() == "PIZZA":
                if Supplies > 3:
                    Supplies -= 4
                else:
                    print("You couldn't make anything cause your out of supplies.")
            else:
                print("The cooks not sure what that is...")
                Cooked.remove(CookWhat.upper())
        else:
            print("The cook is to tired to make something, they need a rest")
    elif ACTION.upper() == "REST":
        Cook.rest(rest)
        Server.rest(rest)
        Manager.rest(rest)
    elif ACTION.upper() == "SERVE":
        if Server.energy > 4:
            ServeWhat = input("Serve What? ")
            Server.ServeFood(rest)
            if ServeWhat.upper() in Cooked:
                Orders.remove(ServeWhat.upper())
                Cooked.remove(ServeWhat.upper())
                Cash += 10 + random.randint(5, 20)
            else:
                print("!!! Customer was not happy being served what they did want. !!!")
        else:
            print("The server is to tired to make something, they need a rest")
    if ACTION.upper() == "RESTOCK":
        if Manager.energy > 49:
            Manager.Restock()
            Supplies += 10
    if ACTION.upper() == "OVERTIME":
        Cook.OverTime(rest)
        Server.OverTime(rest)
        Manager.OverTime(rest)
        time += 30
        
        


    time -= 1
    
    print(str(time) + " Turns left")
    print("People have ordered-------" + str(Orders) + "----------|")
    print("Inventory------------Food Cooked" + str(Cooked) + "---------Supplies left[" + str(Supplies) + "]------------------|")
    print("-----------------------------------|")
print("Wow what a great shift! you made $" + str(Cash))

if Cash > 50 and Cash < 100:
    print("Wow you can buy food today!")
elif Cash > 100 and Cash < 500:
    print("Wow! You can pay your employees today!")
elif Cash > 500 and Cash < 1000:
    print("Wow! You can pay rent tonight!")
elif Cash > 1000 and Cash < 2000:
    print("Wow! You made profit!")
elif Cash >  2000:
    print("Your Gonna go pro one day!")

Highscore = open("ScoreSave.txt", "w")
Highscore.write(Cash)
Highscore.close
