# Define a class called 'Car'
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine has started.")

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Access methods using the objects
car1.display_info()
car1.start_engine()

car2.display_info()
car2.start_engine()
