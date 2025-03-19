class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_broken = False
        
    def breakDown(self):
        self.is_broken = True
    
    def displayInfo(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Broken: {self.is_broken}")
        
class ServiceCenter:
    def __init__(self, name):
        self.name = name
        
    def carRepair(self, car):
        car.is_broken = False
        
class Owner:  # Class name should start with uppercase, following Python naming convention
    def __init__(self, name):
        self.name = name
        self.cars = []
        
    def addCars(self, car):  # Corrected method name to match the correct capitalization
        self.cars.append(car)
        
    def sendCarsToServiceCenter(self, serviceCenter):
        print(f"{self.name} отправил следующие автомобили в сервисный центр {serviceCenter.name}:")
        for car in self.cars:  # Using self.cars instead of undefined 'cars'
            if car.is_broken:
                car.displayInfo()
                serviceCenter.carRepair(car)
        

# Создание экземпляров ServiceCenter и Car
bmwCenter = ServiceCenter("BMW Center")
car1 = Car("BMW", "E34", 1990)
car2 = Car("Ferrari", "Ferrari Roma", 2024)
car3 = Car("VW", "Polo", 1800)
car4 = Car("Toyota", "Corolla", 2020)

# Создание владельца и добавление автомобилей
MarkZuckerberg = Owner("Mark Zuckerberg")
MarkZuckerberg.addCars(car1)
MarkZuckerberg.addCars(car2)
MarkZuckerberg.addCars(car3)
MarkZuckerberg.addCars(car4)

# Симуляция поломки автомобилей
car1.breakDown()
car2.breakDown()

# Отправка автомобилей в сервисный центр
MarkZuckerberg.sendCarsToServiceCenter(bmwCenter)