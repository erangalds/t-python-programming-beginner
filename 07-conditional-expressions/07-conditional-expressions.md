# **Python Conditional Expressions: The Agent's Decision Tree 🕵️‍♂️**

Welcome to your next briefing, Junior Agent\! Today, we're covering **conditional expressions**, which are the logic gates of programming. They are the tools that allow your code to make decisions, execute different paths based on various inputs, and respond dynamically to changing circumstances. Think of them as the agent's internal compass, always pointing the right way based on the available intelligence.

In Python, the primary conditional expressions are `if`, `elif`, and `else`. They allow you to control the flow of your program.

-----

## **1. The `if` Statement: A Basic Check**

The `if` statement is the simplest form of a conditional expression. It checks if a specific condition is `True`. If it is, a block of indented code is executed. If the condition is `False`, the code block is skipped.

**Example Code:**

```python
# Check if a mission is successful
mission_successful = True

if mission_successful:
    print("Mission complete. Awaiting debrief.")

# The code outside the 'if' block runs regardless
print("Continuing with daily operations.")
```

-----

## **2. `if...else`: Handling Two Outcomes**

The `if...else` structure is used when you have two possible outcomes: a "true" outcome and a "false" outcome. The `else` block executes only if the `if` condition is `False`.

**Example Code:**

```python
# Check if the target is in the area
target_spotted = False

if target_spotted:
    print("Engaging target.")
else:
    print("Target not found. Standing by.")
```

-----

## **3. `if...elif...else`: Handling Multiple Outcomes**

When you need to check for more than two possibilities, you use an `if...elif...else` chain. The `elif` (short for "else if") allows you to check for additional conditions. Python evaluates these conditions in order, and the first one that is `True` will have its corresponding code block executed.

**Example Code:**

```python
# Assign a security clearance level
security_level = 3

if security_level == 1:
    print("Access: Restricted")
elif security_level == 2:
    print("Access: Classified")
elif security_level == 3:
    print("Access: Top Secret")
else:
    print("Access: Denied")
```

-----

## **4. Logical and Comparison Operators: The Condition Itself**

The power of conditional expressions comes from the conditions they evaluate. These conditions are built using **comparison operators** (`>`, `<`, `==`, `!=`, `>=`, `<=`) and **logical operators** (`and`, `or`, `not`).

  - `and`: Returns `True` only if **both** conditions are `True`.
  - `or`: Returns `True` if **at least one** of the conditions is `True`.
  - `not`: Reverses the logical state of the operand.

**Example Code:**

```python
# Check for a combination of conditions
agent_status = "active"
threat_level = "high"

if agent_status == "active" and threat_level == "high":
    print("Alert! Deploying backup team.")

# Check for one of several conditions
day_of_week = "Saturday"

if day_of_week == "Saturday" or day_of_week == "Sunday":
    print("Weekend protocol: Stand down.")
```

-----

## **Hands-On Exercises: Briefing Room Puzzles 🧩**

It's time to put your conditional logic skills to the test.

### 1. The `if` Statement (5 Exercises)

1.  **Check Mission Status:** Create a variable `mission_active = True`. Write an `if` statement that prints `"Mission is currently active"` only if the variable is `True`.
2.  **Confirm Identity:** Create a variable `id_verified = True`. Write an `if` statement that prints `"Identity confirmed. You may proceed."` if the variable is `True`.
3.  **Check for Intel:** Create a variable `new_intel_available = True`. Write an `if` statement to print `"New intel has arrived."` if `new_intel_available` is `True`.
4.  **Device Check:** Create a variable `device_functional = False`. Write an `if` statement to print `"Device is not functioning."` if the variable is `False`.
5.  **Access Granted:** Create a variable `clearance_level = 5`. Write an `if` statement that prints `"Access granted"` if `clearance_level` is greater than or equal to `4`.

### 2. `if...else` (5 Exercises)

1.  **Mission Success:** A variable `score = 85`. If the `score` is greater than `75`, print `"Mission Successful"`, otherwise, print `"Mission Failed"`.
2.  **Password Check:** A variable `password = "secret"`. If the `password` is equal to `"top_secret"`, print `"Welcome, Agent"`, otherwise print `"Incorrect password"`.
3.  **Night or Day:** A variable `current_time = "10:00"`. If the `current_time` is less than `"12:00"`, print `"Day Shift"`, otherwise print `"Night Shift"`.
4.  **Weather Report:** A variable `is_raining = True`. If `is_raining` is `True`, print `"Grab an umbrella"`, otherwise print `"Leave the umbrella behind"`.
5.  **Threat Analysis:** A variable `threat_level = "low"`. If `threat_level` is equal to `"high"`, print `"Code Red"`, otherwise print `"Code Green"`.

### 3. `if...elif...else` (5 Exercises)

1.  **Rank Assignment:** A variable `agent_exp = 12`. If `agent_exp` is greater than `20`, print `"Senior Agent"`. If it's greater than `10`, print `"Veteran Agent"`. Otherwise, print `"Rookie Agent"`.
2.  **Mission Rating:** A variable `mission_rating = 7`. If the rating is greater than `8`, print `"Excellent"`. If it is between `5` and `8` (inclusive), print `"Good"`. Otherwise, print `"Poor"`.
3.  **Traffic Light:** A variable `light_color = "red"`. If `light_color` is `"green"`, print `"Go"`. If it's `"yellow"`, print `"Slow down"`. If it's `"red"`, print `"Stop"`.
4.  **Temperature Check:** A variable `temp = 25`. If `temp` is greater than `30`, print `"Hot"`. If it is between `20` and `30` (inclusive), print `"Warm"`. Otherwise, print `"Cold"`.
5.  **Intel Priority:** A variable `intel_priority = 2`. If `intel_priority` is equal to `1`, print `"Immediate Action"`. If it is `2`, print `"High Priority"`. Otherwise, print `"Low Priority"`.

### 4. Logical and Comparison Operators (5 Exercises)

1.  **Multi-Condition Access:** A variable `age = 18` and `has_id = True`. Use `and` to check if `age` is greater than or equal to `21` and `has_id` is `True`. Print "Access Denied" or "Access Granted".
2.  **Mission Readiness:** A variable `fuel_level = 50` and `ammo_count = 100`. Use `and` to check if `fuel_level` is greater than `40` and `ammo_count` is greater than `50`. If both are true, print `"Ready for deployment"`.
3.  **Fallback Plan:** A variable `main_system_online = False` and `backup_system_online = True`. Use `or` to check if `main_system_online` is `True` or `backup_system_online` is `True`. Print `"System is operational."` if the condition is met.
4.  **Inverse Check:** A variable `threat_present = True`. Use the `not` operator to check if `threat_present` is `False`. If it is, print `"All clear."`.
5.  **Complex Condition:** A variable `weather = "stormy"`, `is_daytime = False`. Use `and` and `or` to check if `weather` is `"stormy"` and `is_daytime` is `False`, OR if `weather` is `"clear"`. Print `"Go ahead with mission"` or `"Abort mission"`.


