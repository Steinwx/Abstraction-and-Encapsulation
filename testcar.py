import time
from car import Car

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
