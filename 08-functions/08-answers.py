# ==============================================================================
# SOLUTIONS FOR HANDS-ON FUNCTIONS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 25 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: Simple Functions
# ------------------------------------------------------------------------------

# Question 1: Welcome Message
# Thought Process: Define a function with 'def' and use a print statement inside.
def greet_agent():
    print("Hello, Agent. Your mission awaits.")

greet_agent()

# Question 2: Mission Start
# Thought Process: Define a function to contain a simple print command.
def start_mission():
    print("Mission in progress...")

start_mission()

# Question 3: End of Day
# Thought Process: A single function can contain multiple lines of code.
def end_of_day_report():
    print("Day 1 Report")
    print("All systems nominal")
    print("Awaiting new orders")

end_of_day_report()

# Question 4: Codename
# Thought Process: Define and call a simple function to print a string.
def print_codename():
    print("Pythonic Panther")

print_codename()

# Question 5: Alert!
# Thought Process: Define a function to print the alert message.
def sound_alert():
    print("!! DANGER !! DANGER !!")

sound_alert()


# ------------------------------------------------------------------------------
# Section 2: Functions with Parameters
# ------------------------------------------------------------------------------

# Question 1: Personalized Greeting
# Thought Process: The function takes one parameter, which is used inside the f-string.
def greet_by_name(name):
    print(f"Hello, Agent {name}.")

greet_by_name("Alex")

# Question 2: Set Mission Status
# Thought Process: The function accepts a 'status' argument and uses it in the output.
def set_status(status):
    print(f"Mission status updated to: {status}")

set_status("In Progress")

# Question 3: Log an Event
# Thought Process: The function takes two parameters and combines them in the print statement.
def log_event(event, timestamp):
    print(f"Event: {event}, Timestamp: {timestamp}")

log_event("System Login", "2024-08-22")

# Question 4: Calculate Threat Level
# Thought Process: The function takes a number and includes it in the printed string.
def calculate_threat(level):
    print(f"Threat level is: {level}")

calculate_threat(7.5)

# Question 5: Assign a Rank
# Thought Process: The function takes two parameters and uses them to format a sentence.
def assign_rank(agent, rank):
    print(f"Agent {agent} has been assigned rank {rank}.")

assign_rank("Bravo", 2)


# ------------------------------------------------------------------------------
# Section 3: Functions with Return Values
# ------------------------------------------------------------------------------

# Question 1: Get a Final Score
# Thought Process: The function uses 'return' to send back the result of the calculation.
def get_final_score(points):
    return points * 10

final_score = get_final_score(5)
print(final_score)

# Question 2: Generate a Secret Code
# Thought Process: The function builds a string and returns it.
def generate_code(number):
    return "Code-" + str(number)

secret_code = generate_code(99)
print(secret_code)

# Question 3: Check Mission Success
# Thought Process: The function uses a conditional statement and returns a boolean value.
def check_success(score):
    if score > 100:
        return True
    else:
        return False

success_status = check_success(120)
print(success_status)

# Question 4: Create a Report Title
# Thought Process: The function returns a formatted string.
def create_title(report_name):
    return "CLASSIFIED: " + report_name.upper()

report_title = create_title("project phoenix")
print(report_title)

# Question 5: Calculate Total Damage
# Thought Process: The function performs a mathematical operation and returns the result.
def calculate_damage(hits):
    return hits ** 2

damage = calculate_damage(4)
print(damage)


# ------------------------------------------------------------------------------
# Section 4: Function Scope
# ------------------------------------------------------------------------------

# Question 1: Global Variable Access
# Thought Process: The variable is defined outside the function, making it global and
# accessible within the function's scope.
mission_name = "Operation Alpha"
def print_mission():
    print(f"Current mission is: {mission_name}")

print_mission()

# Question 2: Local Variable Creation
# Thought Process: A local variable cannot be accessed outside its function.
def create_local_variable():
    local_data = "Temporary Log"
    print(f"Inside the function, local_data is: {local_data}")

create_local_variable()
try:
    print(local_data)
except NameError as e:
    print(f"Error: {e}")

# Question 3: Global and Local Interaction
# Thought Process: A local variable with the same name as a global one does not
# affect the global variable.
message = "Global Message"
def change_message():
    message = "Local Message"
    print(f"Inside the function, local message is: {message}")

print(f"Before calling function, global message is: {message}")
change_message()
print(f"After calling function, global message is: {message}")

# Question 4: Using a Global Variable Inside a Function
# Thought Process: Accessing a global variable inside a function is permitted.
agent_id = "007"
def access_agent_id():
    print(f"Agent ID is {agent_id}")

access_agent_id()

# Question 5: The `global` Keyword
# Thought Process: We must use the 'global' keyword to explicitly state that we
# want to modify the global variable from within the function.
counter = 0
def increment_counter():
    global counter
    counter += 1

print(f"Initial counter: {counter}")
increment_counter()
print(f"After first call: {counter}")
increment_counter()
print(f"After second call: {counter}")


# ------------------------------------------------------------------------------
# Section 5: Default Parameters and Keyword Arguments
# ------------------------------------------------------------------------------

# Question 1: Default Agent
# Thought Process: The 'name' parameter is given a default value.
def default_agent(name="Agent 007"):
    print(f"Agent: {name}")

default_agent()
default_agent("Agent Alpha")

# Question 2: Mission Report with Default
# Thought Process: The 'agent' parameter has a default value that can be overridden.
def mission_report(status, agent="Agent X"):
    print(f"Status: {status}, Agent: {agent}")

mission_report("Success")
mission_report("Failure", "Agent Y")

# Question 3: Keyword Message
# Thought Process: We explicitly name the parameters when calling the function.
def send_message(recipient, message):
    print(f"To: {recipient}, Message: {message}")

send_message(message="New intel received.", recipient="Agent 007")

# Question 4: Default Protocol
# Thought Process: The 'protocol' parameter has a default value.
def connect_server(server, protocol="TCP"):
    print(f"Connecting to server '{server}' using protocol '{protocol}'.")

connect_server("10.0.0.1")
connect_server("10.0.0.2", "UDP")

# Question 5: Keyword Report
# Thought Process: Keyword arguments allow us to pass arguments in any order.
def log_report(report_id, agent_id, date):
    print(f"Report ID: {report_id}, Agent ID: {agent_id}, Date: {date}")

log_report(date="2024-08-22", report_id="R-99", agent_id="A-55")
