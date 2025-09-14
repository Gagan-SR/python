# Function definition
def greet(name):
    """
    This function takes a name as input
    and prints a greeting message.
    """
    print(f"Hello, {name}!")

# Function with return value
def add_numbers(a, b):
    """
    This function takes two numbers as input
    and returns their sum.
    """
    return a + b

# Calling the functions
greet("Gagan")

result = add_numbers(5, 10)
print("Sum:", result)

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(4))       # 4^2 = 16
print("Power:", power(2, 3))    # 2^3 = 8

# Function with variable number of arguments
def add_all(*numbers):
    return sum(numbers)

print("Sum of all numbers:", add_all(1, 2, 3, 4, 5))
