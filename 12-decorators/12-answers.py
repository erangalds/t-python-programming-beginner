# ==============================================================================
# SOLUTIONS FOR HANDS-ON DECORATORS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 10 story-based questions.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: Basic Decorators
# ------------------------------------------------------------------------------

# Question 1: A Simple Spy Decorator
# Thought Process: A decorator is a function that returns a wrapper function.
def spy_mode_on(func):
    def wrapper():
        print("Entering stealth mode...")
        func()
        print("Exiting stealth mode.")
    return wrapper

# Question 2: Decorate a Function
# Thought Process: We use the '@' syntax directly above the function definition.
@spy_mode_on
def infiltrate_base():
    print("Infiltrating the base.")

infiltrate_base()

# Question 3: Confirming Mission
# Thought Process: A basic decorator to add a pre-execution message.
def confirm_mission(func):
    def wrapper():
        print("Mission confirmed.")
        func()
    return wrapper

@confirm_mission
def execute_mission():
    print("Executing primary mission.")

execute_mission()

# Question 4: Logging a Function Call
# Thought Process: The wrapper function can access the original function's name using func.__name__.
def log_call(func):
    def wrapper():
        print(f"Calling {func.__name__}...")
        func()
    return wrapper

@log_call
def get_intel():
    print("Retrieving classified intelligence.")

get_intel()

# Question 5: A Countdown
# Thought Process: A decorator can add any logic, including a countdown.
def countdown_timer(func):
    def wrapper():
        print("3... 2... 1...")
        func()
    return wrapper

@countdown_timer
def launch_drone():
    print("Drone launched successfully.")

launch_drone()

# ------------------------------------------------------------------------------
# Section 2: Decorators with Arguments
# ------------------------------------------------------------------------------

# Question 1: Authorization Check
# Thought Process: The wrapper function must accept arguments and pass them to the decorated function.
def authorize(func):
    def wrapper(*args, **kwargs):
        # The clearance level is the first positional argument
        level = args[0]
        if level >= 10:
            return func(*args, **kwargs)
        else:
            print("Insufficient authorization.")
    return wrapper

# Question 2: Test the Decorator
# Thought Process: Apply the decorator and call the function with different arguments to test the logic.
@authorize
def view_top_secret_file(level):
    print("Accessing top secret file.")

view_top_secret_file(12)
view_top_secret_file(8)

# Question 3: Validate Arguments
# Thought Process: The wrapper checks the argument's validity before proceeding.
def validate_input(func):
    def wrapper(data):
        if data is not None and isinstance(data, str):
            func(data)
        else:
            print("Invalid input.")
    return wrapper

# Question 4: Test the Validator
# Thought Process: Apply the decorator and test with both valid and invalid data.
@validate_input
def process_data(data):
    print(f"Processing data: {data}")

process_data("secure-protocol")
process_data(None)

# Question 5: Handling Multiple Arguments
# Thought Process: We use *args and **kwargs in the wrapper to capture all arguments.
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments received: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def send_message(recipient, message, protocol="secure"):
    print(f"Sending '{message}' to {recipient} via {protocol}.")

send_message("HQ", "Intel delivered.")
send_message(recipient="HQ", message="Intel delivered.", protocol="encrypted")