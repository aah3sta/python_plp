#design your own class
class Smartphone:
    def __init__(self, model, year, make, colour):
        self.model = model
        self.year = year
        self.make = make
        self.colour = colour
        
    def phone_specs(self):
        print(f'I have a {self.model}, of the type {self.make}')
        
    def phone_deets(self):
        print(f'I bought it in {self.year}. It is {self.colour} in colour! I love it so much!!!')
        
class features(Smartphone):
    def __init__(self, model, year, make, colour, storage):
        super().__init__(model, year, make,colour)
        self.storage = storage
        
    def phone_features(self):
        print(f'My {self.model} has {self.storage} or storage space!')
    
phone = features('Samsung', 2024, 'A24', 'Silver', '128 GB')
phone.phone_specs()
phone.phone_deets()
phone.phone_features()
        
        
#polymorphism challenge
class Vehicle:
    def move(self):
        pass
    
class Car(Vehicle):
    def move(self):
        print('\nA car is Driving')
        
class Plane(Vehicle):
    def move(self):
        print('The plane is Flying')
        
class Boat(Vehicle):
     def move(self):
        print('The boat is Sailing')
        
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()    