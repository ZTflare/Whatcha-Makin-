

rest = 20
time = 50
class Worker():
    def __init__(self, name, job):
        self.name = name
        self.energy = 100
        self.job = job

    def rest(self, energy):
        self.energy += 20
        print(self.name + " took a well earned break, They now have "+ str(self.energy) + " energy")

class Cook(Worker):
    def __init__(self, name, energy):
        super().__init__(name, energy)
    
    def Cooking(self, energy):
        self.energy -= 10
        print(self.name + " Made food (" + str(self.energy) + " energy)")

class Server(Worker):
    def __init__(self, name, energy):
        super().__init__(name, energy)
    
    def ServeFood(self, energy):
        self.energy -= 5
        print(self.name + " Served some food (" + str(self.energy) + " energy)")

Cook = Cook("Cook", 100)
Server = Server("Server", 100)

while 1 != 0:
    print("(Cook, Serve, Take order, Rest)")
    ACTION = input("Make a(n) action ")
    if ACTION == "Cook":
        Cook.Cooking(rest)
    elif ACTION == "Rest":
        Cook.rest(rest)

    time -= 1
    print(str(time))