class Car:
    def __init__(self, make, model, year):
        if not isinstance(make, str) or not isinstance(model, str) or not isinstance(year, int):
            raise TypeError("Марка и модель должны быть строками, год должен быть целым числом")
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        if self.year < 2010:
            raise ValueError("Эта машина слишком старая, чтобы надежно заводиться")
        print(f"The {self.year} {self.make} {self.model} starts")

    def drive(self, distance):
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        print(f"The {self.year} {self.make} {self.model} приводы {distance} km")


class CarDealer:
    def __init__(self, cars):
        self.cars = cars

    def start_all_cars(self):
        for car in self.cars:
            try:
                car.start()
            except ValueError as e:
                print(f"Error starting {car.year} {car.make} {car.model}: {e}")

    def drive_all_cars(self, distance):
        for car in self.cars:
            try:
                car.drive(distance)
            except ValueError as e:
                print(f"Error driving {car.year} {car.make} {car.model}: {e}")


