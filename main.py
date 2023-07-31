import time
from car import Car

# Program to test the Car class
if __name__ == "__main__":
    car = Car(2022, "Example Make")

    print("Initial speed:", car.get_speed())

    print("Accelerating...")
    for _ in range(5):
        car.accelerate()
        print("Current speed:", car.get_speed())
        time.sleep(1)  # Add a delay of 1 second between speed display

    print("Braking...")
    for _ in range(5):
        car.brake()
        print("Current speed:", car.get_speed())
        time.sleep(1)  # Add a delay of 1 second between speed display