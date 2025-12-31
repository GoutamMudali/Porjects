import uuid

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.hp = horsepower
        self.fuel = fuel_type
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Engine vrooming..."

class Vehicle:
    total_vehicles_created = 0  

    def __init__(self, brand, model, engine):
        self.vin = uuid.uuid4().hex[:8] 
        self.brand = brand
        self.model = model
        self.engine = engine  
        Vehicle.total_vehicles_created += 1

    @property
    def description(self):
        """Dynamic property: calculates string on the fly"""
        return f"{self.brand} {self.model} (VIN: {self.vin})"

    @staticmethod
    def validate_vin(vin):
        return len(vin) == 8

class Truck(Vehicle):
    def __init__(self, brand, model, engine, cargo_capacity):
        super().__init__(brand, model, engine)
        self.capacity = cargo_capacity
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight <= self.capacity:
            self.current_load += weight
        else:
            print("Overload warning!")

class FleetManager:
    def __init__(self, name):
        self.name = name
        self.__vehicles = [] 

    def __len__(self):
        return len(self.__vehicles)

    def __getitem__(self, position):
        return self.__vehicles[position]

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.__vehicles.append(vehicle)
        else:
            raise TypeError("Only Vehicle instances can be added.")


v8_engine = Engine(450, "Gasoline")

my_truck = Truck("Ford", "F-150", v8_engine, 2000)
my_car = Vehicle("Tesla", "Model 3", Engine(280, "Electric"))

my_fleet = FleetManager("City Logistics")
my_fleet.add_vehicle(my_truck)
my_fleet.add_vehicle(my_car)

print(f"Manager: {my_fleet.name}")
print(f"Fleet Size: {len(my_fleet)}") 
print(f"First Vehicle: {my_fleet[0].description}")  
print(f"Engine Status: {my_fleet[0].engine.start()}") 