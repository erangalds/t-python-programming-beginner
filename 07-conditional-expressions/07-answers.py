# ==============================================================================
# SOLUTIONS FOR HANDS-ON CONDITIONAL EXPRESSIONS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 20 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: The `if` Statement
# ------------------------------------------------------------------------------

# Question 1: Check Mission Status
# Thought Process: A simple 'if' statement is used to check the boolean variable.
mission_active = True
if mission_active:
    print("Mission is currently active")

# Question 2: Confirm Identity
# Thought Process: The 'if' statement checks if the boolean variable is True.
id_verified = True
if id_verified:
    print("Identity confirmed. You may proceed.")

# Question 3: Check for Intel
# Thought Process: The 'if' statement evaluates the boolean variable.
new_intel_available = True
if new_intel_available:
    print("New intel has arrived.")

# Question 4: Device Check
# Thought Process: We check if the boolean variable is equal to False.
device_functional = False
if device_functional == False:
    print("Device is not functioning.")

# Question 5: Access Granted
# Thought Process: The 'if' statement uses a comparison operator (>=) to check a condition.
clearance_level = 5
if clearance_level >= 4:
    print("Access granted")


# ------------------------------------------------------------------------------
# Section 2: `if...else`
# ------------------------------------------------------------------------------

# Question 1: Mission Success
# Thought Process: An 'if...else' is perfect for two-way decisions.
score = 85
if score > 75:
    print("Mission Successful")
else:
    print("Mission Failed")

# Question 2: Password Check
# Thought Process: We use the equality operator (==) to compare strings.
password = "secret"
if password == "top_secret":
    print("Welcome, Agent")
else:
    print("Incorrect password")

# Question 3: Night or Day
# Thought Process: We compare the string lexicographically, which works for this format.
current_time = "10:00"
if current_time < "12:00":
    print("Day Shift")
else:
    print("Night Shift")

# Question 4: Weather Report
# Thought Process: A direct check on the boolean variable.
is_raining = True
if is_raining:
    print("Grab an umbrella")
else:
    print("Leave the umbrella behind")

# Question 5: Threat Analysis
# Thought Process: A simple 'if...else' based on a string comparison.
threat_level = "low"
if threat_level == "high":
    print("Code Red")
else:
    print("Code Green")


# ------------------------------------------------------------------------------
# Section 3: `if...elif...else`
# ------------------------------------------------------------------------------

# Question 1: Rank Assignment
# Thought Process: The conditions are checked in order. The 'elif' statement prevents
# 'Veteran Agent' from being printed when the experience is above 20.
agent_exp = 12
if agent_exp > 20:
    print("Senior Agent")
elif agent_exp > 10:
    print("Veteran Agent")
else:
    print("Rookie Agent")

# Question 2: Mission Rating
# Thought Process: The 'elif' condition checks a range.
mission_rating = 7
if mission_rating > 8:
    print("Excellent")
elif mission_rating >= 5 and mission_rating <= 8:
    print("Good")
else:
    print("Poor")

# Question 3: Traffic Light
# Thought Process: A chained conditional statement to check multiple possible values.
light_color = "red"
if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Slow down")
elif light_color == "red":
    print("Stop")

# Question 4: Temperature Check
# Thought Process: We use comparison operators in a chained conditional.
temp = 25
if temp > 30:
    print("Hot")
elif temp >= 20 and temp <= 30:
    print("Warm")
else:
    print("Cold")

# Question 5: Intel Priority
# Thought Process: A simple 'if...elif...else' based on a number.
intel_priority = 2
if intel_priority == 1:
    print("Immediate Action")
elif intel_priority == 2:
    print("High Priority")
else:
    print("Low Priority")


# ------------------------------------------------------------------------------
# Section 4: Logical and Comparison Operators
# ------------------------------------------------------------------------------

# Question 1: Multi-Condition Access
# Thought Process: We use the 'and' operator to ensure both conditions are true.
age = 18
has_id = True
if age >= 21 and has_id:
    print("Access Granted")
else:
    print("Access Denied")

# Question 2: Mission Readiness
# Thought Process: Two conditions must be met for the deployment message to print.
fuel_level = 50
ammo_count = 100
if fuel_level > 40 and ammo_count > 50:
    print("Ready for deployment")

# Question 3: Fallback Plan
# Thought Process: The 'or' operator checks if at least one of the systems is online.
main_system_online = False
backup_system_online = True
if main_system_online or backup_system_online:
    print("System is operational.")

# Question 4: Inverse Check
# Thought Process: The 'not' operator flips the boolean value of the variable.
threat_present = True
if not threat_present:
    print("All clear.")

# Question 5: Complex Condition
# Thought Process: We combine 'and' and 'or' to create a complex logical statement.
weather = "stormy"
is_daytime = False
if (weather == "stormy" and not is_daytime) or weather == "clear":
    print("Go ahead with mission")
else:
    print("Abort mission")
