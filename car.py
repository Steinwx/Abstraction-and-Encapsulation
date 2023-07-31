import time

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed = max(0, self.__speed - 5)

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_year_model(self):
        return self.__year_model

    def set_year_model(self, year_model):
        self.__year_model = year_model

# Program to test the Car class
if __name__ == "__main__":
    car = Car(2023, "Subaru")

    print(f"Car Details - Make: {car.get_make()}, Year Model: {car.get_year_model()}")
    print("Initial speed:", car.get_speed())

    print("Accelerating...")
    for _ in range(5):
        car.accelerate()
        print(f"Make: {car.get_make()}, Year Model: {car.get_year_model()}, Current speed: {car.get_speed()}")
        time.sleep(1)  # Add a delay of 1 second between speed display

    print("Braking...")
    for _ in range(5):
        car.brake()
        print(f"Make: {car.get_make()}, Year Model: {car.get_year_model()}, Current speed: {car.get_speed()}")
        time.sleep(1)  # Add a delay of 1 second between speed display
