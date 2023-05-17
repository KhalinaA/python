class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    
    def start(self):
        print("Автомобиль заведен")
        
    def stop(self):
        print("Автомобиль заглушен")
        
    def set_year(self, year):
        self.year = year
        
    def set_type(self, type):
        self.type = type
        
    def set_color(self, color):
        self.color = color



car = Car("green", "bmw", "2018")
print(car.start(), car.stop(), car.set_year('2018'), car.set_color('green'), car.set_type('bmw'))
print(car.year)