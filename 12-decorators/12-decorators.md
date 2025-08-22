# **Python Decorators: The Agent's Disguise 🎭**

Welcome to your next briefing, Junior Agent\! Today's topic is **decorators**, a powerful and elegant feature in Python. A decorator is a function that takes another function as an argument, adds some new functionality to it, and returns the modified function. Think of a decorator as a master of disguise: it wraps an agent (a function) in new clothes, allowing them to perform their mission with added capabilities like a silent walk or night vision, without changing their core identity.

Decorators are particularly useful for adding functionality to existing functions without modifying their source code. Common uses include logging, timing function execution, enforcing security, and pre- or post-processing data.

-----

## **1. The Basic Decorator: A Function That Wraps Another**

At its core, a decorator is a function that takes a function as input and returns a new function. The inner function, often called `wrapper`, is the one that contains the new logic and calls the original function.

**Example Code:**

```python
# The decorator function
def new_feature_decorator(func):
    def wrapper():
        print("Adding a new feature before the main task.")
        func()  # Call the original function
        print("New feature completed after the main task.")
    return wrapper

# The function to be decorated
def main_task():
    print("Performing the main task.")

# Decorate the function manually
# This is what the @ syntax does behind the scenes
decorated_task = new_feature_decorator(main_task)
decorated_task()
```

-----

## **2. The `@` Syntax: Python's Syntactic Sugar**

Python provides a special syntax, the `@` symbol, to make using decorators much cleaner and more readable. Placing `@decorator_name` directly above a function definition is a shorthand for `my_function = decorator_name(my_function)`.

**Example Code:**

```python
# The decorator function
def log_execution_time(func):
    def wrapper():
        import time
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Function took {end_time - start_time:.4f} seconds to execute.")
    return wrapper

# Use the @ syntax to decorate the function
@log_execution_time
def perform_complex_operation():
    print("Executing complex operation...")
    for _ in range(10000000):
        pass # Simulate a long task

perform_complex_operation()
```

-----

## **3. Decorators with Arguments: Handling Parameters**

What if the function you want to decorate takes arguments? The inner `wrapper` function must be able to accept these arguments and pass them along to the original function. We use `*args` and `**kwargs` to handle any number of positional and keyword arguments.

**Example Code:**

```python
def check_clearance(func):
    def wrapper(*args, **kwargs):
        # We assume the clearance level is the first argument
        clearance_level = args[0]
        if clearance_level >= 5:
            print("Clearance accepted. Granting access.")
            return func(*args, **kwargs)
        else:
            print("Clearance too low. Access denied.")
            return None # Or raise an error
    return wrapper

@check_clearance
def access_secure_intel(level, file_name):
    print(f"Accessing {file_name} with clearance level {level}.")
    return f"Data from {file_name}"

# Call the decorated function with different arguments
access_secure_intel(6, "Project_Nova_Data")
print("-" * 20)
access_secure_intel(3, "Project_Nova_Data")
```

-----

## **Hands-On Exercises: Disguise Puzzles 🧩**

It's time to build your own functional disguises and automate tasks.

### **1. Basic Decorators (5 Exercises)**

1.  **A Simple Spy Decorator:** Write a decorator `spy_mode_on` that prints `"Entering stealth mode..."` before calling the decorated function and `"Exiting stealth mode."` after.
2.  **Decorate a Function:** Define a function `infiltrate_base()` that prints `"Infiltrating the base."`. Apply your `spy_mode_on` decorator to it using the `@` syntax.
3.  **Confirming Mission:** Write a decorator `confirm_mission` that prints `"Mission confirmed."` before the function call. Create a function `execute_mission()` that prints `"Executing primary mission."` and apply the decorator.
4.  **Logging a Function Call:** Write a decorator `log_call` that prints `f"Calling {func.__name__}..."` before the function is executed. Apply it to a simple function `get_intel()`.
5.  **A Countdown:** Write a decorator `countdown_timer` that prints `3... 2... 1...` before executing a function. Apply it to a function `launch_drone()`.

### **2. Decorators with Arguments (5 Exercises)**

1.  **Authorization Check:** Write a decorator `authorize(func)` that takes a function with one argument (`level`). Inside the `wrapper`, check if `level` is `>= 10`. If so, call the original function; otherwise, print `"Insufficient authorization."`.
2.  **Test the Decorator:** Define a function `view_top_secret_file(level)` that prints `"Accessing top secret file."`. Apply your `authorize` decorator and test it with an argument of `12` and then with `8`.
3.  **Validate Arguments:** Write a decorator `validate_input(func)` that takes a function with one argument (`data`). Inside the `wrapper`, check if `data` is not `None` and is a string. If the check passes, call the function; otherwise, print `"Invalid input."`.
4.  **Test the Validator:** Define a function `process_data(data)` that prints `f"Processing data: {data}"`. Apply your `validate_input` decorator and test it with a valid string `"secure-protocol"` and an invalid `None` value.
5.  **Handling Multiple Arguments:** Write a decorator `log_arguments(func)` that prints `f"Arguments received: {args}, {kwargs}"` before calling the decorated function. Apply it to a function `send_message(recipient, message, protocol="secure")` and call it with a recipient and message.


