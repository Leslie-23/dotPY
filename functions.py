# Filename: all_types_of_functions.py

# 1. Basic Function
def greet():
    print("Hello, World!")

# 2. Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")

# 3. Function with Default Parameters
def greet_person_with_default(name="Stranger"):
    print(f"Hello, {name}!")

# 4. Function with Variable-Length Arguments (*args)
def greet_multiple_people(*names):
    for name in names:
        print(f"Hello, {name}!")

# 5. Function with Keyword Arguments (**kwargs)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# 6. Lambda Function
add = lambda x, y: x + y

# 7. Nested Function
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

# 8. Recursive Function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 9. Function with Return Value
def square(number):
    return number * number

# 10. Function with Annotations
def greet_with_annotations(name: str) -> str:
    return f"Hello, {name}!"

# Main block to demonstrate the functions
if __name__ == "__main__":
    # Basic Function
    greet()

    # Function with Parameters
    greet_person("Alice")

    # Function with Default Parameters
    greet_person_with_default()
    greet_person_with_default("Bob")

    # Function with Variable-Length Arguments
    greet_multiple_people("Alice", "Bob", "Charlie")

    # Function with Keyword Arguments
    display_info(name="Alice", age=30, city="New York")

    # Lambda Function
    result = add(5, 3)
    print(f"Sum: {result}")

    # Nested Function
    outer_function("This is a nested function")

    # Recursive Function
    result = factorial(5)
    print(f"Factorial: {result}")

    # Function with Return Value
    result = square(4)
    print(f"Square: {result}")

    # Function with Annotations
    message = greet_with_annotations("Alice")
    print(message)
