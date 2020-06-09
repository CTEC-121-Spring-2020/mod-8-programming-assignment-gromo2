# Module 8
#   Programming Assignment 11
#     Prob-1.py

class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    def set_make(self, make):
        self._make = make

    def get_make(self):
        return self._make

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

def TestCar():
    car1 = Car('Chevorlet', 'Sonora', '2006')
    car2 = Car('Triumph', 'Tiger', '2004')
    car3 = Car('Lexus', 'GS460', '2008')
    car4 = Car('Kia', 'Borrego', '2009')
    car5 = Car('Suzuki', 'GZ250', '2001')
    carLot = [car1, car2, car3, car4, car5]
    for car in carLot:
        print("Make: ", car._make, "  ", "Model: ", car._model, "  ", "Year: ", car._year)
    for car in carLot:
        car.set_make(str(input("Enter a new make for the car: ")))
        car.set_model(str(input("Enter a new model for the car: ")))
        car.set_year(int(input("Enter a new year for the car: ")))
    for car in carLot:
        print("Make: ", car._make, "  ", "Model: ", car._model, "  ", "Year: ", car._year)
        
if __name__ == "__main__":
    TestCar()