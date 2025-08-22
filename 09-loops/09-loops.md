# **Python Loops: The Agent's Repetitive Task Automation 🤖**

Welcome to your next briefing, Junior Agent\! Today, we're covering **loops**, which are essential for automating repetitive tasks. A loop is a programming construct that executes a block of code multiple times. Think of them as a set of automated instructions, like a robot performing the same action repeatedly until a specific goal is achieved.

Python offers two main types of loops: `for` loops and `while` loops. They both automate tasks, but they do it in different ways.

-----

## **1. The `for` Loop: Iterating Over a Sequence**

A `for` loop is used to iterate over a sequence of items, such as a list, tuple, or string. It executes a block of code once for each item in the sequence. This is the go-to loop when you know exactly how many times you need to repeat an action.

**Example Code:**

```python
# Iterate through a list of mission objectives
mission_objectives = ['infiltrate', 'secure', 'extract']

for objective in mission_objectives:
    print(f"Current objective: {objective}")
    print("Executing...")

print("All objectives completed.")
```

  - **The `range()` Function:** A common use of `for` loops is with the `range()` function, which generates a sequence of numbers.
      - `range(stop)`: Generates numbers from `0` up to (but not including) `stop`.
      - `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
      - `range(start, stop, step)`: Generates numbers from `start` up to (but not including) `stop`, with a specific `step` value.

**Example Code:**

```python
# Loop a specific number of times
print("Counting down for launch:")
for i in range(5, 0, -1):
    print(f"{i}...")
print("Launch!")
```

-----

## **2. The `while` Loop: Repeating Until a Condition is Met**

A `while` loop executes a block of code as long as a specified condition is `True`. It's perfect for situations where you don't know in advance how many times the loop needs to run. The loop will continue to run until the condition becomes `False`.

**Important:** You must include code inside the loop that eventually makes the condition `False`. Otherwise, you'll create an **infinite loop**, and your program will never stop.

**Example Code:**

```python
# A simple while loop
security_breach_count = 0
max_breaches = 3

while security_breach_count < max_breaches:
    print(f"Warning! Security breach detected. Breach count: {security_breach_count + 1}")
    security_breach_count += 1 # This line is crucial to prevent an infinite loop

print("Lockdown protocol initiated.")
```

-----

## **3. Controlling Loop Flow: `break` and `continue`**

Sometimes you need to modify the default behavior of a loop. The `break` and `continue` statements give you fine-grained control.

  - `break`: Immediately **exits** the entire loop. It's used to stop a loop prematurely.
  - `continue`: **Skips** the rest of the current iteration and jumps to the next one.

**Example Code:**

```python
# Using break to exit a loop early
secret_codes = ['alpha', 'beta', 'gamma', 'STOP', 'delta']

for code in secret_codes:
    if code == 'STOP':
        print("Termination code received. Aborting loop.")
        break # Exit the loop immediately
    print(f"Processing code: {code}")

# Using continue to skip an iteration
mission_log = ['start', 'error', 'proceed', 'error', 'complete']

for entry in mission_log:
    if entry == 'error':
        print("Skipping corrupted log entry.")
        continue # Skip this iteration and go to the next one
    print(f"Processing log entry: {entry}")
```

-----

## **Hands-On Exercises: Automation Puzzles 🧩**

It's time to test your loop skills to automate some tasks.

### **1. `for` Loops (5 Exercises)**

1.  **Iterate Over a Team:** A list of agents is `agents = ['Alpha', 'Bravo', 'Charlie']`. Use a `for` loop to print each agent's name.
2.  **Count Down:** Use a `for` loop and the `range()` function to count down from 5 to 1. Print each number.
3.  **Process Mission Reports:** A list of reports is `reports = ['Report A', 'Report B', 'Report C']`. Use a `for` loop to print `"Processing:"` followed by each report name.
4.  **Count Up:** Use a `for` loop and `range()` to count from 0 to 4 (inclusive). Print each number.
5.  **Iterate Over a String:** A classified word is `word = "secret"`. Use a `for` loop to print each character in the word on a new line.

### **2. `while` Loops (5 Exercises)**

1.  **Password Attempts:** A variable `attempts_left = 3`. Use a `while` loop to print `"Attempting to connect..."` as long as `attempts_left` is greater than 0. Inside the loop, decrease `attempts_left` by 1.
2.  **Waiting for Data:** A variable `data_received = False`. Use a `while` loop that prints `"Waiting for data..."` as long as `data_received` is `False`. Inside the loop, use a variable and a conditional to change `data_received` to `True` after one iteration.
3.  **Intel Download:** A variable `progress = 0`. Use a `while` loop that prints `f"Download progress: {progress}%"` and adds 20 to `progress` each time, until `progress` is 100.
4.  **Security Check:** A variable `threat_level = 5`. Use a `while` loop that prints `"Threat level is high. Engaging protocols..."` and decreases `threat_level` by 1 each time, until `threat_level` is 0.
5.  **Infinite Loop (with a catch):** Create a `while True:` loop. Inside the loop, print `"Scanning..."` and then use an `if` statement and a counter to `break` the loop after 3 iterations.

### **3. Controlling Loops (5 Exercises)**

1.  **Break on Target Found:** A list of locations is `locations = ['A', 'B', 'C', 'TARGET', 'D']`. Use a `for` loop to iterate through the list. When the loop finds `'TARGET'`, print `"Target found! Mission complete."` and `break` the loop.
2.  **Continue on Error:** A list of log entries is `log = ['OK', 'ERROR', 'OK', 'ERROR', 'OK']`. Use a `for` loop to iterate. When the loop finds `'ERROR'`, print `"Skipping error..."` and `continue` to the next entry. For all `'OK'` entries, print `"Processing log."`.
3.  **Password Attempts (with break):** Use a `for` loop and `range(3)` to simulate 3 password attempts. Inside the loop, print the attempt number. Add an `if` statement to `break` if a correct password `("secret_code")` is guessed on the second attempt.
4.  **Skip Odd Numbers:** Use a `for` loop and `range(1, 10)` to iterate from 1 to 9. Use an `if` statement with `continue` to skip all odd numbers and only print the even numbers.
5.  **Search and Exit:** A list of threats is `threats = ['low', 'low', 'high', 'low']`. Use a `for` loop to print each threat. If a `high` threat is found, print `"High threat detected, aborting mission!"` and exit the loop using `break`.


