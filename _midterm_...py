class Building: #parent class for buildings
    def __init__(self): #constructor
        self._siding = "yes" #setting defalut value of siding to yes
    def getSiding(self): # method for getting siding
        return self._siding # returning siding
    def setSiding(self, siding): #method for Setting/updating siding
        self._siding = siding # upadating siding

class Room: #Room class to store info of a room
    def __init__(self, size, gas = "No", water = "No" ): #constructor with default values
        self._squareFeet = size #setting the size of room in sq feet
        self._gas = gas #setting value for gas
        self._water = water #setting value for water
    def getSquareFeet(self): #method for getting squareFeet
        return self._squareFeet #returning squareFeet
    def setSquareFeet(self, size): #method for setting squareFeet
        self._squareFeet = size #updating squareFeet
    
class House(Building): #House class inherited from building class
    def __init__(self): #constructor
        super().__init__() #inheriting properties of parent class
        self._rooms = [Room(0), Room(0), Room(0)] #setting 3 rooms with 0 size
        
    def setLivingRoom(self, roomsize): #method for setting Living Room size
        self._rooms[0] = Room(roomsize) #storing living room object in rooms list
    def setKitchen(self, roomsize): #method for setting Kitchen size
        self._rooms[1] = Room(roomsize, "Yes", "Yes") #storing kithen Room object in rooms list(need water and gas)
    def setDinning(self, roomsize): #method for setting Dinning room size
        self._rooms[2] = Room(roomsize, "No", "Yes")  #storing Dinning Room object in rooms list(need water only)
        
    def addBedRoom(self, roomsize): #method for adding bed rooms
        self._rooms.append(Room(roomsize))#adding new Room object to the rooms list

    def totalSquareFeet(self): #menthod to return total size of building
        sum = 0 #inital size taking 0
        for r in self._rooms: # loop to iterate over rooms list
            sum += r.getSquareFeet() #adding sie of each room to sum
        return sum #returning total size

class Commercial(Building): #Commertial class inherited from building class
    def __init__(self): #constructor
        super().__init__() #inheriting properties of parent class
        self._rooms = [] #taking empty list to store rooms data
        
    def addRoom(self, roomsize): #method for adding rooms
        self._rooms.append(Room(roomsize)) #adding new Room object to the rooms list
        
    def totalSquareFeet(self): #menthod to return total size of building
        sum = 0 #inital size taking 0
        for r in self._rooms: # loop to iterate over rooms list
            sum += r.getSquareFeet() #adding sie of each room to sum
        return sum #returning total size

#proving Polymorphism
def displayArea(building): #method for displaying the size of given building
    print("Area = ",building.totalSquareFeet(),"sq.feet") #printing size
    
h = House() #creating house object
lr = int(input("Enter Living Room Size(h): ")) #taking input for living room size
h.setLivingRoom(lr) #updating living room size
k = int(input("Enter Kitchen Size(h): ")) #taking input for kitchen size
h.setKitchen(k) #updating kitchen size
d = int(input("Enter Dinning Size(h): ")) #taking input for dinning size
h.setDinning(d) #updating dinning size
n = int(input("Enter no. of bed rooms(h): ")) #taking input for no. of bed rooms
for i in range(n): #loop iterate for n times
    b = int(input(" Enter bed room"+str(i+1)+" size(h): ")) #taking input for size of each bedroom
    h.addBedRoom(b) #adding the bedroom with given size

displayArea(h) #displaying total size of house h

c = Commercial() #creating Commertial object
m = int(input("\n\nEnter no. of rooms(c): "))#taking input for no. of rooms
for i in range(m): #loop iterate for m times
    r = int(input(" Enter room"+str(i+1)+" size(c): ")) #taking input for size of each room
    c.addRoom(r) #adding the room with given size
