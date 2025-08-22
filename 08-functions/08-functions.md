# Python Functions: The Agent's Tool Kit 🔧

Welcome back, Junior Agent\! Your final lesson is on **functions**, one of the most powerful tools in a programmer's arsenal. A function is like a specialized gadget in an agent's tool kit: it's a block of reusable code designed to perform a specific task. Just like you can grab your lockpick for any locked door, you can call a function to execute a job whenever you need it.

In Python, you define a function using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.

## 1. What are Functions?

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better **modularity** for your application and a high degree of code **reusability**.

Think of a function as a recipe. It contains a set of instructions, but those instructions are only carried out when you actually "make the recipe," which in programming is called **calling** or **invoking** the function.

### Example Code:

```python
# A simple function to print a mission briefing
def print_briefing():
    print("Mission: Infiltrate the enemy base.")
    print("Objective: Retrieve the intel.")

# Now, we "call" the function to execute the code inside it
print_briefing()
```

-----

## 2. Functions with Parameters and Arguments 🤝

A function can accept data, known as **parameters**, which allows it to be more flexible. When you call the function, you pass in the actual values, known as **arguments**, that the function will use.

  - **Parameters:** The variables listed inside the parentheses `()` when you define the function (`def`).
  - **Arguments:** The actual values you pass into the function when you call it.

### Example Code:

```python
# A function that accepts a parameter 'agent_name'
def send_secure_message(agent_name):
    print(f"Sending secure message to {agent_name}...")
    print("Message received. Awaiting new orders.")

# Calling the function with a specific argument 'Agent 007'
send_secure_message("Agent 007")

# You can reuse the function with a different argument
send_secure_message("Agent Alpha")
```

-----

## 3. Returning Values: Getting a Result 📈

Many functions don't just perform an action; they also **return** a result. The `return` statement is used to send a value back to the code that called the function. This allows you to store the function's output in a variable and use it later.

### Example Code:

```python
# A function that calculates a mission score and returns the result
def calculate_mission_score(points_earned):
    total_score = points_earned + 100
    return total_score

# Call the function and store the returned value in a variable
score = calculate_mission_score(50)
print(f"Mission score is: {score}")

# The function can return any data type, including strings or booleans
def get_mission_status(score):
    if score >= 150:
        return "Mission: Success"
    else:
        return "Mission: Failure"

status = get_mission_status(score)
print(f"Mission Status: {status}")
```

-----

## 4. Function Scope: Where Variables Live 🗺️

**Scope** refers to the region of your code where a variable is accessible. Think of it as a security clearance level for your variables.

  - **Local Scope:** A variable created **inside** a function is **local** to that function. It can only be used within that function and is destroyed once the function completes its task. It's like an agent's temporary, mission-specific credentials—they only work for that single mission.
  - **Global Scope:** A variable created **outside** of any function is a **global** variable. It can be accessed from anywhere in your code, including inside functions. These are like permanent, agency-wide credentials.

Understanding scope prevents errors where a variable is "out of reach" for the part of the code trying to use it.

### Example Code:

```python
# A global variable
global_intel = "Top Secret"

def share_intel():
    # This function can access the global variable
    print(f"Inside the function, I can access global intel: {global_intel}")

    # This is a local variable; it only exists inside this function
    local_password = "password123"
    print(f"Inside the function, I have a local password: {local_password}")

# Call the function to see the variables
share_intel()

# Now, try to access the local variable from outside
try:
    print(f"Outside the function, I am trying to access the local password: {local_password}")
except NameError as e:
    print(f"Error! {e}")
```

-----

## 5. Default Parameters and Keyword Arguments 🔑

You can assign a **default value** to a parameter. If you call the function without an argument for that parameter, the default value will be used. This makes functions more versatile.

You can also use **keyword arguments** to call functions. This means you specify the name of the parameter when you pass in the argument, which can make your code more readable and lets you pass arguments in any order.

### Example Code:

```python
# A function with a default parameter 'status'
def record_log(event, status="Success"):
    print(f"Event: {event}, Status: {status}")

# Calling the function without specifying the status (default is used)
record_log("Login")

# Calling the function and overriding the default status
record_log("Data Transfer", "Warning")

# Calling the function using keyword arguments
def create_report(title, date):
    print(f"Report: {title}, Date: {date}")

# Arguments can be passed out of order using keywords
create_report(date="2024-08-22", title="Operation Shadow Report")
```

-----

## Hands-On Exercises: Tool Kit Puzzles 🧩

It's time to test your skills\! Use your new knowledge of functions to build tools for your agent's kit.

### 1. Simple Functions (5 Exercises)

1.  **Welcome Message:** Define a function `greet_agent()` that prints the message `"Hello, Agent. Your mission awaits."`. Call the function.
2.  **Mission Start:** Define a function `start_mission()` that prints `"Mission in progress..."`. Call the function.
3.  **End of Day:** Define a function `end_of_day_report()` that prints three lines: `'Day 1 Report'`, `'All systems nominal'`, and `'Awaiting new orders'`. Call the function.
4.  **Codename:** Define a function `print_codename()` that prints the string `"Pythonic Panther"`. Call the function.
5.  **Alert\!:** Define a function `sound_alert()` that prints `"!! DANGER !! DANGER !!"`. Call the function.

### 2\. Functions with Parameters (5 Exercises)

1.  **Personalized Greeting:** Define a function `greet_by_name(name)` that takes one parameter `name` and prints `f"Hello, Agent {name}."`. Call the function with your own name.
2.  **Set Mission Status:** Define a function `set_status(status)` that takes one parameter and prints `f"Mission status updated to: {status}"`. Call it with the argument `"In Progress"`.
3.  **Log an Event:** Define a function `log_event(event, timestamp)` that takes two parameters and prints them on the same line, e.g., `"Event: System Login, Timestamp: 2024-08-22"`. Call the function with two arguments.
4.  **Calculate Threat Level:** Define a function `calculate_threat(level)` that takes a number as a parameter and prints `f"Threat level is: {level}"`. Call the function with the number `7.5`.
5.  **Assign a Rank:** Define a function `assign_rank(agent, rank)` that takes two parameters and prints `f"Agent {agent} has been assigned rank {rank}."`. Call it with an agent name and a rank number.

### 3. Functions with Return Values (5 Exercises)

1.  **Get a Final Score:** Define a function `get_final_score(points)` that takes a number and returns that number multiplied by 10. Call the function with the number `5` and print the returned value.
2.  **Generate a Secret Code:** Define a function `generate_code(number)` that takes a number, converts it to a string, and returns the string `"Code-"` followed by the number. Call the function with `99` and print the returned value.
3.  **Check Mission Success:** Define a function `check_success(score)` that returns `True` if `score` is greater than 100 and `False` otherwise. Call the function with a score of `120` and print the result.
4.  **Create a Report Title:** Define a function `create_title(report_name)` that returns the string `"CLASSIFIED: "` followed by the `report_name` in uppercase. Call the function with `"project phoenix"` and print the result.
5.  **Calculate Total Damage:** Define a function `calculate_damage(hits)` that returns the number of `hits` squared. Call it with `4` and print the result.

### 4. Function Scope (5 Exercises)

1.  **Global Variable Access:** Create a global variable `mission_name = "Operation Alpha"`. Define a function `print_mission()` that prints the value of this global variable. Call the function.
2.  **Local Variable Creation:** Define a function `create_local_variable()` that creates a local variable `local_data = "Temporary Log"`. After the function definition, try to print the `local_data` variable outside the function and observe the `NameError`.
3.  **Global and Local Interaction:** Create a global variable `message = "Global Message"`. Define a function `change_message()` that creates a **local** variable also named `message` and sets it to `"Local Message"`. Print both the global `message` before and after calling the function to show that the global variable was not affected.
4.  **Using a Global Variable Inside a Function:** Create a global variable `agent_id = "007"`. Define a function `access_agent_id()` that prints `f"Agent ID is {agent_id}"`. Call the function.
5.  **The `global` Keyword:** Create a global variable `counter = 0`. Define a function `increment_counter()` that uses the `global` keyword to modify the `counter` and adds `1` to it. Call the function twice and print the value of `counter` after both calls.

### 5. Default Parameters and Keyword Arguments (5 Exercises)

1.  **Default Agent:** Define a function `default_agent(name="Agent 007")` that prints the agent's name. Call the function once without any arguments and once with the argument `"Agent Alpha"`.
2.  **Mission Report with Default:** Define a function `mission_report(status, agent="Agent X")` with a default agent name. Call the function once with just the `status` as `"Success"` and once with both `status` and `agent` as `"Failure"` and `"Agent Y"`.
3.  **Keyword Message:** Define a function `send_message(recipient, message)` that prints a message to a recipient. Call the function using keyword arguments so that the `message` argument comes first.
4.  **Default Protocol:** Define a function `connect_server(server, protocol="TCP")` with a default protocol. Call the function once without specifying the protocol and once with the protocol as `"UDP"`.
5.  **Keyword Report:** Define a function `log_report(report_id, agent_id, date)` with no default values. Call the function using keyword arguments and pass them in the order: `date`, `report_id`, `agent_id`.


