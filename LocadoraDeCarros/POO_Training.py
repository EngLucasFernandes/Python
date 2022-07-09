def menu():

    print("=" * 100)
    print("[1] Add a car")
    print("[2] Remove a car")
    print("[3] List all cars")
    print("[4] Exit")
    print("=" * 100)

    user_option = input("Enter a valid option: ")
    print()

    return user_option


class Car:

    total_cars = 0

    def __init__(self):
        self._model = ""
        self._brand = ""
        self._color = ""
        self.on = False
        self.velocity = 0

    def set_info(self):
        self._model = input("Enter your car's model: ")
        self._brand = input("Enter your car's brand: ")
        self._color = input("Enter your car's color: ")
        Car.total_cars += 1

    def get_model(self):
        return self._model

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def accelerate(self):
        self.velocity += 10

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color


cars = []

print("Python Code Made By EngLucasFernandes!")
print("Version 1.0.0")
print()

while True:

    user_input = menu()

    while user_input not in ["1", "2", "3", "4"]:
        print("Invalid option!")
        user_input = menu()

    if user_input == "1":

        user_car = Car()
        user_car.set_info()
        cars.append(user_car)

        print()
        print("Added!")
        print()

    elif user_input == "2":

        if cars == []:

            print()
            print("No cars!")
            print()

        else:

            car_number = 1

            print()
            print("\nCars: \n")

            for car in cars:
                print(f"[{car_number}]\t {car.get_model()}")
                car_number += 1

            print()
            remove_car = int(input("Enter the car's number to remove: "))
            print()

            while remove_car not in [i for i in range(0, len(cars) + 1)]:

                print("Invalid option!")
                remove_car = input("Enter the car's number to remove: ")

            cars.pop(int(remove_car) - 1)

            print()
            print("Removed!")
            print()

    elif user_input == "3":

        if cars == []:

            print()
            print("No cars!")
            print()

        else:

            print()
            print("\nCars: \n")

            for car in cars:

                print(f"\t {car.get_model()}")
                print()

            print()

    elif user_input == "4":
        break
