# 1. Class and Object
class Animal:
    # Constructor (__init__)
    def __init__(self, name, sound):
        self.name = name        # attribute
        self.sound = sound

    # Method
    def speak(self):
        return f"{self.name} says {self.sound}"


# 2. Inheritance
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # call parent constructor
        self.breed = breed

    # Polymorphism (same method name, but different behavior)
    def speak(self):
        return f"{self.name} ({self.breed}) barks: {self.sound}"


# 3. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}, New Balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount}, New Balance: {self.__balance}"
        else:
            return "Insufficient funds!"

    def get_balance(self):
        return self.__balance


# --- Using the classes ---

# Object creation
cat = Animal("Cat", "Meow")
print(cat.speak())  # Cat says Meow

dog = Dog("Tommy", "Labrador")
print(dog.speak())  # Tommy (Labrador) barks: Woof

# Encapsulation
account = BankAccount("Alice", 1000)
print(account.deposit(500))   # Deposited 500
print(account.withdraw(200))  # Withdrawn 200
print(account.get_balance())  # Balance check
